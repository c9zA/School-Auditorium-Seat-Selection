#!/bin/bash

# Quick Start Script for Local Development

echo "🚀 Starting School Auditorium Seat Selection System"
echo "=================================================="

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "❌ Python is not installed. Please install Python 3.x first."
    exit 1
fi

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    echo "❌ pip is not installed. Please install pip first."
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements-prod.txt

# Check if .env file exists
if [ ! -f .env ]; then
    echo "⚙️  Creating .env file from template..."
    cp .env.example .env
    echo "📝 Please edit .env file with your database credentials"
    echo "   Database should be running on localhost:3306"
    echo "   Default database name: film"
fi

# Initialize database (optional)
read -p "🗄️  Do you want to initialize the database? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🔧 Initializing database..."
    python db_init.py
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "To start the application:"
echo "  python app.py"
echo ""
echo "Then open your browser to: http://localhost:5000"
echo ""
echo "Default login credentials:"
echo "  Username: admin"
echo "  Password: admin"