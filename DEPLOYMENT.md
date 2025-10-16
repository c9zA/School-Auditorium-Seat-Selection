# Deployment Guide

## Prerequisites

Before deploying, ensure you have:
1. A GitHub account
2. Your code pushed to a GitHub repository
3. A database hosting service (like Railway, PlanetScale, or AWS RDS)

## Step 1: Prepare Your Code

1. **Update your main.py** - I've created a production-ready version in `app.py` with:
   - Environment variable support
   - Secure database connections
   - SQL injection prevention
   - Production server configuration

2. **Use the production requirements**:
   ```bash
   cp requirements-prod.txt requirements.txt
   ```

## Step 2: Choose a Deployment Platform

### Option A: Railway (Recommended for beginners)

1. Go to [Railway.app](https://railway.app)
2. Connect your GitHub account
3. Create a new project from your GitHub repository
4. Add a MySQL database service
5. Set environment variables:
   - `DATABASE_HOST`: (Railway will provide this)
   - `DATABASE_USER`: (Railway will provide this)
   - `DATABASE_PASSWORD`: (Railway will provide this)
   - `DATABASE_NAME`: film
   - `PORT`: Railway sets this automatically

### Option B: Heroku

1. Install Heroku CLI
2. Login: `heroku login`
3. Create app: `heroku create your-app-name`
4. Add MySQL addon: `heroku addons:create cleardb:ignite`
5. Get database URL: `heroku config:get CLEARDB_DATABASE_URL`
6. Set environment variables:
   ```bash
   heroku config:set DATABASE_HOST=your_host
   heroku config:set DATABASE_USER=your_user
   heroku config:set DATABASE_PASSWORD=your_password
   heroku config:set DATABASE_NAME=film
   ```
7. Deploy: `git push heroku main`

### Option C: Render

1. Connect your GitHub repository at [Render.com](https://render.com)
2. Create a new Web Service
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `gunicorn app:app`
5. Add environment variables in the Render dashboard

## Step 3: Database Setup

### Import your database schema:

1. **For Railway/Render**: Use a database client to connect and import `film.sql`
2. **For Heroku**: Use the Heroku CLI:
   ```bash
   heroku run python
   # Then manually create tables or use a migration script
   ```

### Create a database initialization script:

```python
# db_init.py
import os
import pymysql

def init_database():
    conn = pymysql.connect(
        host=os.environ.get('DATABASE_HOST'),
        port=int(os.environ.get('DATABASE_PORT', 3306)),
        user=os.environ.get('DATABASE_USER'),
        password=os.environ.get('DATABASE_PASSWORD'),
        database=os.environ.get('DATABASE_NAME'),
        charset="utf8"
    )
    
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            password VARCHAR(50) NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS seat (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            row_num INT NOT NULL,
            column_num INT NOT NULL
        )
    """)
    
    # Insert sample user
    cursor.execute("INSERT IGNORE INTO user (username, password) VALUES ('admin', 'admin')")
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_database()
```

## Step 4: Environment Variables

Set these environment variables in your deployment platform:

```
DATABASE_HOST=your_database_host
DATABASE_PORT=3306
DATABASE_USER=your_database_user
DATABASE_PASSWORD=your_database_password
DATABASE_NAME=film
SECRET_KEY=your_secret_key
```

## Step 5: Testing

1. Deploy your application
2. Access the provided URL
3. Test login functionality
4. Test seat booking and cancellation

## Common Issues and Solutions

### Database Connection Issues
- Ensure your database allows external connections
- Verify environment variables are set correctly
- Check if your database service is running

### Static Files Not Loading
- Make sure your static files are in the `static/` directory
- Verify Flask is serving static files correctly

### Application Not Starting
- Check the logs in your deployment platform
- Ensure `gunicorn` is installed in requirements.txt
- Verify the Procfile is correct

## Security Considerations

1. Never commit database credentials to Git
2. Use environment variables for all sensitive data
3. Enable SSL for database connections in production
4. Consider implementing proper authentication (sessions, JWT)
5. Add input validation and CSRF protection

## Monitoring

- Set up logging in your application
- Monitor database performance
- Use health check endpoints
- Set up alerts for downtime

## Scaling

- Consider using connection pooling for database
- Implement caching for frequently accessed data
- Use CDN for static files
- Consider load balancing for high traffic