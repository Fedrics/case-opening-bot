from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy.orm import Session
import uvicorn
import logging
import hashlib
import hmac
import json
import os
from urllib.parse import unquote
from datetime import datetime
import random

import config
from database import get_db, User, CaseOpening, Transaction

# Initialize FastAPI app
app = FastAPI(title="Case Opening Bot WebApp")

# Setup templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def verify_telegram_data(init_data: str, bot_token: str) -> dict:
    """Verify Telegram WebApp init data"""
    try:
        # Handle URL encoded data
        from urllib.parse import unquote_plus
        init_data = unquote_plus(init_data)
        
        # Parse init data - handle single values properly
        parsed_data = {}
        for item in init_data.split('&'):
            if '=' in item:
                key, value = item.split('=', 1)
                parsed_data[key] = value
            else:
                # Skip malformed parameters
                continue
                
        hash_value = parsed_data.pop('hash', None)
        
        if not hash_value:
            logger.warning("No hash in init data")
            return None
            
        # Create data check string
        data_check_arr = []
        for key, value in sorted(parsed_data.items()):
            data_check_arr.append(f"{key}={value}")
        data_check_string = '\n'.join(data_check_arr)
        
        # Calculate hash
        secret_key = hmac.new(b"WebAppData", bot_token.encode(), hashlib.sha256).digest()
        calculated_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()
        
        if calculated_hash == hash_value:
            # Parse user data
            user_data = json.loads(unquote(parsed_data.get('user', '{}')))
            return user_data
        else:
            logger.warning(f"Hash mismatch: {calculated_hash} != {hash_value}")
            return None
    except Exception as e:
        logger.error(f"Error verifying telegram data: {e}")
        return None

def get_or_create_user(telegram_id: int, user_data: dict, db: Session) -> User:
    """Get existing user or create new one"""
    user = db.query(User).filter(User.telegram_id == telegram_id).first()
    if not user:
        user = User(
            telegram_id=telegram_id,
            username=user_data.get('username'),
            first_name=user_data.get('first_name'),
            last_name=user_data.get('last_name')
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    else:
        # Update user data
        user.username = user_data.get('username')
        user.first_name = user_data.get('first_name')
        user.last_name = user_data.get('last_name')
        user.last_activity = datetime.utcnow()
        db.commit()
    
    return user

@app.get("/health")
async def health_check():
    """Health check endpoint for Railway"""
    return {"status": "healthy", "service": "case-opening-bot"}

@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request, init_data: str = None, db: Session = Depends(get_db)):
    """Main case opening page"""
    if not init_data:
        return templates.TemplateResponse("error.html", {
            "request": request, 
            "error": "Unauthorized access - no init data"
        })
    
    # Handle placeholder init_data from template
    if init_data == "{init_data}" or init_data == "%7Binit_data%7D":
        # Create demo user for testing
        demo_user_data = {
            'id': 123456789,
            'username': 'demo_user',
            'first_name': 'Demo',
            'last_name': 'User'
        }
        user = get_or_create_user(demo_user_data['id'], demo_user_data, db)
        
        return templates.TemplateResponse("index.html", {
            "request": request,
            "user": user,
            "cases": config.CASES,
            "init_data": "demo_mode"
        })
    
    # Verify telegram data
    user_data = verify_telegram_data(init_data, config.BOT_TOKEN)
    if not user_data:
        return templates.TemplateResponse("error.html", {
            "request": request,
            "error": "Invalid authorization data - verification failed"
        })
    
    # Get or create user
    user = get_or_create_user(user_data['id'], user_data, db)
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "user": user,
        "cases": config.CASES,
        "init_data": init_data
    })

