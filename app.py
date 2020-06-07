from app import app, render_template, request


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data', methods=['GET', 'POST'])
def get_data():
    title = "Add data"
    if request.method == 'GET':
        message = "Welcome, add data"
        return render_template('form.html', message=message, title=title)
    elif request.method == 'POST':
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


if __name__ == '__main__':
    app.run(debug=True)
