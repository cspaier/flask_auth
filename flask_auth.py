import toml
from flask import Flask, request, redirect, flash, url_for, render_template, session
from flask_mysqldb import MySQL
from utils import empreinte_mdp


app = Flask(__name__)
app.config.from_file("config.toml", load=toml.load)
mysql = MySQL(app)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/creer-compte', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        bdd = mysql.connection.cursor()

        # On vérifie si un utilisateur existe déja avec le même nom
        bdd.execute(
            "SELECT * FROM utilisateur WHERE nom = %s", (username,)
        )
        user = bdd.fetchone()
        if user is not None:
            error = 'Ce nom d\'utilisateur est déja pris'

        if error is None:
            empreinte = empreinte_mdp(password)
            bdd.execute(
                "INSERT INTO utilisateur (nom, empreinte) VALUES (%s, %s)",
                (username, empreinte),
            )
            mysql.connection.commit()
            flash(f'Le compte {username} a été créé.', 'is-primary')
            return redirect(url_for("login"))

        flash(error, 'is-danger')

    return render_template('register.html')


@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        bdd = mysql.connection.cursor()
        bdd.execute(
            "SELECT * FROM utilisateur WHERE nom = %s", (username,)
        )
        user = bdd.fetchone()
        if user is not None and user['empreinte'] == empreinte_mdp(password):
            session.clear()
            session['user_id'] = user['id_utilisateur']
            session['username'] = username
            return redirect(url_for('index'))
        flash('Mot de passe ou identifiant incorrect', 'is-danger')

    return render_template('login.html')


@app.route('/deconnection', methods=('GET', 'POST'))
def logout():
    if request.method == 'POST':
        session.clear()
        return redirect(url_for('index'))
    return render_template('logout.html')
