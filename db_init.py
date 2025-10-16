import os
import pymysql
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def init_database():
    """Initialize database with required tables and sample data"""
    try:
        conn = pymysql.connect(
            host=os.environ.get('DATABASE_HOST', 'localhost'),
            port=int(os.environ.get('DATABASE_PORT', 3306)),
            user=os.environ.get('DATABASE_USER', 'root'),
            password=os.environ.get('DATABASE_PASSWORD', 'root'),
            database=os.environ.get('DATABASE_NAME', 'film'),
            charset="utf8"
        )
        
        cursor = conn.cursor()
        
        # Create user table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) NOT NULL UNIQUE,
                password VARCHAR(50) NOT NULL
            ) CHARACTER SET utf8 COLLATE utf8_general_ci
        """)
        
        # Create seat table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS seat (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) NOT NULL,
                row_num INT NOT NULL,
                column_num INT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                INDEX idx_username (username),
                INDEX idx_position (row_num, column_num)
            ) CHARACTER SET utf8 COLLATE utf8_general_ci
        """)
        
        # Insert sample users
        sample_users = [
            ('admin', 'admin'),
            ('user1', 'password1'),
            ('user2', 'password2'),
            ('test', 'test')
        ]
        
        for username, password in sample_users:
            try:
                cursor.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (username, password))
            except pymysql.IntegrityError:
                # User already exists, skip
                pass
        
        conn.commit()
        print("Database initialized successfully!")
        print("Sample users created:")
        print("- admin/admin")
        print("- user1/password1") 
        print("- user2/password2")
        print("- test/test")
        
    except Exception as e:
        print(f"Error initializing database: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    init_database()