@app.post("/api/open_case")
async def open_case(request: Request, db: Session = Depends(get_db)):
    """Open a case and return reward"""
    data = await request.json()
    init_data = data.get('init_data')
    case_type = data.get('case_type')
    
    if not init_data or not case_type:
        raise HTTPException(status_code=400, detail="Missing required data")
    
    # Verify telegram data
    user_data = verify_telegram_data(init_data, config.BOT_TOKEN)
    if not user_data:
        raise HTTPException(status_code=401, detail="Invalid authorization")
    
    # Check if case type exists
    if case_type not in config.CASES:
        raise HTTPException(status_code=400, detail="Invalid case type")
    
    case_config = config.CASES[case_type]
    user = get_or_create_user(user_data['id'], user_data, db)
    
    # Check if user has enough balance
    if user.balance < case_config['price']:
        raise HTTPException(status_code=400, detail="Insufficient balance")
    
    # Select reward based on probability
    reward = select_reward(case_config)
    
    # Deduct case price from balance
    user.balance -= case_config['price']
    user.total_spent += case_config['price']
    user.cases_opened += 1
    
    # Add reward to balance
    user.balance += reward['value']
    user.total_won += reward['value']
    
    # Record case opening
    case_opening = CaseOpening(
        user_id=user.id,
        case_type=case_type,
        case_price=case_config['price'],
        reward_name=reward['name'],
        reward_value=reward['value'],
        reward_rarity=reward['rarity']
    )
    
    db.add(case_opening)
    db.commit()
    
    return JSONResponse({
        "success": True,
        "reward": reward,
        "new_balance": user.balance,
        "case_price": case_config['price']
    })

def select_reward(case_config):
    """Select reward based on probability"""
    rand = random.random() * 100
    current_prob = 0
    
    for rarity in ['common', 'uncommon', 'rare', 'epic', 'legendary']:
        if rarity not in case_config['rewards']:
            continue
            
        prob = case_config['rewards'][rarity]['probability']
        current_prob += prob
        
        if rand <= current_prob:
            rewards = case_config['rewards'][rarity]['items']
            selected_reward = random.choice(rewards)
            return {
                'name': selected_reward['name'],
                'value': selected_reward['value'],
                'rarity': rarity,
                'image': selected_reward.get('image', 'default.png')
            }
    
    # Fallback to common reward
    rewards = case_config['rewards']['common']['items']
    selected_reward = random.choice(rewards)
    return {
        'name': selected_reward['name'],
        'value': selected_reward['value'],
        'rarity': 'common',
        'image': selected_reward.get('image', 'default.png')
    }

@app.get("/api/user_stats")
async def get_user_stats(init_data: str, db: Session = Depends(get_db)):
    """Get user statistics"""
    user_data = verify_telegram_data(init_data, config.BOT_TOKEN)
    if not user_data:
        raise HTTPException(status_code=401, detail="Invalid authorization")
    
    user = get_or_create_user(user_data['id'], user_data, db)
    
    return JSONResponse({
        "balance": user.balance,
        "total_spent": user.total_spent,
        "total_won": user.total_won,
        "cases_opened": user.cases_opened,
        "profit": user.total_won - user.total_spent
    })

@app.get("/api/recent_openings")
async def get_recent_openings(init_data: str, limit: int = 10, db: Session = Depends(get_db)):
    """Get recent case openings for user"""
    user_data = verify_telegram_data(init_data, config.BOT_TOKEN)
    if not user_data:
        raise HTTPException(status_code=401, detail="Invalid authorization")
    
    user = get_or_create_user(user_data['id'], user_data, db)
    
    openings = db.query(CaseOpening).filter(
        CaseOpening.user_id == user.id
    ).order_by(CaseOpening.opened_at.desc()).limit(limit).all()
    
    result = []
    for opening in openings:
        result.append({
            "case_type": opening.case_type,
            "reward_name": opening.reward_name,
            "reward_value": opening.reward_value,
            "reward_rarity": opening.reward_rarity,
            "opened_at": opening.opened_at.isoformat()
        })
    
    return JSONResponse(result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port, debug=True)