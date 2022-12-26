
"""Fichier de configuration de gunicorn
https://docs.gunicorn.org/en/stable/settings.html
"""
import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
bind = 'unix:flask_auth.sock'
umask = 0o007
reload = True

# logging
accesslog = '-'
errorlog = '-'
