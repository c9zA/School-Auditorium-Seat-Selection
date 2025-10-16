import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def init_postgres_database():
    """Initialize PostgreSQL database with required tables and sample data"""
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            host=os.environ.get('DATABASE_HOST', 'localhost'),
            port=int(os.environ.get('DATABASE_PORT', 5432)),
            user=os.environ.get('DATABASE_USER', 'postgres'),
            password=os.environ.get('DATABASE_PASSWORD', 'password'),
            database=os.environ.get('DATABASE_NAME', 'film')
        )
        
        cursor = conn.cursor()
        
        # Create users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) NOT NULL UNIQUE,
                password VARCHAR(50) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Create seats table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS seats (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) NOT NULL,
                row_num INTEGER NOT NULL,
                column_num INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Create indexes for better performance
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_seats_username ON seats(username)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_seats_position ON seats(row_num, column_num)")
        
        # Insert sample users
        sample_users = [
            ('admin', 'admin'),
            ('user1', 'password1'),
            ('user2', 'password2'),
            ('test', 'test')
        ]
        
        for username, password in sample_users:
            try:
                cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", 
                             (username, password))
            except psycopg2.IntegrityError:
                # User already exists, skip
                pass
        
        conn.commit()
        print("✅ PostgreSQL database initialized successfully!")
        print("📊 Sample users created:")
        print("   - admin/admin")
        print("   - user1/password1") 
        print("   - user2/password2")
        print("   - test/test")
        
    except Exception as e:
        print(f"❌ Error initializing database: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    init_postgres_database()