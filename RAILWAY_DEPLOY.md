# 🚄 Railway Deployment Guide

## Quick Deploy to Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/github-repo/Fedrics/case-opening-bot)

## Manual Deployment Steps

### 1. Connect GitHub Repository

1. Visit [Railway](https://railway.app)
2. Sign up with GitHub
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose `Fedrics/case-opening-bot`

### 2. Configure Environment Variables

In Railway dashboard, add these variables:

```env
BOT_TOKEN=your_bot_token_from_botfather
WEB_APP_URL=https://your-railway-app.railway.app
ADMIN_ID=your_telegram_user_id
SECRET_KEY=your_random_secret_key_32_chars
DATABASE_URL=postgresql://... (automatically provided by Railway)
```

### 3. Add PostgreSQL Database

1. In Railway dashboard, click "Add Service"
2. Select "PostgreSQL"
3. Railway will automatically set `DATABASE_URL`

### 4. Domain Setup

1. Go to your Railway service settings
2. Click "Generate Domain" or add custom domain
3. Update `WEB_APP_URL` with your Railway domain

### 5. Deploy

Railway will automatically deploy when you:
- Push changes to GitHub
- Update environment variables
- Redeploy manually from dashboard

## Environment Variables Explained

| Variable | Description | Example |
|----------|-------------|---------|
| `BOT_TOKEN` | Telegram bot token from @BotFather | `1234567890:ABC...` |
| `WEB_APP_URL` | Railway app URL | `https://mybot.railway.app` |
| `ADMIN_ID` | Your Telegram user ID | `123456789` |
| `SECRET_KEY` | Random secret for security | `super-secret-key-32-chars-long` |
| `DATABASE_URL` | PostgreSQL connection (auto) | `postgresql://...` |

## Getting Your Values

### Bot Token
1. Message @BotFather on Telegram
2. Create new bot: `/newbot`
3. Copy the token

### Your Telegram ID
1. Message @userinfobot
2. Copy the ID number

### Secret Key
Generate random 32-character string:
```bash
python -c "import secrets; print(secrets.token_hex(16))"
```

## Troubleshooting

### Bot doesn't respond
- Check `BOT_TOKEN` is correct
- Verify Railway service is running
- Check Railway logs for errors

### WebApp doesn't open
- Verify `WEB_APP_URL` matches Railway domain
- Check if domain is accessible
- Ensure HTTPS (Railway provides this)

### Database errors
- Railway PostgreSQL should auto-connect
- Check `DATABASE_URL` is set
- View Railway database service logs

## Monitoring

Railway provides:
- **Metrics**: CPU, memory, network usage
- **Logs**: Real-time application logs  
- **Analytics**: Request statistics
- **Alerts**: Notification setup

Access these in your Railway dashboard.

## Cost

Railway offers:
- **Free Tier**: $5 credit per month
- **Pro Plan**: Pay for usage beyond free tier
- **Database**: ~$5/month for PostgreSQL

Your bot should run comfortably within free tier for moderate usage.

## Scaling

Railway automatically handles:
- HTTPS certificates
- Load balancing  
- Auto-scaling
- Health monitoring
- Zero-downtime deployments

Perfect for production Telegram bots!

---

**Need help?** [Open an issue](https://github.com/Fedrics/case-opening-bot/issues) on GitHub.