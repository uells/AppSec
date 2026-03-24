from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import json
import os


app = Flask(__name__)
app.secret_key = 'change_this_to_secure_random_value'  #  — заменить 

DATA_FILE = os.path.join('data', 'users.json')
MESSAGES_FILE = os.path.join('data', 'messages.json')

def load_json(file):
    if not os.path.exists(file):
        return {}
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, file):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('chat'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        if not username or not password or not email:
            flash('Заполните все поля', 'error')
            return render_template('register.html')
        users = load_json(DATA_FILE)
        if username in users:
            flash('Пользователь уже существует', 'error')
            return render_template('register.html')
        # Хешируем пароль
        pw_hash = generate_password_hash(password)
        users[username] = {"email": email, "password": pw_hash}
        save_json(users, DATA_FILE)
        flash('Регистрация прошла успешно. Войдите.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        users = load_json(DATA_FILE)
        user = users.get(username)
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            flash('Вы успешно вошли', 'success')
            return redirect(url_for('chat'))
        flash('Неверный логин или пароль', 'error')
        return render_template('login.html')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Вы вышли', 'info')
    return redirect(url_for('login'))

@app.route('/chat', methods=['GET'])
def chat():
    if 'username' not in session:
        return redirect(url_for('login'))
    # Загружаем собственные сообщения пользователя (пока что) из файла
    messages = load_json(MESSAGES_FILE)
    user = session.get('username') 
    user_messages = messages.get(user, [])
    return render_template('chat_vul.html', username=user, user_messages=user_messages)

@app.route('/send', methods=['POST'])
def send():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    # Запись собственных сообщений пользователя в файл
    message = request.form.get('message', '')
    all_messages = load_json(MESSAGES_FILE)
    user = session.get('username')
    now = datetime.now()
    if user not in all_messages:
        all_messages[user] = []
    all_messages[user].append({
        'text': message,
        'time': now.strftime("%d-%m-%Y %H:%M")
    })
    save_json(all_messages, MESSAGES_FILE)
    return redirect(url_for('chat'))

if __name__ == '__main__':
    app.run(debug=True)
