import hashlib
from datetime import datetime

from fastapi import (Depends, FastAPI, HTTPException, encoders, responses,
                     status)
from sqlalchemy.orm import Session

import crud
import models
import schemas
import utils
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
now = datetime.now()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/person/{person_id}', response_model=schemas.Person)
def read_person(person_id: int,
                db: Session = Depends(get_db)):

    db_person = crud.get_person_by_id(db, person_id)
    if db_person is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Cliente não encontrado")

    return db_person


@app.post('/create_person/', response_model=schemas.Person)
def create_person(person: schemas.PersonCreate,
                  db: Session = Depends(get_db)):

    if utils.cpf_validator(person.cpf):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="CPF invalido.")

    if utils.email_validator(person.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="E-mail invalido.")

    person.idade = utils.age(person.dataDeNascimento)
    if person.idade < 18:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Individio menor de 18 anos.")

    person = crud.get_person_by_cpf(db, person_cpf=person.cpf)
    if person:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Existe um cadastro com esse CPF")

    cpf = person.cpf

    person.idHash = hashlib.md5(cpf.encode()).hexdigest()

    person.dataCriacao = now

    crud.create_person(db=db, person=person)

    person = crud.get_person_by_cpf(db, person_cpf=cpf)

    res = {
        'id': f'{person.id}' + ' | ' + f'{person.idHash}',
    }

    return responses.JSONResponse(content=res)


@app.post('/create_product/', response_model=schemas.Product)
def create_product(product: schemas.ProductCreate,
                   db: Session = Depends(get_db)):

    if utils.susep_validator(product.susep):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Susep Inválido. Valor esperado 15414.6XXXXX/AAAA-DV")

    if crud.get_product_by_name(db, product.nome):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Existe um produto com esse nome.")

    db_product = crud.get_product_by_susep(db, product_susep=product.susep)
    if db_product:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Existe um produto com esse susep")

    product.idHash = hashlib.md5(product.susep.encode()).hexdigest()
    product.dataCriacao = now
    crud.create_product(db=db, product=product)

    susep = product.susep

    product = crud.get_product_by_susep(db, product_susep=susep)

    res = {
        'id': f'{product.id}' + ' | ' + f'{product.idHash}',
    }

    return responses.JSONResponse(content=res)


@app.get('/product/{product_id}', response_model=schemas.Product)
def read_product(product_id: int,
                 db: Session = Depends(get_db)):

    db_product = crud.get_product_by_id(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Produto não encontrado")

    return db_product


@app.post('/plan_hiring/', response_model=schemas.Plan)
def plan_hiring(plan: schemas.PlanCreate,
                db: Session = Depends(get_db)):

    person = crud.get_person_by_id(db,
                                   int(plan.idCliente.split(' | ')[0].
                                       replace('\'', '')))

    if not person:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cliente não encontrado.")

    product = crud.get_product_by_id(db,
                                     int(plan.idProduto.split(' | ')[0].
                                         replace('\'', '')))

    if not product:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Produto não encontrado.")

    if utils.buy_validate_age(product.idadeDeEntrada, person.idade):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cliente não tem idade necessária para adquirir o produto.")

    if utils.buy_validate_expired_date(product.expiracaoDeVenda,
                                       plan.dataDaContratacao):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Data de compra do produto expirada.")

    if utils.buy_validate_contribution(product.valorMinimoAporteInicial,
                                       plan.aporte):

        detail = "Esse produto só pode ser adquirido se o aporte for de R$"
        detail += f"{product.valorMinimoAporteInicial} ou mais"

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail)

    db_plan = crud.get_plan_by_person_product(db,
                                              person_id=person.id,
                                              product_id=product.id)

    if db_plan:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Esse cliente ja possui esse plano")

    result = ''.join([x for x in str(now) if x.isdigit()])
    plan.idHash = hashlib.md5(result.encode()).hexdigest()
    plan.dataCriacao = now

    plan.idCliente = person.id
    plan.hashCliente = person.idHash
    plan.idProduto = product.id
    plan.hashProduto = product.idHash

    crud.create_plan(db=db, plan=plan)

    idHash = plan.idHash

    plan = crud.get_plan_by_idHash(db, idHash=idHash)

    res = {
        'id': f'{plan.id}' + ' | ' + f'{plan.idHash}',
    }

    return responses.JSONResponse(content=res)


