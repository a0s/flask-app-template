import os

from flask import Flask
from flask_migrate import Migrate

from app.models import db, load_all_models


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('app.config.Config')

    load_all_models()
    migrate = Migrate(directory=os.path.join('app', 'migrations'))

    db.init_app(app)
    migrate.init_app(app, db)

    return app
