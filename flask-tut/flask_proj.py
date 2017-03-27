from flask import Flask, render_template, flash, request, redirect
from forms import LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask("flask_app")
app.config.from_object('config')
db = SQLAlchemy(app)

db.create_all()

admin_user={
    'username' : 'admin',
    'password' : 'pass'
}

@app.route('/')
def main():
    return "You logged in"

@app.route('/start')
def start():
    title = 'my title'
    user = {'nickname': 'Vovan'}
    return render_template(
                          'index.html',
                           title=title,
                           user=user)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.is_submitted():
        print "submitted"
    if form.validate():
        print "valid"

    print(form.errors)
    if form.validate_on_submit():
        if(form.data['username'] == admin_user['username'] and
            form.data['password'] == admin_user['password']):
            return redirect('/')
        else:
            flash('Wrong username or password')
    return render_template('login.html', form=form)

import models

if __name__ == '__main__':
    app.run(debug=True)