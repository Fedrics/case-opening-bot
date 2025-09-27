# Deployment Guide - Case Opening Bot

## 🚀 Развертывание на Railway

### 1. Подготовка GitHub репозитория

1. Создайте новый репозиторий на GitHub с именем `case-opening-bot`
2. Выгрузите код:
```bash
git remote add origin https://github.com/YOUR_USERNAME/case-opening-bot.git
git branch -M main  
git push -u origin main
```

### 2. Развертывание на Railway

1. Зайдите на [railway.app](https://railway.app)
2. Нажмите "Start a New Project"
3. Выберите "Deploy from GitHub repo"
4. Выберите репозиторий `case-opening-bot`

### 3. Настройка переменных окружения

В Railway добавьте следующие переменные:

**Обязательные:**
```
BOT_TOKEN=8444654226:AAFNUurGO2xluz2G7PkoS_DpqOEO_Bvmpj4
WEB_APP_URL=https://your-railway-domain.up.railway.app
ADMIN_ID=6263683504
SECRET_KEY=super-secret-key-change-this-in-production
```

**Опциональные:**
```
CRYPTOBOT_TOKEN=your_cryptobot_token_here
DATABASE_URL=postgresql://postgres:password@db:5432/case_opening_bot
```

### 4. База данных

Railway автоматически предоставит PostgreSQL базу данных.
Переменная `DATABASE_URL` будет установлена автоматически.

### 5. Настройка Telegram WebApp

1. После развертывания получите URL вашего приложения
2. Обновите переменную `WEB_APP_URL` на Railway
3. Перезапустите сервис

## 🎁 Новые подарки и кейсы

### 🌟 Стартовый кейс (50⭐)
**Популярные игры:**
- Steam: Stardew Valley (€14)
- Steam: Left 4 Dead 2 (€10)
- Steam: The Witcher 3 (€30)
- Steam: Cyberpunk 2077 (€35)
- Steam: Elden Ring (€60)

**Подарки:**
- iTunes Gift Card $10
- Google Play $15
- Nintendo eShop $20
- 100-1000 Telegram Stars

### 💎 Премиум кейс (150⭐)
**AAA Игры:**
- Steam: Hades II (€29)
- Steam: Sekiro GOTY (€60)
- Steam: Forza Horizon 5 (€60)
- Steam: EA SPORTS FC 26 (€140)
- Steam: Battlefield 6 (€140)

**Премиум подарки:**
- Spotify Premium 1M
- Netflix Premium 1M
- Adobe Creative Suite 1M
- iPhone 15 Pro Case
- AirPods Pro (€250)
- PlayStation 5 Slim (€500)

### 🎮 Gaming кейс (300⭐)
**Новинки 2025:**
- Steam: Path of Exile 2 (€55)
- Steam: No Man's Sky (€120)
- Steam: Silent Hill f (€160)
- Steam: Tokyo Xtreme Racer (€98)

**Gaming оборудование:**
- Gaming Chair RGB (€250)
- Mechanical Keyboard (€150)
- Xbox Series S (€300)
- Gaming Laptop RTX 4050 (€800)
- Custom Gaming PC (€1200)

### 🚀 Мега кейс (500⭐)
**Премиум техника:**
- Steam: Valve Index VR Kit (€1079)
- Nintendo Switch OLED (€350)
- Professional Monitor 4K (€600)
- Custom Built PC RTX 4080 (€2000)
- MacBook Pro Max 16 (€3500)

**Эксклюзивные призы:**
- Tesla Model 3 Accessories (€2000)
- Dream Gaming Setup Complete (€5000)
- Luxury Watch (€3000)
- До 10,000 Telegram Stars

## 📊 Сбалансированная экономика

- **Максимальная прибыль:** 10x от стоимости кейса
- **Средний возврат:** 60-80% от стоимости кейса
- **Легендарные призы:** 1-5% шанс выпадения
- **Честная система:** Provably Fair RNG

## 🔧 Технические особенности

- **FastAPI** веб-приложение с современным UI
- **PostgreSQL** база данных
- **Telegram WebApp** интеграция
- **Telegram Stars** платежная система
- **Docker** контейнеризация
- **Railway** хостинг

## 🚀 Масштабирование

Приложение готово для:
- Тысячи одновременных пользователей
- Автоматическое масштабирование на Railway
- Мониторинг и логирование
- Backup и восстановление данных

## 📈 Аналитика

Railway предоставляет:
- Метрики использования ресурсов
- Логи приложения в реальном времени
- Мониторинг uptime
- Автоматические уведомления об ошибках

---

**Готово к запуску!** 🚀

После развертывания отправьте `/start` вашему боту и наслаждайтесь современной системой кейсов с реальными призами!