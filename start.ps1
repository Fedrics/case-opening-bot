# PowerShell script to start the bot
Set-Location "C:\Users\komp\Desktop\case_opening_bot"

Write-Host "Starting Case Opening Bot..." -ForegroundColor Green
Write-Host "Press Ctrl+C to stop the bot" -ForegroundColor Yellow

try {
    python bot.py
} catch {
    Write-Host "Error starting bot: $_" -ForegroundColor Red
    Read-Host "Press Enter to exit"
}