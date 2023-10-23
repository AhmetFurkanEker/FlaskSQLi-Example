from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import hashlib
import bleach

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# SQLite3 veritabanı bağlantısını oluştur
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Kullanıcı tablosunu oluştur (eğer yoksa)
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')

conn.commit()
conn.close()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = bleach.clean(request.form['username'])
        password = bleach.clean(request.form['password'])

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        # Parametreli sorgu kullanarak SQL enjeksiyonlarına karşı koruma sağla
        c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))

        user = c.fetchone()
        conn.close()

        if user:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Geçersiz kullanıcı adı veya şifre'), 302

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('login'))

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = bleach.clean(request.form['username'])
        password = bleach.clean(request.form['password'])
        confirm_password = bleach.clean(request.form['confirm_password'])

        if password != confirm_password:
            return render_template('registration.html', error='Şifreler uyuşmuyor')

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        # Kullanıcı adının veritabanında daha önce kullanılıp kullanılmadığını kontrol et
        c.execute("SELECT * FROM users WHERE username=?", (username,))
        existing_user = c.fetchone()

        if existing_user:
            return render_template('registration.html', error='Bu kullanıcı adı zaten alınmış')

        # Şifreyi hash'le ve kullanıcıyı eklemek için parametreli sorguyu çalıştır
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))

        conn.commit()
        conn.close()

        return redirect(url_for('login'))

    return render_template('registration.html')

if __name__ == '__main__':
    app.run(debug=True)
