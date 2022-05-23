from flask_sqlalchemy import SQLAlchemy


from flask_migrate import Migrate


db = SQLAlchemy()


import lib.models


def init_db(app):
    db.init_app
    Migrate(app, db)