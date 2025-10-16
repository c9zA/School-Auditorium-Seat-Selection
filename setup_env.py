#!/usr/bin/env python3
"""
Setup script for creating .env file from template
"""

import os
import shutil

def setup_env():
    """Copy .env.example to .env if it doesn't exist"""
    
    if os.path.exists('.env'):
        print("✅ .env file already exists!")
        return
    
    if not os.path.exists('.env.example'):
        print("❌ .env.example not found!")
        return
    
    # Copy template to .env
    shutil.copy('.env.example', '.env')
    print("✅ Created .env file from template")
    print("")
    print("📝 Please edit .env file with your actual database credentials:")
    print("   - For local development: use localhost MySQL")
    print("   - For production: use your cloud database credentials")
    print("")
    print("🔒 Remember: Never commit .env file to Git!")

if __name__ == "__main__":
    setup_env()