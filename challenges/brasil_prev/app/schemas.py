from datetime import date, datetime
from enum import Enum

from pydantic import BaseModel


class Sexo(str, Enum):
    masculino = 'M'
    feminino = 'F'


class PersonBase(BaseModel):
    cpf: str
    nome: str
    email: str
    dataDeNascimento: date
    idade: int = None
    sexo: Sexo
    rendaMensal: float
    idHash: str = None
    dataCriacao: datetime = None

    class Config:
        use_enum_values = True


class PersonCreate(PersonBase):
    pass


class Person(PersonBase):
    id: int

    class Config:
        orm_mode = True


class ProductBase(BaseModel):

    nome: str
    susep: str
    expiracaoDeVenda: date
    idadeDeEntrada: int
    idadeDeSaida: int
    carenciaInicialDeResgate: float
    carenciaEntreResgates: float
    valorMinimoAporteInicial: float
    valorMinimoAporteExtra: float
    idHash: str = None
    dataCriacao: datetime = None


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


class PlanBase(BaseModel):

    idCliente: str
    hashCliente: str = None
    idProduto: str
    hashProduto: str = None
    aporte: float
    dataDaContratacao: date
    idHash: str = None
    dataCriacao: datetime = None


class PlanCreate(PlanBase):
    pass


class Plan(PlanBase):
    id: int

    class Config:
        orm_mode = True


class ExtraContributionBase(BaseModel):

    idCliente: str
    hashCliente: str = None
    idPlano: str
    hashPlano: str = None
    aporte: float
    idHash: str = None
    dataCriacao: datetime = None


class ExtraContributionCreate(ExtraContributionBase):
    pass


class ExtraContribution(ExtraContributionBase):
    id: int

    class Config:
        orm_mode = True


class RescueBase(BaseModel):

    idPlano: str
    hashPlano: str = None
    valorResgate: float
    idHash: str = None
    dataCriacao: datetime = None


class RescueCreate(RescueBase):
    pass


class Rescue(RescueBase):
    id: int

    class Config:
        orm_mode = True
