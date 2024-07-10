from typing import Mapping

from sqlalchemy import select, insert, delete, update
from sqlalchemy.orm import Session

from app.src.database import engine
from app.src.models.products import Product as ProductModel


class ProductRepository:
    @staticmethod
    def is_id_exists(product_id: int) -> bool:
        with Session(engine) as session:
            query = select(ProductModel.id).where(ProductModel.id == product_id)
            result = session.execute(query).scalar_one_or_none()
            return result is not None

    @staticmethod
    def create_product(product_mapping: Mapping) -> Mapping | None:
        with Session(engine) as session:
            stmt = insert(
                ProductModel
            ).values(
                **product_mapping
            ).returning(
                ProductModel.id,
                ProductModel.name,
                ProductModel.price,
                ProductModel.unit,
                ProductModel.category_id
            )
            data = session.execute(stmt).mappings().one_or_none()
            session.commit()
        return data

    @staticmethod
    def read_product(product_id: int) -> Mapping | None:
        with (Session(engine) as session):
            query = select(
                ProductModel.id,
                ProductModel.name,
                ProductModel.price,
                ProductModel.unit,
                ProductModel.category_id
            ).where(
                ProductModel.id == product_id
            )
            return session.execute(query).mappings().one_or_none()

    @staticmethod
    def update_product(product_id: int, product_mapping: Mapping) -> Mapping | None:
        with Session(engine) as session:
            stmt = update(
                ProductModel
            ).where(
                ProductModel.id == product_id
            ).values(
                **product_mapping
            ).returning(
                ProductModel.id,
                ProductModel.name,
                ProductModel.price,
                ProductModel.unit,
                ProductModel.category_id,
            )
            data = session.execute(stmt).mappings().one_or_none()
            session.commit()
        return data

    @staticmethod
    def delete_product(product_id: int) -> None:
        with Session(engine) as session:
            stmt = delete(
                ProductModel
            ).where(
                ProductModel.id == product_id
            )
            session.execute(stmt)
            session.commit()
