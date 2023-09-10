from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setcookie', methods=['POST'])
def setcookie():
    name = request.form['name']
    email = request.form['email']

    resp = make_response(redirect(url_for('greet')))
    resp.set_cookie('name', name)
    resp.set_cookie('email', email)

    return resp

@app.route('/greet')
def greet():
    name = request.cookies.get('name', '')
    if not name:
        return redirect(url_for('index'))

    return render_template('greet.html', name=name)

@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for('index')))
    resp.delete_cookie('name')
    resp.delete_cookie('email')

    return resp

if __name__ == "__main__":
    app.run(debug=True)
