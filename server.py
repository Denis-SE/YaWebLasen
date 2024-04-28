from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from constants_data import *

app = Flask(__name__)
app.secret_key = 'your_secret_key'
login_check = 1


# Функция для соединения с базой данных
def connect_db():
    return sqlite3.connect('database.db')


@app.route('/')
def index():
    return render_template('news.html', news=news)


# Профиль пользователя
@app.route('/profile.html', methods=['GET', 'POST'])
def profile_page():
    if login_check == 0:
        return render_template('profile.html')
    else:
        return render_template('log_or_reg.html')


# Регистрация пользователя
@app.route('/register.html', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            return 'Пользователь с таким именем уже существует'
        finally:
            conn.close()
    return render_template('register.html')


# Вход пользователя
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return 'Неверное имя пользователя или пароль'
    return render_template('login.html')


# Выход пользователя
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/news.html')
def news_page():
    return render_template('news.html', news=news)


@app.route('/concerts.html')
def concerts_page():
    return render_template('concerts.html', concerts=concerts)


@app.route('/music.html')
def music_page():
    return render_template('music.html', music=music)


@app.route('/video.html')
def video_page():
    return render_template('video.html', videos=videos)


@app.route('/info.html')
def info_page():
    return render_template('info.html')


@app.route('/shop.html')
def merch_page():
    return render_template('shop.html')


@app.route('/браслет-lasen.html')
def b_merch_page():
    return render_template('браслет-lasen.html')


@app.route('/значок-lasen.html')
def z_merch_page():
    return render_template('значок-lasen.html')


@app.route('/подарочный-пакет-lasen.html')
def p_merch_page():
    return render_template('подарочный-пакет-lasen.html')


@app.route('/стикерпак-lasen.html')
def s_merch_page():
    return render_template('стикерпак-lasen.html')


@app.route('/футболка-lasen.html')
def f_merch_page():
    return render_template('футболка-lasen.html')


if __name__ == '__main__':
    app.run(debug=True)
