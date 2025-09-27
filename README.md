# Case Opening Telegram Bot

Telegram бот для открытия кейсов с подарками, интегрированный с веб-приложением.

## Особенности

- 🎁 Система кейсов с разными редкостями наград
- ⭐ Интеграция с Telegram Stars для платежей
- 🌐 Веб-приложение с современным интерфейсом
- 📊 Статистика игрока и история открытий
- 💰 Система балансов и транзакций
- 🔄 Сбалансированная система наград

## Структура проекта

```
case_opening_bot/
├── bot.py              # Telegram бот
├── main.py             # FastAPI веб-приложение
├── config.py           # Конфигурация кейсов и наград
├── database.py         # Модели базы данных
├── requirements.txt    # Зависимости Python
├── .env               # Переменные окружения
├── templates/         # HTML шаблоны
│   ├── index.html     # Главная страница веб-приложения
│   └── error.html     # Страница ошибок
└── static/           # Статические файлы
```

## Установка и запуск

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Настройте переменные окружения в файле `.env`:
```bash
BOT_TOKEN=your_bot_token_here
WEB_APP_URL=your_web_app_url_here
ADMIN_ID=your_telegram_id_here
DATABASE_URL=sqlite:///case_opening.db
```

3. Запустите бота:
```bash
python bot.py
```

## Типы кейсов

### 🥉 Bronze Case (50 ⭐)
- Common: 50% (10-25 ⭐)
- Uncommon: 30% (30-50 ⭐)
- Rare: 15% (60-100 ⭐)
- Epic: 4% (120-200 ⭐)
- Legendary: 1% (250-500 ⭐)

### 🥈 Silver Case (100 ⭐)
- Common: 45% (20-50 ⭐)
- Uncommon: 30% (60-100 ⭐)
- Rare: 20% (120-200 ⭐)
- Epic: 4% (250-400 ⭐)
- Legendary: 1% (500-1000 ⭐)

### 🥇 Gold Case (200 ⭐)
- Common: 40% (50-100 ⭐)
- Uncommon: 30% (120-200 ⭐)
- Rare: 25% (250-400 ⭐)
- Epic: 4% (500-800 ⭐)
- Legendary: 1% (1000-2000 ⭐)

### 💎 Diamond Case (500 ⭐)
- Common: 25% (100-250 ⭐)
- Uncommon: 30% (300-500 ⭐)
- Rare: 35% (600-1000 ⭐)
- Epic: 8% (1200-2000 ⭐)
- Legendary: 2% (2500-5000 ⭐)

## API Endpoints

### Веб-приложение
- `GET /` - Главная страница с интерфейсом кейсов
- `POST /api/open_case` - Открытие кейса
- `GET /api/user_stats` - Статистика пользователя
- `GET /api/recent_openings` - Последние открытия

### Telegram Bot
- `/start` - Запуск бота и главное меню
- `/add_balance <сумма>` - Добавить баланс (только админ)

## База данных

### Users
- Информация о пользователях
- Баланс и статистика

### CaseOpening
- История открытых кейсов
- Полученные награды

### Transaction
- История транзакций
- Платежи и пополнения

### PaymentInvoice
- Счета для оплаты
- Статусы платежей

## Безопасность

- Проверка подписи Telegram WebApp
- Валидация пользовательских данных
- Защита от дублирования транзакций
- Сбалансированная система наград

## Технологии

- **Backend**: FastAPI, SQLAlchemy, Aiogram 3
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite
- **Payments**: Telegram Stars
- **WebApp**: Telegram WebApp API

## Развертывание

Для production развертывания рекомендуется:

1. Использовать PostgreSQL вместо SQLite
2. Настроить HTTPS для веб-приложения
3. Использовать обратный прокси (nginx)
4. Настроить логирование и мониторинг
5. Добавить rate limiting

## Лицензия

MIT License