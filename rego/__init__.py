import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db = SQLAlchemy()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='secret_here!',
    )
    Bootstrap(app)
    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello world'

    with app.app_context():
        db.init_app(app)
        db.create_all()

    from . import fop, orgadm, api
    app.register_blueprint(fop.bp)
    app.register_blueprint(orgadm.bp)
    app.register_blueprint(api.bp)
        
    return app
