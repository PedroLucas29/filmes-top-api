from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

db = SQLAlchemy()


class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(120), nullable=False)
    celular = Column(String(20), nullable=True)
    email = Column(String(120), unique=True, nullable=False)
    alugueis = relationship('Aluguel', backref='usuario', lazy=True)


class Filme(db.Model):
    __tablename__ = 'filmes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(200), nullable=False)
    genero = Column(String(100), nullable=False)
    ano = Column(Integer, nullable=False)
    sinopse = Column(String(500), nullable=True)
    diretor = Column(String(120), nullable=True)
    nota_final = Column(Float, default=0)
    total_avaliacoes = Column(Integer, default=0)
    alugueis = relationship('Aluguel', backref='filme', lazy=True)


class Aluguel(db.Model):
    __tablename__ = 'alugueis'
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    filme_id = Column(Integer, ForeignKey('filmes.id'), nullable=False)
    data_locacao = Column(DateTime, default=datetime.utcnow)
    nota = Column(Integer)

    def avaliar(self, nova_nota):
        self.nota = nova_nota
        filme = self.filme
        filme.total_avaliacoes += 1
        filme.nota_final = (
            filme.nota_final * (filme.total_avaliacoes - 1) + nova_nota) / filme.total_avaliacoes
