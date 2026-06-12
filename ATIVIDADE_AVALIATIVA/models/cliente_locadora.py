from . import db
from .base import ModeloBase


class ClienteLocadora(ModeloBase):
    __tablename__ = "clientes_locadora"

    nome = db.Column(db.String(120), nullable=False)
     cpf = db.Columndb.String((14), nullable=False)
     cnh = db.Columndb.String((11), nullable=False)

    # TODO ALUNO: relationship com Locacao
    locacoes = db.relationship("Locacao", back_populates="cliente")

    @classmethod
    def listar(cls):
        return cls.query.order_by(cls.nome).all()