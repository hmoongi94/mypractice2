from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        print("입력된 이름:", name)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)