from flask import Flask, render_template, redirect, request, url_for, session
import register_login_manager

app = Flask(__name__)


@app.route('/')
@app.route('/#')
def main():
    return render_template('main_page.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = register_login_manager.check_user(request.form['register_user_name'])
        if len(user) == 0:

            password = register_login_manager.hash_password(request.form['register_password'])

            login_name = request.form['register_user_name']
            print("registered")
            register_login_manager.register(login_name, password)

            return redirect(url_for('main', already_used=False))
        else:
            return redirect(url_for('register', already_used=True))
    return render_template('registration.html', already_used=False)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form['user_name']

        data = register_login_manager.login(user_name)
        if not data:
            return redirect(url_for('main',log=False))
        user_id = register_login_manager.get_id_by_user_name(user_name)['id']
        session['user_name'] = user_name
        session['user_id'] = user_id

        log = register_login_manager.verify_password(request.form.to_dict()['password'], data[0]['password'])
        if log:

            return redirect(url_for('main'))
        else:
            session.pop('user_name', None)
            session.pop('user_id', None)
            log=False
            return redirect(url_for('main', log=False))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_name', None)
    return redirect(url_for('main'))


if __name__ == '__main__':
    app.secret_key = "Qd3A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"
    app.run(debug=True)
