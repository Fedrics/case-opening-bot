import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from sqlalchemy.orm import Session
import uvicorn
from threading import Thread

import config
from database import create_tables, SessionLocal, User, Transaction, PaymentInvoice
from main import app

# Initialize bot and dispatcher
bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

def get_or_create_user(telegram_id: int, username: str = None, first_name: str = None, last_name: str = None) -> User:
    """Get existing user or create new one"""
    db = get_db()
    user = db.query(User).filter(User.telegram_id == telegram_id).first()
    if not user:
        user = User(
            telegram_id=telegram_id,
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    
    db.close()
    return user

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    """Handle /start command"""
    user = get_or_create_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )
    
    webapp_url = f"{config.WEB_APP_URL}?init_data={{init_data}}"
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🎁 Открыть кейсы",
                web_app=WebAppInfo(url=webapp_url)
            )
        ],
        [
            InlineKeyboardButton(text="💰 Пополнить баланс", callback_data="deposit"),
            InlineKeyboardButton(text="📊 Статистика", callback_data="stats")
        ]
    ])
    
    welcome_text = f"""
🎉 <b>Добро пожаловать в Case Opening Bot!</b>

Привет, <b>{user.first_name}</b>! 

🎁 Открывай кейсы и получай крутые награды!
⭐ Твой текущий баланс: <b>{user.balance:.0f} Stars</b>

<b>Доступные кейсы:</b>
🌟 Стартовый кейс - 50 ⭐
💎 Премиум кейс - 150 ⭐
🎮 Gaming кейс - 300 ⭐
� Мега кейс - 500 ⭐

Нажми кнопку ниже, чтобы начать играть!
    """
    
    await message.answer(welcome_text, reply_markup=keyboard)

@dp.callback_query(lambda c: c.data == "deposit")
async def deposit_handler(callback_query: types.CallbackQuery):
    """Handle deposit button"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="⭐ Telegram Stars", callback_data="deposit_stars"),
        ],
        [
            InlineKeyboardButton(text="₿ Криптовалюта", callback_data="deposit_crypto"),
        ],
        [
            InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_main")
        ]
    ])
    
    text = """
💰 <b>Пополнение баланса</b>

Выберите способ пополнения:

⭐ <b>Telegram Stars</b>
• Быстрое пополнение
• Официальный способ оплаты Telegram
• Комиссия ~5%

₿ <b>Криптовалюта</b>
• USDT, TON, BTC, ETH
• Минимальная комиссия
• Обработка до 10 минут
    """
    
    await callback_query.message.edit_text(text, reply_markup=keyboard)

@dp.callback_query(lambda c: c.data == "deposit_stars")
async def deposit_stars_handler(callback_query: types.CallbackQuery):
    """Handle Telegram Stars deposit"""
    amounts = [100, 250, 500, 1000, 2500, 5000]
    
    keyboard_buttons = []
    for i in range(0, len(amounts), 2):
        row = []
        for j in range(i, min(i + 2, len(amounts))):
            amount = amounts[j]
            row.append(InlineKeyboardButton(
                text=f"{amount} ⭐",
                callback_data=f"stars_{amount}"
            ))
        keyboard_buttons.append(row)
    
    keyboard_buttons.append([
        InlineKeyboardButton(text="🔙 Назад", callback_data="deposit")
    ])
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)
    
    text = """
⭐ <b>Пополнение через Telegram Stars</b>

Выберите сумму для пополнения:

<i>После оплаты баланс будет пополнен автоматически</i>
    """
    
    await callback_query.message.edit_text(text, reply_markup=keyboard)

@dp.callback_query(lambda c: c.data.startswith("stars_"))
async def process_stars_payment(callback_query: types.CallbackQuery):
    """Process Telegram Stars payment"""
    try:
        amount = int(callback_query.data.split("_")[1])
        
        # Create invoice for Telegram Stars
        invoice = await bot.create_invoice_link(
            title=f"Пополнение баланса на {amount} ⭐",
            description=f"Пополнение баланса в Case Opening Bot",
            payload=f"stars_{callback_query.from_user.id}_{amount}",
            provider_token="",  # Empty for Stars
            currency="XTR",  # Telegram Stars currency
            prices=[types.LabeledPrice(label=f"Пополнение на {amount} Stars", amount=amount)]
        )
        
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=f"💳 Оплатить {amount} ⭐", url=invoice)],
            [InlineKeyboardButton(text="🔙 Назад", callback_data="deposit_stars")]
        ])
        
        text = f"""
💳 <b>Оплата {amount} Telegram Stars</b>

Нажмите кнопку ниже для оплаты.

