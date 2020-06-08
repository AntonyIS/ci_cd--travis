from flask import render_template, request
from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data', methods=['GET', 'POST'])
def get_data():
    title = "Add data"
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if username == '' or email == '' or password == '' :
            message = "Fill all fields"
            return render_template('form.html', message=message, title=title)
        else:
            message = "Data received"
            data = {
                'username':username,
                'email':email,
                'password':password

            }
            return render_template('form.html',message=message,title=title,data =data)

    message = "Welcome, add data"
    return render_template('form.html', message=message, title=title)
