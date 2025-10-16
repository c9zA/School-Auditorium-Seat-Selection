import os
from flask import Flask, render_template, request
import pymysql
import json

app = Flask(__name__)

# Database configuration
def get_db_connection():
    """Get database connection using environment variables for production"""
    return pymysql.connect(
        host=os.environ.get('DATABASE_HOST', '127.0.0.1'),
        port=int(os.environ.get('DATABASE_PORT', 3306)),
        user=os.environ.get('DATABASE_USER', 'root'),
        password=os.environ.get('DATABASE_PASSWORD', 'root'),
        database=os.environ.get('DATABASE_NAME', 'film'),
        charset="utf8"
    )

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userID = request.form.get('username')
        password = request.form.get('password')
        
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("select * from user where BINARY username = %s and password = %s", (userID, password))
        result = cursor.fetchall()
        user_num = len(result)
        
        center_data_list = [{"id": row[0],
                            "username": str(row[1]),
                            "password": str(row[2])} for row in result]
        
        conn.close()
        
        if user_num > 0:
            # Initialize seat layout
            row = 13
            col = 27
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
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("select * from seat")
            result = cursor.fetchall()
            
            seat_list = [{"id": row[0],
                         "username": str(row[1]),
                         "row_num": int(row[2]),
                         "column_num": int(row[3])} for row in result]
            
            for s in seat_list:
                res[s['row_num']][s['column_num']] = 1
                if s['username'] == userID:
                    res[s['row_num']][s['column_num']] = 2
                    
            conn.close()
            return render_template('index.html', res=res, username=userID)
        else:
            return render_template('login.html', error="Invalid username or password")
    
    return render_template('login.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    userID = request.args.get("username")
    row = 13
    col = 27
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

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("select * from seat")
    result = cursor.fetchall()
    
    seat_list = [{"id": row[0],
                 "username": str(row[1]),
                 "row_num": int(row[2]),
                 "column_num": int(row[3])} for row in result]
    
    for s in seat_list:
        res[s['row_num']][s['column_num']] = 1
        if s['username'] == userID:
            res[s['row_num']][s['column_num']] = 2
            
    conn.close()
    return render_template('index.html', res=res, username=userID)

@app.route('/book', methods=['POST'])
def book():
    username = request.form.get('username')
    row = request.form.get('row')
    column = request.form.get('column')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    sql = "insert into seat(username, row_num, column_num) values(%s, %s, %s)"
    cursor.execute(sql, (username, row, column))
    conn.commit()
    conn.close()
    
    return "ok"

@app.route('/cancel', methods=['POST'])
def cancel():
    username = request.form.get('username')
    row = request.form.get('row')
    column = request.form.get('column')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    sql = "delete from seat where BINARY username=%s and row_num=%s and column_num=%s"
    cursor.execute(sql, (username, row, column))
    conn.commit()
    conn.close()
    
    return "ok"

@app.route('/get_detail', methods=['GET', 'POST'])
def get_detail():
    username = request.args.get("username")
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("select * from seat where username=%s", (username,))
    result = cursor.fetchall()
    
    seat_list = [{"id": row[0],
                  "username": str(row[1]),
                  "row_num": int(row[2]),
                  "column_num": int(row[3])} for row in result]
    
    conn.close()
    return render_template('detail.html', seat_list=seat_list, username=username)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)