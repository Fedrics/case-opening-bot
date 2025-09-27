import os
from dotenv import load_dotenv

load_dotenv()

# Bot Configuration
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEB_APP_URL = os.getenv("WEB_APP_URL", "http://localhost:8000")
CRYPTOBOT_TOKEN = os.getenv("CRYPTOBOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./case_bot.db")
SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret-key")
# Use BigInteger compatible value
ADMIN_ID = int(os.getenv("ADMIN_ID", "123456789"))

# Case Configuration
CASES = {
    "starter": {
        "name": "🌟 Стартовый кейс",
        "price": 50,
        "rewards": {
            "common": {
                "probability": 40,
                "items": [
                    {"name": "Steam: Stardew Valley", "value": 14, "image": "games.png"},
                    {"name": "Steam: Left 4 Dead 2", "value": 10, "image": "games.png"},
                    {"name": "Mobile: Clash Royale Gems", "value": 5, "image": "mobile.png"},
                    {"name": "100 Telegram Stars", "value": 20, "image": "stars.png"}
                ]
            },
            "uncommon": {
                "probability": 35,
                "items": [
                    {"name": "Steam: The Witcher 3", "value": 30, "image": "games.png"},
                    {"name": "Steam: Cyberpunk 2077", "value": 35, "image": "games.png"},
                    {"name": "200 Telegram Stars", "value": 40, "image": "stars.png"},
                    {"name": "iTunes Gift Card $10", "value": 10, "image": "gift.png"}
                ]
            },
            "rare": {
                "probability": 20,
                "items": [
                    {"name": "Steam: Elden Ring", "value": 60, "image": "games.png"},
                    {"name": "Nintendo eShop $20", "value": 20, "image": "nintendo.png"},
                    {"name": "400 Telegram Stars", "value": 80, "image": "stars.png"},
                    {"name": "Google Play $15", "value": 15, "image": "mobile.png"}
                ]
            },
            "epic": {
                "probability": 4,
                "items": [
                    {"name": "Steam: Black Myth Wukong", "value": 120, "image": "games.png"},
                    {"name": "PlayStation Store $25", "value": 25, "image": "playstation.png"},
                    {"name": "600 Telegram Stars", "value": 120, "image": "stars.png"}
                ]
            },
            "legendary": {
                "probability": 1,
                "items": [
                    {"name": "Steam Deck (256GB)", "value": 420, "image": "hardware.png"},
                    {"name": "1000 Telegram Stars", "value": 200, "image": "stars.png"},
                    {"name": "Xbox Game Pass Ultimate 3M", "value": 45, "image": "xbox.png"}
                ]
            }
        }
    },
    "premium": {
        "name": "💎 Премиум кейс",
        "price": 150,
        "rewards": {
            "common": {
                "probability": 35,
                "items": [
                    {"name": "Steam: Hades II", "value": 29, "image": "games.png"},
                    {"name": "Steam: Grounded", "value": 40, "image": "games.png"},
                    {"name": "Spotify Premium 1M", "value": 12, "image": "music.png"},
                    {"name": "300 Telegram Stars", "value": 60, "image": "stars.png"}
                ]
            },
            "uncommon": {
                "probability": 30,
                "items": [
                    {"name": "Steam: Sekiro GOTY", "value": 60, "image": "games.png"},
                    {"name": "Steam: Forza Horizon 5", "value": 60, "image": "games.png"},
                    {"name": "Netflix Premium 1M", "value": 18, "image": "streaming.png"},
                    {"name": "500 Telegram Stars", "value": 100, "image": "stars.png"}
                ]
            },
            "rare": {
                "probability": 25,
                "items": [
                    {"name": "Steam: EA SPORTS FC 26", "value": 140, "image": "games.png"},
                    {"name": "Steam: Battlefield 6", "value": 140, "image": "games.png"},
                    {"name": "Adobe Creative Suite 1M", "value": 60, "image": "software.png"},
                    {"name": "800 Telegram Stars", "value": 160, "image": "stars.png"}
                ]
            },
            "epic": {
                "probability": 8,
                "items": [
                    {"name": "iPhone 15 Pro Case", "value": 120, "image": "accessories.png"},
                    {"name": "AirPods Pro", "value": 250, "image": "hardware.png"},
                    {"name": "1200 Telegram Stars", "value": 240, "image": "stars.png"}
                ]
            },
            "legendary": {
                "probability": 2,
                "items": [
                    {"name": "PlayStation 5 Slim", "value": 500, "image": "hardware.png"},
                    {"name": "RTX 4060 Graphics Card", "value": 320, "image": "hardware.png"},
                    {"name": "2000 Telegram Stars", "value": 400, "image": "stars.png"}
                ]
            }
        }
    },
    "gaming": {
        "name": "🎮 Gaming кейс",
        "price": 300,
        "rewards": {
            "common": {
                "probability": 30,
                "items": [
                    {"name": "Steam: Path of Exile 2", "value": 55, "image": "games.png"},
                    {"name": "Steam: No Man's Sky", "value": 120, "image": "games.png"},
                    {"name": "Discord Nitro 1M", "value": 10, "image": "software.png"},
                    {"name": "600 Telegram Stars", "value": 120, "image": "stars.png"}
                ]
            },
            "uncommon": {
                "probability": 30,
                "items": [
                    {"name": "Steam: Silent Hill f", "value": 160, "image": "games.png"},
                    {"name": "Steam: Tokyo Xtreme Racer", "value": 98, "image": "games.png"},
                    {"name": "Telegram Premium 3M", "value": 15, "image": "telegram.png"},
                    {"name": "900 Telegram Stars", "value": 180, "image": "stars.png"}
                ]
            },
            "rare": {
                "probability": 25,
                "items": [
                    {"name": "Gaming Chair RGB", "value": 250, "image": "furniture.png"},
                    {"name": "Mechanical Keyboard", "value": 150, "image": "hardware.png"},
                    {"name": "1500 Telegram Stars", "value": 300, "image": "stars.png"},
                    {"name": "Xbox Series S", "value": 300, "image": "hardware.png"}
                ]
            },
            "epic": {
                "probability": 12,
                "items": [
                    {"name": "Gaming Laptop RTX 4050", "value": 800, "image": "hardware.png"},
                    {"name": "Custom Gaming PC", "value": 1200, "image": "hardware.png"},
                    {"name": "2500 Telegram Stars", "value": 500, "image": "stars.png"}
                ]
            },
            "legendary": {
                "probability": 3,
                "items": [
                    {"name": "RTX 4070 Graphics Card", "value": 600, "image": "hardware.png"},
                    {"name": "iPhone 15 Pro Max", "value": 1200, "image": "hardware.png"},
                    {"name": "MacBook Pro M3", "value": 2000, "image": "hardware.png"}
                ]
            }
        }
    },
    "mega": {
        "name": "🚀 Мега кейс",
        "price": 500,
        "rewards": {
            "common": {
                "probability": 20,
                "items": [
                    {"name": "Steam: Valve Index VR Kit", "value": 1079, "image": "hardware.png"},
                    {"name": "Premium Gaming Setup", "value": 800, "image": "hardware.png"},
                    {"name": "1000 Telegram Stars", "value": 200, "image": "stars.png"},
                    {"name": "Nintendo Switch OLED", "value": 350, "image": "hardware.png"}
                ]
            },
            "uncommon": {
                "probability": 25,
                "items": [
                    {"name": "High-End Smartphone", "value": 900, "image": "hardware.png"},
                    {"name": "Professional Monitor 4K", "value": 600, "image": "hardware.png"},
                    {"name": "2000 Telegram Stars", "value": 400, "image": "stars.png"},
                    {"name": "Gaming Workstation", "value": 1500, "image": "hardware.png"}
                ]
            },
            "rare": {
                "probability": 35,
                "items": [
                    {"name": "Custom Built PC RTX 4080", "value": 2000, "image": "hardware.png"},
                    {"name": "Professional Camera Kit", "value": 1200, "image": "hardware.png"},
                    {"name": "3500 Telegram Stars", "value": 700, "image": "stars.png"},
                    {"name": "Electric Scooter Premium", "value": 800, "image": "transport.png"}
                ]
            },
            "epic": {
                "probability": 15,
                "items": [
                    {"name": "Tesla Model 3 Accessories", "value": 2000, "image": "transport.png"},
                    {"name": "MacBook Pro Max 16", "value": 3500, "image": "hardware.png"},
                    {"name": "5000 Telegram Stars", "value": 1000, "image": "stars.png"}
                ]
            },
            "legendary": {
                "probability": 5,
                "items": [
                    {"name": "Dream Gaming Setup Complete", "value": 5000, "image": "hardware.png"},
                    {"name": "Luxury Watch", "value": 3000, "image": "luxury.png"},
                    {"name": "10000 Telegram Stars", "value": 2000, "image": "stars.png"}
                ]
            }
        }
    }
}

# Rarity Colors
RARITY_COLORS = {
    "common": "#808080",      # Gray
    "uncommon": "#00ff00",    # Green
    "rare": "#0080ff",        # Blue
    "epic": "#8000ff",        # Purple
    "legendary": "#ff8000",   # Orange
}

# Payment Configuration
CRYPTOBOT_API_URL = "https://pay.crypt.bot/api"
PAYMENT_METHODS = ["USDT", "TON", "BTC", "ETH"]

# Test donation for admin
TEST_DONATION = {
    "amount": 1,
    "enabled_for": [ADMIN_ID]
}