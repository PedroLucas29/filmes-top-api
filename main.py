from flask import Flask
from database.model import db
from sqlalchemy.orm.exc import NoResultFound
from flask_migrate import Migrate
from os import getenv
from dotenv import load_dotenv
from controllers import filmes_controller
from cache.cache_client import init_cache


load_dotenv()

app = Flask(__name__)

# Configurar a URL do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar Cache
init_cache(app)

# Inicializar a conexão com o banco de dados
db.init_app(app)
migrate = Migrate(app, db)

# Registrar Blueprint dos filmes
app.register_blueprint(filmes_controller.filmes_controller, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, jsonify, request
# from database.model import Usuario, Filme, Aluguel, db
# from sqlalchemy.orm.exc import NoResultFound
# from flask_migrate import Migrate
# from os import getenv
# from dotenv import load_dotenv
# from controllers import filmes_controller
# from cache.cache_client import Cache

# app = Flask(__name__)

# # Configurar a URL do banco de dados
# app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Cache(app)

# # Inicializar a conexão com o banco de dados
# db.init_app(app)
# migrate = Migrate(app, db)

# app.register_blueprint(filmes_controller.filmes_controller, url_prefix='/')


# if __name__ == '__main__':
#     app.run(debug=True)