После успешной оплаты ваш баланс будет автоматически пополнен на {amount} ⭐
        """
        
        await callback_query.message.edit_text(text, reply_markup=keyboard)
        
    except Exception as e:
        logger.error(f"Error creating stars invoice: {e}")
        await callback_query.answer("Ошибка при создании счета", show_alert=True)

@dp.pre_checkout_query()
async def pre_checkout_handler(pre_checkout_query: types.PreCheckoutQuery):
    """Handle pre-checkout query for Telegram Stars"""
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@dp.message(lambda message: message.successful_payment is not None)
async def successful_payment_handler(message: types.Message):
    """Handle successful payment"""
    payment = message.successful_payment
    payload_data = payment.invoice_payload.split("_")
    
    if len(payload_data) >= 3 and payload_data[0] == "stars":
        user_id = int(payload_data[1])
        amount = int(payload_data[2])
        
        # Update user balance
        db = get_db()
        user = db.query(User).filter(User.telegram_id == user_id).first()
        if user:
            user.balance += amount
            
            # Record transaction
            transaction = Transaction(
                user_id=user.id,
                transaction_type="deposit",
                amount=amount,
                payment_method="stars",
                payment_id=payment.telegram_payment_charge_id,
                status="completed",
                description=f"Пополнение через Telegram Stars на {amount} ⭐"
            )
            
            db.add(transaction)
            db.commit()
            db.close()
            
            await message.answer(
                f"✅ <b>Платеж успешно обработан!</b>\n\n"
                f"💰 Ваш баланс пополнен на <b>{amount} ⭐</b>\n"
                f"🏦 Текущий баланс: <b>{user.balance:.0f} ⭐</b>\n\n"
                f"Спасибо за пополнение! Теперь вы можете открывать кейсы! 🎁"
            )

@dp.callback_query(lambda c: c.data == "stats")
async def stats_handler(callback_query: types.CallbackQuery):
    """Handle stats button"""
    db = get_db()
    user = db.query(User).filter(User.telegram_id == callback_query.from_user.id).first()
    
    if not user:
        user = get_or_create_user(callback_query.from_user.id)
    
    profit = user.total_won - user.total_spent
    profit_text = f"+{profit:.0f}" if profit >= 0 else f"{profit:.0f}"
    profit_emoji = "📈" if profit >= 0 else "📉"
    
    text = f"""
📊 <b>Ваша статистика</b>

👤 <b>Игрок:</b> {user.first_name}
💰 <b>Баланс:</b> {user.balance:.0f} ⭐

🎁 <b>Кейсы открыто:</b> {user.cases_opened}
💸 <b>Всего потрачено:</b> {user.total_spent:.0f} ⭐
💎 <b>Всего выиграно:</b> {user.total_won:.0f} ⭐
{profit_emoji} <b>Прибыль:</b> {profit_text} ⭐

📅 <b>Регистрация:</b> {user.created_at.strftime("%d.%m.%Y")}
    """
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_main")]
    ])
    
    await callback_query.message.edit_text(text, reply_markup=keyboard)
    db.close()

@dp.callback_query(lambda c: c.data == "back_to_main")
async def back_to_main_handler(callback_query: types.CallbackQuery):
    """Handle back to main menu"""
    user = get_or_create_user(
        telegram_id=callback_query.from_user.id,
        username=callback_query.from_user.username,
        first_name=callback_query.from_user.first_name,
        last_name=callback_query.from_user.last_name
    )
    
    webapp_url = f"{config.WEB_APP_URL}?init_data={{init_data}}"
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🎁 Открыть кейсы",
                web_app=WebAppInfo(url=webapp_url)
            )
        ],
        [
            InlineKeyboardButton(text="💰 Пополнить баланс", callback_data="deposit"),
            InlineKeyboardButton(text="📊 Статистика", callback_data="stats")
        ]
    ])
    
    welcome_text = f"""
🎉 <b>Case Opening Bot</b>

Привет, <b>{user.first_name}</b>! 

🎁 Открывай кейсы и получай крутые награды!
⭐ Твой текущий баланс: <b>{user.balance:.0f} Stars</b>

<b>Доступные кейсы:</b>
🌟 Стартовый кейс - 50 ⭐
💎 Премиум кейс - 150 ⭐
🎮 Gaming кейс - 300 ⭐
� Мега кейс - 500 ⭐

Нажми кнопку ниже, чтобы начать играть!
    """
    
    await callback_query.message.edit_text(welcome_text, reply_markup=keyboard)

# Admin commands (for testing)
@dp.message(Command("add_balance"))
async def add_balance_handler(message: types.Message):
    """Admin command to add balance for testing"""
    if message.from_user.id != config.ADMIN_ID:
        return
    
    try:
        args = message.text.split()
        if len(args) < 2:
            await message.answer("Использование: /add_balance <сумма>")
            return
        
        amount = float(args[1])
        db = get_db()
        user = db.query(User).filter(User.telegram_id == message.from_user.id).first()
        
        if user:
            user.balance += amount
            
            # Record transaction
            transaction = Transaction(
                user_id=user.id,
                transaction_type="deposit",
                amount=amount,
                payment_method="admin",
                status="completed",
                description=f"Тестовое пополнение админом на {amount} ⭐"
            )
            
            db.add(transaction)
            db.commit()
            
            await message.answer(
                f"✅ <b>Баланс пополнен!</b>\n"
                f"💰 Добавлено: <b>{amount:.0f} ⭐</b>\n"
                f"🏦 Текущий баланс: <b>{user.balance:.0f} ⭐</b>"
            )
        
        db.close()
        
    except ValueError:
        await message.answer("❌ Неверная сумма!")
    except Exception as e:
        logger.error(f"Error adding balance: {e}")
        await message.answer("❌ Ошибка при пополнении баланса!")

def run_fastapi():
    """Run FastAPI server in a separate thread"""
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")

async def main():
    """Main function"""
    # Create database tables
    try:
        from init_db import init_database
        init_database()
    except Exception as e:
        logger.error(f"Database initialization error: {e}")
        # Fallback to old method
        create_tables()
    
    # Start FastAPI server in background thread
    fastapi_thread = Thread(target=run_fastapi, daemon=True)
    fastapi_thread.start()
    
    logger.info("Bot is starting...")
    
    # Start bot polling
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())