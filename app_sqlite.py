import os
import sqlite3
from flask import Flask, render_template, request, g
import json

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'nkenNCEA^qki7RJ&18^zbxQoVZNZW&&g')

# Database configuration
DATABASE = os.path.join(app.instance_path, 'film.db')

def get_db():
    """Get database connection"""
    if 'db' not in g:
        # Ensure instance folder exists
        os.makedirs(app.instance_path, exist_ok=True)
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    """Close database connection"""
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    """Initialize database with tables and sample data"""
    db = get_db()
    
    # Create tables
    db.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    db.execute('''
        CREATE TABLE IF NOT EXISTS seats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            row_num INTEGER NOT NULL,
            column_num INTEGER NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create indexes
    db.execute('CREATE INDEX IF NOT EXISTS idx_seats_username ON seats(username)')
    db.execute('CREATE INDEX IF NOT EXISTS idx_seats_position ON seats(row_num, column_num)')
    
    # Insert sample users
    sample_users = [
        ('admin', 'admin'),
        ('user1', 'password1'),
        ('user2', 'password2'),
        ('test', 'test')
    ]
    
    for username, password in sample_users:
        try:
            db.execute('INSERT INTO users (username, password) VALUES (?, ?)', 
                      (username, password))
        except sqlite3.IntegrityError:
            # User already exists, skip
            pass
    
    db.commit()

@app.before_first_request
def initialize_database():
    """Initialize database before first request"""
    init_db()

@app.teardown_appcontext
def close_db_connection(exception):
    """Close database connection after request"""
    close_db(exception)

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userID = request.form.get('username')
        password = request.form.get('password')
        
        db = get_db()
        user = db.execute(
            'SELECT * FROM users WHERE username = ? AND password = ?', 
            (userID, password)
        ).fetchone()
        
        if user:
            # Initialize seat layout
            res = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                   [-1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1],
                   [-1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0],
                   [-1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
                   [-1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
                   [-1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1],
                   [-1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1],
                   [-1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1]]

            # Get current seat bookings
            seats = db.execute('SELECT * FROM seats').fetchall()
            
            for seat in seats:
                res[seat['row_num']][seat['column_num']] = 1
                if seat['username'] == userID:
                    res[seat['row_num']][seat['column_num']] = 2
                    
            return render_template('index.html', res=res, username=userID)
        else:
            return render_template('login.html', error="Invalid username or password")
    
    return render_template('login.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    userID = request.args.get("username")
    res = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0],
           [-1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
           [-1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
           [-1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1]]

    db = get_db()
    seats = db.execute('SELECT * FROM seats').fetchall()
    
    for seat in seats:
        res[seat['row_num']][seat['column_num']] = 1
        if seat['username'] == userID:
            res[seat['row_num']][seat['column_num']] = 2
            
    return render_template('index.html', res=res, username=userID)

@app.route('/book', methods=['POST'])
def book():
    username = request.form.get('username')
    row = request.form.get('row')
    column = request.form.get('column')
    
    db = get_db()
    db.execute('INSERT INTO seats(username, row_num, column_num) VALUES (?, ?, ?)', 
              (username, row, column))
    db.commit()
    
    return "ok"

@app.route('/cancel', methods=['POST'])
def cancel():
    username = request.form.get('username')
    row = request.form.get('row')
    column = request.form.get('column')
    
    db = get_db()
    db.execute('DELETE FROM seats WHERE username = ? AND row_num = ? AND column_num = ?', 
              (username, row, column))
    db.commit()
    
    return "ok"

@app.route('/get_detail', methods=['GET', 'POST'])
def get_detail():
    username = request.args.get("username")
    
    db = get_db()
    seats = db.execute('SELECT * FROM seats WHERE username = ?', (username,)).fetchall()
    
    seat_list = [dict(seat) for seat in seats]
    
    return render_template('detail.html', seat_list=seat_list, username=username)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)