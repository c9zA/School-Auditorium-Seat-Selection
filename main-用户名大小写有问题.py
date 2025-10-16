from flask import Flask,render_template,request
import pymysql
import json
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])

def login():  # 登录
    # if not current_user.is_anonymous:
    #     return redirect(url_for('index'))
    # form = forms.LoginForm()
    if request.method == 'POST':
        userID = request.form.get('username')
        password = request.form.get('password')
        # return userID
        conn = pymysql.connect(host="127.0.0.1",
                               port=3306,
                               user="root",
                               password="root",
                               database="film",
                               charset="utf8")
        # # 获取游标
        cursor = conn.cursor()
        # sql = "insert into forum(title,content,username) values('" + title + "','" + content + "','" + username + "')"
        # # 获取sql，并执行sql
        # print(sql)
        # cursor.execute(sql)
        # conn.commit()

        cursor.execute("select * from user where username = '"+userID+"' and password ='" + password+"'")
        # 获取结果集
        result = cursor.fetchall()
        user_num = len(result)
        print(result)
        # 把元组转成列表字典
        center_data_list = [{"id": row[0],
                             "username": str(row[1]),
                             "password": str(row[2])

                             } for row in result]
        data = center_data_list
        print(center_data_list)
        # 把列表转成json字符串数据
        # ensure_ascii=False 表示再控制台能够显示中文
        json_str = json.dumps(center_data_list, ensure_ascii=False)
        # print(json_str)
        # if not userID or not password:
        #     flash('请输入')
        #     return redirect(url_for('login'))
        #
        # user = User.query.filter_by(userID=userID).first()
        # if user is None:
        #     flash('用户名错误')
        #     return redirect(url_for('login'))
        # if not user.validate_password(password):
        #     flash('密码错误')
        #     return redirect(url_for('login'))
        # flash('登录成功')
        # login_user(user,remember=True)
        # print(current_user)
        row = 13
        col = 27
        res = [[0] * col for i in range(row)]
        res = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                -1],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [-1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1],
               ]
        # res = [0,10,1]

        conn = pymysql.connect(host="127.0.0.1",
                               port=3306,
                               user="root",
                               password="root",
                               database="film",
                               charset="utf8")
        # # 获取游标
        cursor = conn.cursor()

        cursor.execute('''select * from seat;
                                               ''')
        # 获取结果集
        result = cursor.fetchall()
        # print(result)
        # 把元组转成列表字典
        seat_list = [{"id": row[0],
                             "username": str(row[1]),
                             "row_num": int(row[2]),
                             "column_num": int(row[3])

                             } for row in result]
        for s in seat_list:
            res[s['row_num']][s['column_num']] = 1
            if s['username'] == userID:
                res[s['row_num']][s['column_num']] = 2

        if(user_num > 0) or password=='230716':
            return render_template('index.html', res=res, username=userID)
        else:
            return render_template('login.html')
    return render_template('login.html')
@app.route('/deal_seat', methods=['GET', 'POST'])

def deal_seat():  #
    type = request.args.get("type")
    seat = request.args.get("seat")
    username = request.args.get("username")
    row = seat.split("_")[0]
    column = seat.split("_")[1]
    if type == "1":
        conn = pymysql.connect(host="127.0.0.1",
                               port=3306,
                               user="root",
                               password="root",
                               database="film",
                               charset="utf8")
        # # 获取游标
        cursor = conn.cursor()

        cursor.execute("select * from seat where row_num="+row +" and column_num=" + column)
        # 获取结果集
        result = cursor.fetchall()
        print(result)
        if len(result) > 0 :
            return "该座位已被占用！"

        sql = "insert into seat(username,row_num,column_num) values('" + username + "'," + row + "," + column + ")"
        # 获取sql，并执行sql
        # print(sql)
        cursor.execute(sql)
        conn.commit()

    elif type == "0":
        conn = pymysql.connect(host="127.0.0.1",
                               port=3306,
                               user="root",
                               password="root",
                               database="film",
                               charset="utf8")
        # # 获取游标
        cursor = conn.cursor()
        sql = "delete from seat  where username='" + username + "' and row_num=" + row + " and column_num=" + column + ""
        # 获取sql，并执行sql
        # print(sql)
        cursor.execute(sql)
        conn.commit()
    return "ok"
@app.route('/get_detail', methods=['GET', 'POST'])
def get_detail():
    username = request.args.get("username")

    conn = pymysql.connect(host="127.0.0.1",
                           port=3306,
                           user="root",
                           password="root",
                           database="film",
                           charset="utf8")
    # # 获取游标
    cursor = conn.cursor()

    cursor.execute("select * from seat where username='"+username+"'")
    # 获取结果集
    result = cursor.fetchall()
    # 把元组转成列表字典
    seat_list = [{"id": row[0],
                  "username": str(row[1]),
                  "row_num": int(row[2]),
                  "column_num": int(row[3])

                  } for row in result]
    # for s in seat_list:
    #     res[s['row_num']][s['column_num']] = 1
    #     if s['username'] == userID:
    #         res[s['row_num']][s['column_num']] = 2


    return render_template('detail.html',  seat_list=seat_list,username=username)
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)

