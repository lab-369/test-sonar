import os
import sqlite3
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Vulnerable to SQL Injection
def get_user(username):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '{}';".format(username)
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    return user

# Vulnerable to Cross-Site Scripting (XSS)
@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', '')
    template = "<h1>Hello, {}!</h1>".format(name)
    return render_template_string(template)

# Vulnerable to Command Injection
@app.route('/run', methods=['POST'])
def run():
    command = request.form['command']
    os.system(command)
    return "Command executed"

# Insecure Password Storage
def store_password(password):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    query = "INSERT INTO passwords (password) VALUES ('{}');".format(password)
    cursor.execute(query)
    conn.commit()
    conn.close()

# Main route for testing
@app.route('/')
def index():
    return '''
    <h1>Vulnerable Python Application</h1>
    <form action="/run" method="post">
        Command: <input type="text" name="command">
        <input type="submit" value="Run">
    </form>
    <form action="/greet" method="get">
        Name: <input type="text" name="name">
        <input type="submit" value="Greet">
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
