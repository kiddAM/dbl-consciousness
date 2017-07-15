# here lies our app

from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')

# OVERRIDES
app.config.from_pyfile('config.py') # instance config
# app.config.from_envvar('APP_CONFIG_FILE') # set path to config in env
