from flask import Flask


from lib.db import init_db

app = Flask(__name__)

app.config.from_object('app.config')
app.config.from_object('lib.config')


init_db(app)