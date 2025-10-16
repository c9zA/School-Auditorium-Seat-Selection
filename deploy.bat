@echo off
echo 🚀 Deploying School Auditorium Seat Selection System
echo ==================================================
echo.

echo Choose deployment option:
echo 1. Render.com with PostgreSQL (Free)
echo 2. SQLite version (Works everywhere)
echo 3. Show all free options
echo.

set /p choice="Enter your choice (1-3): "

if "%choice%"=="1" (
    echo 📋 Setting up for Render.com with PostgreSQL...
    copy requirements-postgres.txt requirements.txt
    copy app_postgres.py app.py
    echo ✅ Files prepared for Render.com deployment
    echo.
    echo Next steps:
    echo 1. Go to render.com
    echo 2. Create PostgreSQL database (FREE)
    echo 3. Create Web Service from GitHub
    echo 4. Use: gunicorn app:app
) else if "%choice%"=="2" (
    echo 📋 Setting up SQLite version...
    copy requirements-sqlite.txt requirements.txt
    copy app_sqlite.py app.py
    copy Procfile-sqlite Procfile
    echo ✅ Files prepared for SQLite deployment
    echo.
    echo This works on:
    echo - Render.com
    echo - Vercel
    echo - Railway
    echo - Any hosting platform
) else if "%choice%"=="3" (
    echo 📖 Opening free deployment guide...
    start FREE_DEPLOYMENT.md
) else (
    echo ❌ Invalid choice
)

echo.
echo 📝 Don't forget to:
echo 1. git add .
echo 2. git commit -m "Setup for deployment"
echo 3. git push origin main
pause