@app.get('/plan/{plan_id}', response_model=schemas.Plan)
def read_plan(plan_id: int,
              db: Session = Depends(get_db)):

    db_plan = crud.get_plan_by_id(db, plan_id)
    if db_plan is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Plano não encontrado")

    return db_plan


@app.post('/extra_contribuition/',
          response_model=schemas.ExtraContribution)
def extra_contribuition(extra_contri: schemas.ExtraContributionCreate,
                        db: Session = Depends(get_db)):

    plan = crud.get_plan_by_id(db,
                               int(extra_contri.idPlano.split(' | ')[0].
                                   replace('\'', '')))

    if not plan:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Plano não encontrado.")

    person = crud.get_person_by_id(db, plan.idCliente)

    if not person:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cliente não encontrado.")

    product = crud.get_product_by_id(db, plan.idProduto)

    if not product:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Produto não encontrado.")

    if utils.buy_validate_contribution(product.valorMinimoAporteExtra,
                                       extra_contri.aporte):

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Valor de aporte menor que o minimo do produto")

    result = ''.join([x for x in str(now) if x.isdigit()])
    extra_contri.idHash = hashlib.md5(result.encode()).hexdigest()

    extra_contri.dataCriacao = now

    extra_contri.idCliente = person.id
    extra_contri.hashCliente = person.idHash
    extra_contri.idPlano = plan.id
    extra_contri.hashPlano = plan.idHash

    crud.create_extra_contrib(db=db, extra_contrib=extra_contri)

    extra_contri = crud.get_extra_contrib_by_idHash(db,
                                                    extra_contri.idHash)

    crud.add_extra_contrib_plan(
        db=db, contrib_value=extra_contri.aporte, plan_id=plan.id)

    res = {
        'id': f'{extra_contri.id}' + ' | ' + f'{extra_contri.idHash}',
    }

    return responses.JSONResponse(content=res)


@app.get('/extra_contribuition/{plan_id}',
         response_model=schemas.ExtraContribution)
def read_extra_contribuition(plan_id: int,
                             db: Session = Depends(get_db)):

    extra_contrib = encoders.jsonable_encoder(
        crud.get_extra_contrib_by_idPlan(db=db, plan_id=plan_id))

    if extra_contrib is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Aportes extras não encontrados")

    return responses.JSONResponse(content=extra_contrib)


@app.post('/resgate/', response_model=schemas.Rescue)
def create_rescue(rescue: schemas.RescueCreate,
                  db: Session = Depends(get_db)):

    plan = crud.get_plan_by_id(db,
                               int(rescue.idPlano.split(' | ')[0].
                                   replace('\'', '')))

    if not plan:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Plano inexistente ou inválido")

    product = crud.get_product_by_idPlan(db=db, plan_id=plan.id)

    if not product:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Produto inexistente ou inválido")

    last_rescued_date = crud.get_last_rescue_date(
        db=db, plan_id=plan.id).dataCriacao

    if utils.rescue_min_days(product.carenciaEntreResgates,
                             last_rescued_date):

        detail = "A carencia entre os resgates são de "
        detail += f"{product.carenciaEntreResgates} dias"

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail)

    if utils.rescue_min_days(product.carenciaInicialDeResgate,
                             plan.dataCriacao):

        detail = "A carencia inicial de resgate são de "
        detail += f"{product.carenciaInicialDeResgate} dias"

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail)

    if utils.value_rescue_validation(rescue.valorResgate, plan.aporte):

        detail = "Valor solicitado maior que o permitido."

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail)

    rescue.idPlano = plan.id
    rescue.hashPlano = plan.idHash

    result = ''.join([x for x in str(now) if x.isdigit()])
    rescue.idHash = hashlib.md5(result.encode()).hexdigest()
    rescue.dataCriacao = now
    crud.create_rescue(db=db, rescue=rescue)

    rescue = crud.get_rescue_by_idHash(db,
                                       rescue.idHash)

    crud.rescue_value_plan(
        db=db, contrib_value=rescue.valorResgate, plan_id=plan.id)

    res = {
        'id': f'{rescue.id}' + ' | ' + f'{rescue.idHash}',
    }

    return responses.JSONResponse(content=res)


@app.get('/resgates/{plan_id}', response_model=schemas.Rescue)
def read_rescue(plan_id: int,
                db: Session = Depends(get_db)):

    rescues = encoders.jsonable_encoder(
        crud.get_rescue_by_idPlan(db=db, plan_id=plan_id))

    if rescues is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Resgates não encontrados")

    return responses.JSONResponse(content=rescues)
