from flask import Flask
from database.model import db
from sqlalchemy.orm.exc import NoResultFound
from flask_migrate import Migrate
from os import getenv
from dotenv import load_dotenv
from controllers import filmes_controller
from cache.cache_client import init_cache
import asyncio
import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_cache(app)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(filmes_controller.filmes_controller, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)
