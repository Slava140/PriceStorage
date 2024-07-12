from typing import Mapping

from sqlalchemy import select, insert, delete, update
from sqlalchemy.orm import Session

from src.database import engine
from src.models.categories import Category as CategoryModel


class CategoryRepository:
    @staticmethod
    def is_id_exists(category_id: int) -> bool:
        with Session(engine) as session:
            query = select(CategoryModel.id).where(CategoryModel.id == category_id)
            result = session.execute(query).scalar_one_or_none()
            return result is not None

    @staticmethod
    def create_category(category_mapping: Mapping) -> dict | None:
        with Session(engine) as session:
            stmt = insert(
                CategoryModel
            ).values(
                **category_mapping
            ).returning(
                CategoryModel.id,
                CategoryModel.name
            )
            data = session.execute(stmt).mappings().one_or_none()
            session.commit()
        return dict(data)

    @staticmethod
    def read_category(category_id: int) -> dict | None:
        with Session(engine) as session:
            query = select(
                CategoryModel.id,
                CategoryModel.name
            ).where(
                CategoryModel.id == category_id
            )
            data = session.execute(query).mappings().one_or_none()
            return dict(data)

    @staticmethod
    def read_categories(limit: int, offset: int) -> list[dict]:
        with Session(engine) as session:
            query = select(
                CategoryModel.id,
                CategoryModel.name
            ).limit(limit).offset(offset)
            data = session.execute(query).mappings().all()
        return [dict(i) for i in data]

    @staticmethod
    def update_category(category_id: int, category_mapping: Mapping) -> dict | None:
        with Session(engine) as session:
            stmt = update(
                CategoryModel
            ).where(
                CategoryModel.id == category_id
            ).values(
                **category_mapping
            ).returning(
                CategoryModel.id,
                CategoryModel.name
            )
            data = session.execute(stmt).mappings().one_or_none()
            session.commit()
        return dict(data)

    @staticmethod
    def delete_category(category_id: int) -> None:
        with Session(engine) as session:
            stmt = delete(
                CategoryModel
            ).where(
                CategoryModel.id == category_id
            )
            session.execute(stmt)
            session.commit()
