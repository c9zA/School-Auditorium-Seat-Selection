# 🆓 100% FREE Deployment Guide

## Option 1: Render.com (Recommended - Completely Free)

Render offers **FREE PostgreSQL database** + **FREE web hosting**!

### Step 1: Create FREE PostgreSQL Database
1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. Click "New +" → "PostgreSQL"
4. Settings:
   - **Name**: `film-database`
   - **Database**: `film`
   - **User**: `film_user` 
   - **Plan**: **Free** (important!)
   - Click "Create Database"

### Step 2: Deploy Web Service
1. Click "New +" → "Web Service"
2. Connect GitHub repo: `c9zA/School-Auditorium-Seat-Selection`
3. Settings:
   - **Name**: `seat-selection-app`
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements-postgres.txt`
   - **Start Command**: `gunicorn app_postgres:app`
   - **Plan**: **Free**

### Step 3: Environment Variables
Get database connection info from your PostgreSQL service and add:
```
DATABASE_HOST=your_render_postgres_host
DATABASE_PORT=5432
DATABASE_USER=your_render_postgres_user
DATABASE_PASSWORD=your_render_postgres_password
DATABASE_NAME=film
SECRET_KEY=nkenNCEA^qki7RJ&18^zbxQoVZNZW&&g
```

### Step 4: Initialize Database
After deployment, go to your web service → "Shell" tab and run:
```bash
python db_init_postgres.py
```

---

## Option 2: Railway.app (FREE with GitHub Student Pack)

If you're a student, Railway is free with GitHub Student Pack.

### Step 1: Get GitHub Student Pack
1. Go to [education.github.com](https://education.github.com)
2. Apply for GitHub Student Developer Pack
3. Get free Railway credits

### Step 2: Deploy to Railway
1. Go to [railway.app](https://railway.app) 
2. Login with GitHub
3. "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Add PostgreSQL database (free with student pack)

---

## Option 3: Vercel + Free Database

### Free Database Options:
1. **Supabase** (free PostgreSQL): [supabase.com](https://supabase.com)
2. **Neon** (free PostgreSQL): [neon.tech](https://neon.tech)
3. **Aiven** (free tier): [aiven.io](https://aiven.io)

### Deploy to Vercel:
1. Go to [vercel.com](https://vercel.com)
2. Connect GitHub repository
3. Use serverless functions for Flask

---

## Option 4: Fly.io (Free Tier)

1. Go to [fly.io](https://fly.io)
2. Free tier includes PostgreSQL
3. Deploy with: `flyctl deploy`

---

## Option 5: SQLite (No Database Service Needed)

For simplest deployment, I can convert your app to use SQLite (file-based database):

### Advantages:
- ✅ No external database needed
- ✅ Works on any hosting platform
- ✅ Perfect for small applications
- ✅ Completely free

### Would you like me to create SQLite version?

---

## 🎯 My Recommendation:

**Use Render.com** - it's the easiest and completely free:
- Free PostgreSQL database (750MB)
- Free web hosting
- Automatic deployments from GitHub
- No credit card required
- SSL certificates included

## Next Steps:

Choose your preferred option and I'll help you set it up! Which one interests you most?

1. **Render.com** (easiest, completely free)
2. **SQLite version** (simplest, works everywhere)
3. **Railway** (if you have student pack)
4. **Other option**