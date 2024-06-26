from typing import Type

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.database import engine, Base


def is_id_exists(session: Session, orm_model: Type[Base], target_id: int, id_field_name: str = 'id') -> bool:
    model_id = orm_model.__dict__.get(id_field_name)
    query = select(model_id).where(model_id == target_id)
    result = session.execute(query).scalar_one_or_none()
    return result is not None
