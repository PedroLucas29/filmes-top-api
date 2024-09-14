from flask import Flask, jsonify, request
from database.model import Usuario, Filme, Aluguel, db
from sqlalchemy.orm.exc import NoResultFound
from flask_migrate import Migrate
from os import getenv
from dotenv import load_dotenv


app = Flask(__name__)

# Configurar a URL do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar a conexão com o banco de dados
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def first():
    return 'Hello'


if __name__ == '__main__':
    app.run(debug=True)
