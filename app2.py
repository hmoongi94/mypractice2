from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MariaDB 연결 정보
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'mariadb',
    'database': 'pythonpractice'
}

# 데이터베이스 연결 함수
def connect_to_database():
    return mysql.connector.connect(**db_config)

# 데이터베이스에 값을 삽입하는 함수
def insert_data(name):
    try:
        conn = connect_to_database()
        cursor = conn.cursor()
        sql = "INSERT INTO users (name) VALUES (%s)"
        cursor.execute(sql, (name,))
        conn.commit()
        return True
    except Exception as e:
        print("Error inserting data:", e)
        return False
    finally:
        if conn:
            conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        if insert_data(name):
            print("입력된 이름을 데이터베이스에 성공적으로 추가했습니다.")
        else:
            print("데이터베이스에 입력된 이름을 추가하는 데 문제가 발생했습니다.")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)