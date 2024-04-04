# Задание №9
# Создать страницу, на которой будет форма для ввода имени
# и электронной почты
# При отправке которой будет создан cookie файл с данными
# пользователя
# Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.

from flask import Flask, render_template, request,redirect, url_for, session

app = Flask(__name__)

app.secret_key = b'84725e64a911d73dabc58c7a3c4cdae294c77a9d1993967f58896ad8ca2cfbb9'


@app.route('/', methods=['GET', 'POST'])
def login():
    context = {
        'login': 'Авторизация'
    }
    if request.method == 'POST':
        session['name'] = request.form.get('name')
        session['email'] = request.form.get('email')
        return redirect(url_for('success'))
    return render_template('app_9_index.html', **context)


@app.route('/successlogin/', methods=['GET', 'POST'])
def success():
    if 'name' in session:
        context = {
            'name': session['name'],
            'email': session['email'],
            'title': 'Добро пожаловать'
        }
        if request.method == 'POST':
            session.pop('name', None)
            session.pop('email', None)
            return redirect(url_for('login'))
        return render_template('successlogin.html', **context)
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)