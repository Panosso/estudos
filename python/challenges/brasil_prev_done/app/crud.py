from sqlalchemy.orm import Session

import models
import schemas


# Person functions and creations
def create_person(db: Session, person: schemas.PersonCreate):
    db_person = models.Person(**person.dict())
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person


def get_person_by_cpf(db: Session, person_cpf: str):
    return db.query(models.Person).\
        filter(models.Person.cpf == person_cpf).first()


def get_person_by_id(db: Session, person_id: int):
    return db.query(models.Person).\
        filter(models.Person.id == person_id).first()


# Product functions and creations
def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_product_by_susep(db: Session, product_susep: str):

    return db.query(models.Product).\
        filter(models.Product.susep == product_susep).first()


def get_product_by_name(db: Session, product_name: str):

    return db.query(models.Product).\
        filter(models.Product.nome == product_name).first()


def get_product_by_id(db: Session, product_id: int):

    return db.query(models.Product).\
        filter(models.Product.id == product_id).first()


def get_product_by_idPlan(db: Session, plan_id: int):
    plan = get_plan_by_id(db, plan_id).idProduto

    product = get_product_by_id(db, plan)

    return product


# Plan functions and creations
def create_plan(db: Session, plan: schemas.PlanCreate):
    db_plan = models.Plan(**plan.dict())
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return db_plan


def get_plan_by_person_product(db: Session,
                               person_id: int,
                               product_id: int):

    return db.query(models.Plan).\
        filter(models.Plan.idCliente == person_id).\
        filter(models.Plan.idProduto == product_id).first()


def get_plan_by_idHash(db: Session, idHash: str):

    return db.query(models.Plan).\
        filter(models.Plan.idHash == idHash).first()


def get_plan_by_id(db: Session, id: int):

    return db.query(models.Plan).\
        filter(models.Plan.id == id).first()


# Extra Contrib functions and creations
def create_extra_contrib(db: Session,
                         extra_contrib: schemas.ExtraContributionCreate):
    db_extra_contrib = models.ExtraContribution(**extra_contrib.dict())
    db.add(db_extra_contrib)
    db.commit()
    db.refresh(db_extra_contrib)
    return db_extra_contrib


def get_extra_contrib_by_idHash(db: Session, idHash: str):

    return db.query(models.ExtraContribution).\
        filter(models.ExtraContribution.idHash == idHash).first()


def get_extra_contrib_by_id(db: Session, id: int):

    return db.query(models.ExtraContribution).\
        filter(models.ExtraContribution.id == id).first()


def get_extra_contrib_by_idPlan(db: Session, plan_id: int):

    return db.query(models.ExtraContribution).\
        filter(models.ExtraContribution.idPlano == plan_id).\
        order_by(models.ExtraContribution.dataCriacao).all()


def get_extra_contrib_by_planId(db: Session, plan_id: int):

    return db.query(models.ExtraContribution).\
        filter(models.ExtraContribution.idPlano == plan_id).first()


def add_extra_contrib_plan(db: Session, plan_id: int, contrib_value: float):

    plan = get_plan_by_id(db, plan_id)

    plan.aporte += contrib_value
    db.commit()

    return plan


# Rescue Functions and creations
def create_rescue(db: Session, rescue: schemas.RescueCreate):
    db_rescue = models.Rescue(**rescue.dict())
    db.add(db_rescue)
    db.commit()
    db.refresh(db_rescue)
    return db_rescue


def get_rescue_by_idHash(db: Session, idHash: str):

    return db.query(models.Rescue).\
        filter(models.Rescue.idHash == idHash).first()


def get_rescue_by_id(db: Session, id: int):

    return db.query(models.Rescue).\
        filter(models.Rescue.id == id).first()


def get_last_rescue_date(db: Session, plan_id: int):

    return db.query(models.Rescue).\
        filter(models.Rescue.idPlano == plan_id).\
        order_by(models.Rescue.dataCriacao.desc()).first()


def get_rescue_by_idPlan(db: Session, plan_id: int):

    return db.query(models.Rescue).\
        filter(models.Rescue.idPlano == plan_id).\
        order_by(models.Rescue.dataCriacao).all()


def rescue_value_plan(db: Session, plan_id: int, contrib_value: float):

    plan = get_plan_by_id(db, plan_id)

    plan.aporte -= contrib_value
    db.commit()

    return plan
