# Render.com Deployment Guide

## Step 1: Prepare Database

Since Render's free tier doesn't include databases, we'll use a free external MySQL database.

### Option A: PlanetScale (Recommended)
1. Go to [planetscale.com](https://planetscale.com)
2. Sign up with GitHub
3. Create a new database named `film-db`
4. Get connection details from the dashboard

### Option B: Aiven
1. Go to [aiven.io](https://aiven.io)
2. Sign up for free tier
3. Create a MySQL service
4. Note the connection details

## Step 2: Deploy to Render

1. **Go to Render.com**
   - Visit [render.com](https://render.com)
   - Sign up/login with GitHub

2. **Create Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository: `c9zA/School-Auditorium-Seat-Selection`
   - Choose the repository

3. **Configure Service**
   - **Name**: `seat-selection-app`
   - **Region**: Choose closest to you
   - **Branch**: `main`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements-prod.txt`
   - **Start Command**: `gunicorn app:app`

4. **Set Environment Variables**
   Click "Advanced" and add these environment variables:

   ```
   DATABASE_HOST=your_planetscale_host
   DATABASE_PORT=3306
   DATABASE_USER=your_planetscale_user
   DATABASE_PASSWORD=your_planetscale_password
   DATABASE_NAME=film-db
   SECRET_KEY=nkenNCEA^qki7RJ&18^zbxQoVZNZW&&g
   PYTHON_VERSION=3.9.16
   ```

5. **Deploy**
   - Click "Create Web Service"
   - Render will automatically build and deploy your app

## Step 3: Initialize Database

Once deployed, you need to initialize your database:

1. **Access Render Shell**
   - Go to your service dashboard
   - Click "Shell" tab
   - Run: `python db_init.py`

2. **Or use database client**
   - Connect to your external database
   - Import the `film.sql` file

## Step 4: Test Your Application

1. **Get your app URL**
   - Found in Render dashboard (like: `https://your-app-name.onrender.com`)

2. **Test login**
   - Username: `admin`
   - Password: `admin`

## Free Database Services

### PlanetScale Setup:
```bash
# Connection details format:
Host: aws.connect.psdb.cloud
Port: 3306
Database: film-db
Username: [provided by PlanetScale]
Password: [provided by PlanetScale]
```

### Aiven Setup:
```bash
# Connection details format:
Host: [provided by Aiven]
Port: 3306
Database: defaultdb
Username: avnadmin
Password: [provided by Aiven]
```

## Troubleshooting

### Build Failures:
- Check if `requirements-prod.txt` is in root directory
- Ensure Python version compatibility

### Database Connection Issues:
- Verify environment variables are set correctly
- Check if external database allows connections
- Test connection using database client first

### Application Not Starting:
- Check logs in Render dashboard
- Ensure `gunicorn` is in requirements.txt
- Verify `app.py` has correct Flask app variable

## Auto-Deploy

Render automatically redeploys when you push to your main branch on GitHub!

## Custom Domain (Optional)

On Render's free tier, you can add a custom domain if you have one.