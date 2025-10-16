@echo off
echo 🚀 Starting School Auditorium Seat Selection System
echo ==================================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.x first.
    pause
    exit /b 1
)

REM Install dependencies
echo 📦 Installing dependencies...
pip install -r requirements-prod.txt

REM Check if .env file exists
if not exist .env (
    echo ⚙️  Creating .env file from template...
    copy .env.example .env
    echo 📝 Please edit .env file with your database credentials
    echo    Database should be running on localhost:3306
    echo    Default database name: film
)

REM Initialize database (optional)
set /p choice="🗄️  Do you want to initialize the database? (y/N): "
if /i "%choice%"=="y" (
    echo 🔧 Initializing database...
    python db_init.py
)

echo.
echo ✅ Setup complete!
echo.
echo To start the application:
echo   python app.py
echo.
echo Then open your browser to: http://localhost:5000
echo.
echo Default login credentials:
echo   Username: admin
echo   Password: admin
pause