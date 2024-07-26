from sqlalchemy import (CHAR, Column, Date, DateTime, Float, ForeignKey,
                        Integer, String, Text)

from database import Base


class Person(Base):

    __tablename__ = 'BP_Entidade'

    id = Column(Integer, primary_key=True, index=True)
    cpf = Column(String(11), nullable=False, index=True)
    nome = Column(String(50), nullable=False, index=True)
    email = Column(String(255), nullable=False, index=True)
    dataDeNascimento = Column(Date, nullable=False, index=True)
    idade = Column(Integer, nullable=False, index=True)
    sexo = Column(CHAR(1), nullable=False, index=True)
    rendaMensal = Column(Float(precision=2), nullable=False, index=True)
    idHash = Column(Text, nullable=False)
    dataCriacao = Column(DateTime, nullable=False, index=True)


class Product(Base):

    __tablename__ = 'BP_Produto'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150), nullable=False, index=True)
    susep = Column(String(20), nullable=False, index=True)
    expiracaoDeVenda = Column(Date, nullable=False, index=True)
    idadeDeEntrada = Column(Integer, nullable=False, index=True)
    idadeDeSaida = Column(Integer, nullable=False, index=True)
    carenciaInicialDeResgate = Column(Integer, nullable=False, index=True)
    carenciaEntreResgates = Column(Integer, nullable=False, index=True)
    idHash = Column(Text, nullable=False)
    dataCriacao = Column(DateTime, nullable=False, index=True)

    valorMinimoAporteInicial = Column(
        Float(precision=2), nullable=False, index=True)

    valorMinimoAporteExtra = Column(
        Float(precision=2), nullable=False, index=True)


class Plan(Base):

    __tablename__ = 'BP_Plano'

    id = Column(Integer, primary_key=True, index=True)
    idCliente = Column(Integer, ForeignKey("BP_Entidade.id"))
    hashCliente = Column(String(50), nullable=False, index=True)
    idProduto = Column(Integer, ForeignKey("BP_Produto.id"))
    hashProduto = Column(String(50), nullable=False, index=True)
    aporte = Column(Float(precision=2), nullable=False, index=True)
    dataDaContratacao = Column(Date, nullable=False, index=True)
    idHash = Column(Text, nullable=False)
    dataCriacao = Column(DateTime, nullable=False, index=True)


class ExtraContribution(Base):

    __tablename__ = 'BP_AporteExtra'

    id = Column(Integer, primary_key=True, index=True)
    idCliente = Column(Integer, ForeignKey("BP_Entidade.id"))
    hashCliente = Column(String(50), nullable=False, index=True)
    idPlano = Column(Integer, ForeignKey("BP_Produto.id"))
    hashPlano = Column(String(50), nullable=False, index=True)
    aporte = Column(Float(precision=2), nullable=False, index=True)
    idHash = Column(Text, nullable=False)
    dataCriacao = Column(DateTime, nullable=False, index=True)


class Rescue(Base):

    __tablename__ = 'BP_Resgate'

    id = Column(Integer, primary_key=True, index=True)
    idPlano = Column(Integer, ForeignKey("BP_Plano.id"))
    hashPlano = Column(String(50), nullable=False, index=True)
    valorResgate = Column(Float(precision=2), nullable=False, index=True)
    idHash = Column(Text, nullable=False)
    dataCriacao = Column(DateTime, nullable=False, index=True)
