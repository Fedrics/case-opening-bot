# 🎁 Case Opening Telegram Bot

[![Python](https://img.shields.io/badge/python-v3.11+-blue.svg)](https://www.python.org/downloads/)
[![Telegram Bot API](https://img.shields.io/badge/Telegram%20Bot%20API-Latest-blue)](https://core.telegram.org/bots/api)
[![Railway](https://img.shields.io/badge/Deployed%20on-Railway-purple)](https://railway.app)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **Modern Telegram bot for opening cases with real prizes! WebApp integration, 2025 actual gifts, and balanced economics.**

## ✨ Features

- 🎁 **4 case types** with real prizes from games to tech
- 🌐 **Modern web interface** via Telegram WebApp  
- ⭐ **Telegram Stars payments** - official currency
- 🎮 **2025 actual prizes** - Steam games, consoles, hardware
- 📊 **Fair system** with transparent probabilities
- ✨ **Premium UI/UX** with animations and effects

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/Fedrics/case-opening-bot.git
cd case-opening-bot

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp .env.example .env
# Edit .env with your bot token and settings

# Run the bot
python bot.py
# Or use start.bat on Windows
```

## 🎁 Available Cases Telegram Bot 🎁

Современный Telegram бот для открытия кейсов с реальными призами! Интеграция с веб-приложением, актуальные подарки 2025 года и сбалансированная экономика.

## ✨ Особенности

- 🎁 **4 типа кейсов** с реальными призами от игр до техники
- 🌐 **Современный веб-интерфейс** через Telegram WebApp
- ⭐ **Платежи через Telegram Stars** - официальная валюта
- � **Актуальные призы 2025** - Steam игры, консоли, техника
- 📊 **Честная система** с прозрачными вероятностями
- � **Premium UI/UX** с анимациями и эффектами

## 🎁 Доступные кейсы

### 🌟 Стартовый кейс (50⭐)
- **Steam игры:** Stardew Valley, Cyberpunk 2077, Elden Ring
- **Подарки:** Google Play, iTunes, Nintendo eShop
- **Максимальный приз:** Steam Deck 256GB (~€420)

### 💎 Премиум кейс (150⭐)  
- **AAA игры:** EA SPORTS FC 26, Battlefield 6, Forza Horizon 5
- **Премиум:** Netflix, Spotify, Adobe Creative Suite
- **Максимальный приз:** PlayStation 5 Slim (~€500)

### 🎮 Gaming кейс (300⭐)
- **Новинки 2025:** Path of Exile 2, Silent Hill f, Tokyo Xtreme Racer
- **Gaming оборудование:** Gaming Chair, RTX видеокарты
- **Максимальный приз:** MacBook Pro M3 (~€2000)

### 🚀 Мега кейс (500⭐)
- **Premium техника:** Valve Index VR, Custom Gaming PC RTX 4080
- **Эксклюзив:** Tesla аксессуары, Luxury Watch
- **Максимальный приз:** Dream Gaming Setup (~€5000)

## 🚀 Быстрый запуск

### Railway Deployment (Рекомендуется)

1. **Fork this repository**
2. **Deploy on Railway:**
   - Зайдите на [railway.app](https://railway.app)
   - "Deploy from GitHub" → выберите форк
   - Добавьте переменные окружения (см. ниже)

3. **Переменные окружения:**
```env
BOT_TOKEN=your_bot_token_here
WEB_APP_URL=https://your-railway-domain.up.railway.app  
ADMIN_ID=your_telegram_id
SECRET_KEY=change-this-secret-key
```

4. **Готово!** Бот автоматически запустится с PostgreSQL

### Локальный запуск

```bash
# Клонирование
git clone https://github.com/YOUR_USERNAME/case-opening-bot.git
cd case-opening-bot

# Установка зависимостей  
pip install -r requirements.txt

# Настройка .env файла
cp .env.example .env
# Отредактируйте .env с вашими данными

# Запуск
python bot.py
```

## 🎯 Архитектура

### Backend
- **FastAPI** - современный веб-фреймворк
- **SQLAlchemy** - ORM для работы с БД
- **Aiogram 3** - Telegram Bot API
- **PostgreSQL** - продукционная БД

### Frontend  
- **Telegram WebApp** - нативная интеграция
- **Responsive Design** - адаптивный UI
- **CSS3 Animations** - плавные анимации призов
- **JavaScript ES6+** - современный JS

### DevOps
- **Docker** - контейнеризация
- **Railway** - cloud deployment
- **GitHub Actions** - CI/CD ready
- **Health Checks** - мониторинг

## 💰 Экономическая модель

### Сбалансированные награды
- **Максимум:** 10x от стоимости кейса
- **Средний возврат:** 60-80% 
- **Легендарные призы:** 1-5% шанс

### Честная система
- **Provably Fair RNG** - проверяемая случайность
- **Прозрачные вероятности** - открытые шансы
- **Без накрутки** - реальные цены призов

## � Технические детали

### База данных
```sql
Users (id, telegram_id, balance, stats...)
CaseOpenings (id, user_id, case_type, reward...)  
Transactions (id, user_id, type, amount...)
PaymentInvoices (id, user_id, status...)
```

### API Endpoints
- `GET /` - Веб-приложение кейсов
- `POST /api/open_case` - Открытие кейса
- `GET /api/user_stats` - Статистика пользователя
- `GET /health` - Health check для Railway

### Bot Commands
- `/start` - Главное меню
- `/add_balance <amount>` - Пополнение (админ)
- `💰 Пополнить баланс` - Telegram Stars оплата
- `📊 Статистика` - Личная статистика

## 🔧 Настройка для продакшена

### Безопасность
```python
# Обязательно измените
SECRET_KEY=your-super-secret-key-here
DATABASE_URL=postgresql://secure_connection
```

### Мониторинг
- Railway предоставляет встроенную аналитику
- Логирование через Python logging
- Health checks на `/health`

### Масштабирование  
- Автоматическое масштабирование Railway
- PostgreSQL для высокой нагрузки
- Кэширование статических файлов

## 🎨 Кастомизация

### Добавление новых кейсов
```python
# config.py
"new_case": {
    "name": "🆕 Новый кейс", 
    "price": 100,
    "rewards": {
        "legendary": {
            "probability": 1,
            "items": [{"name": "Приз", "value": 1000}]
        }
    }
}
```

### Кастом UI/UX
- Редактируйте `templates/index.html`
- CSS переменные для цветов кейсов
- Анимации наград настраиваются

## 📈 Roadmap

- [ ] **CryptoBot** интеграция (USDT, TON, BTC)
- [ ] **Многопользовательские турниры** 
- [ ] **NFT призы** через TON blockchain
- [ ] **Реферальная система**
- [ ] **Админ панель** для управления
- [ ] **Многоязычность** (EN, RU, ES)

## 🤝 Contributing

1. Fork проект
2. Создайте feature branch (`git checkout -b feature/amazing-feature`)
3. Commit изменения (`git commit -m 'Add amazing feature'`)
4. Push в branch (`git push origin feature/amazing-feature`)  
5. Откройте Pull Request

## 📄 License

Распространяется под MIT License. См. `LICENSE` для подробностей.

## 🆘 Поддержка

- 🐛 **Issues:** [GitHub Issues](https://github.com/YOUR_USERNAME/case-opening-bot/issues)
- 💬 **Telegram:** [@your_support_bot](https://t.me/your_support_bot)
- 📧 **Email:** support@yourproject.com

---

<div align="center">

**[🚀 Deploy on Railway](https://railway.app)** | **[⭐ Star on GitHub](https://github.com/YOUR_USERNAME/case-opening-bot)** | **[📚 Documentation](./DEPLOYMENT.md)**

Сделано с ❤️ для Telegram сообщества

</div>