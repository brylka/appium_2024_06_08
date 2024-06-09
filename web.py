from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']

        # Sprawdzanie, czy dane są poprawne
        if login == 'test' and (password == 'qwer1234' or password == '*'):
            return render_template_string('<h1>Witaj, {{ login }}</h1>', login=login)
        else:
            message = 'Błędne dane'

    # Renderowanie formularza z ewentualnym komunikatem o błędzie
    return render_template_string('''
        <form method="post">
            Login: <input type="text" name="login"><br>
            Hasło: <input type="password" name="password"><br>
            <input type="submit" value="Zaloguj">
        </form>
        <div style="color:red;">{{ message }}</div>
        ''', message=message)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
