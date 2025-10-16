# Render.com Deployment Guide (PostgreSQL)

## Step 1: Prepare for PostgreSQL

Render.com offers **FREE PostgreSQL** database! This is much better than using external services.

## Step 2: Deploy to Render

1. **Go to Render.com**
   - Visit [render.com](https://render.com)
   - Sign up/login with GitHub

2. **Create PostgreSQL Database First**
   - Click "New +" → "PostgreSQL"
   - **Name**: `film-database`
   - **Database**: `film`
   - **User**: `film_user`
   - **Region**: Choose closest to you
   - **Plan**: Free
   - Click "Create Database"

3. **Create Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository: `c9zA/School-Auditorium-Seat-Selection`
   - Choose the repository

4. **Configure Service**
   - **Name**: `seat-selection-app`
   - **Region**: Same as your database
   - **Branch**: `main`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements-postgres.txt`
   - **Start Command**: `gunicorn app_postgres:app`

5. **Set Environment Variables**
   Click "Advanced" and add these environment variables:

   From your PostgreSQL database dashboard, copy the connection details:
   ```
   DATABASE_HOST=your_postgres_host_from_render
   DATABASE_PORT=5432
   DATABASE_USER=your_postgres_user_from_render
   DATABASE_PASSWORD=your_postgres_password_from_render
   DATABASE_NAME=film
   SECRET_KEY=nkenNCEA^qki7RJ&18^zbxQoVZNZW&&g
   PYTHON_VERSION=3.9.16
   ```

6. **Deploy**
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