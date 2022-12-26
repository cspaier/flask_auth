# Exemple d'authentification

## Description
Ce projet est un exemple d'authentification en [flask](https://flask.palletsprojects.com/) avec le framework CSS [bulma](https://bulma.io")  pour le front-end.

On a voulontairement choisi d'utiliser [flask_mysqldb](https://flask-mysqldb.readthedocs.io/) afin de faire les transactions sur la base de donnée "à la main".

Un projet non pédagogique choisirai probablement un ORM du type [SQLalchemy](https://www.sqlalchemy.org/).

Le stockage des mots de passe est fait en SHA256 sans salage. Un projet non pédagogique utiliserait les fonctions de [werkzeug](https://werkzeug.palletsprojects.com/en/2.2.x/utils/#module-werkzeug.security) ou [flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/1.0.1/).

## Déploiement sous debian:
1. Installation des dépendances systeme

`sudo apt install python3-dev default-libmysqlclient-dev build-essential`

2. Mise en place de l'environnement python

créer un dossier de travail: `mkdir flask_auth`

S'y rendre: `cd mkdir`

Cloner le dépot: `git clone ????`

Créer un environnement virtuel python: `python3 -m venv venv`

L'activer: `source venv bin activate`

Installer les dépendances python: `pip install -r requirements.txt`

3. Créer la base de donnée:

Dans Mysql: `source utilisateurs.sql`

L'utilisateur `test` a pour mot de passe `test`.

4. Modifier la configuration Mysql
Dans `config.toml`, indiquer les variables relatives à la connection MYsql.
```toml
# Utilisateur Mysql
MYSQL_USER = ""
# Mot de passe Mysql
MYSQL_PASSWORD = ""
```

5. Générer une [clef secrète Flask](https://flask.palletsprojects.com/en/2.2.x/config/#SECRET_KEY)
Coller le résultat de cette commande dans le fichier de configuration `config.toml`:
`python -c 'import secrets; print(secrets.token_hex())'`

```toml
# Clef secrète Flask: https://flask.palletsprojects.com/en/2.2.x/config/#SECRET_KEY
SECRET_KEY = 'Changez moi en production!'
```

6. Tester le serveur:
Vous pouvez lancer le serveur pour tester avec `flask --app flask_auth.py run`
```sh
flask_auth_exemple$ flask --app flask_auth.py run
 * Serving Flask app 'flask_auth.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```


### Mise en production

1. Tester le serveur derrière gunicorn: `gunicorn --bind 127.0.0.1:8080 --config gunicorn_config.py wsgi:app`
Le service sera accessible à l'adresse `http://127.0.0.1:8080`
```
flask_auth_exemple$ gunicorn --bind 127.0.0.1:8080 --config gunicorn_config.py wsgi:app
[2022-12-26 17:10:35 +0100] [4668] [INFO] Starting gunicorn 20.1.0
[2022-12-26 17:10:35 +0100] [4668] [INFO] Listening at: http://127.0.0.1:8080 (4668)
[2022-12-26 17:10:35 +0100] [4668] [INFO] Using worker: sync
[2022-12-26 17:10:35 +0100] [4670] [INFO] Booting worker with pid: 4670
```


2. Créer un service systemd
`sudo nano /etc/systemd/system/flask_auth.service`
Le fichier contiendra ce qui suit:
```
[Unit]
Description=Gunicorn instance to serve flask application
After=network.target

[Service]
User=REMPLACER PAR UTILISATEUR UNIX
Group=www-data
WorkingDirectory=/CHEMIN/VERS/LE/DOSSIER/flask_auth/flask_auth
Environment="PATH=/CHEMIN/VERS/LE/DOSSIER/flask_auth/venv/bin"
ExecStart=/CHEMIN/VERS/LE/DOSSIER/flask_auth/venv/bin/gunicorn --config gunicorn_config.py wsgi:app

[Install]
WantedBy=multi-user.target
```

Activer et démarer le service:
```
$ sudo systemctl start flask_auth_.service
$ sudo systemctl enable flask_auth_.service
```

3. Créer un serveur virtuel Apache2
Le fichier devra contenir la balise location suivante
```
	<Location />
		ProxyPass unix:/CHEMIN/VERS/LE/DOSSIER/flask_auth/flask_auth/flask_auth_.sock|http://127.0.0.1/
		ProxyPassReverse unix:/CHEMIN/VERS/LE/DOSSIER/flask_auth/flask_auth/flask_auth_.sock|http://127.0.0.1/
	</Location>

```

