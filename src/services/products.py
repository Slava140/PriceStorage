from typing import List

from pydantic import ValidationError

from repositories.products import ProductRepository
from repositories.categories import CategoryRepository
from schemas.products import (ProductCreateRequest, ProductCreateResponse,
                              ProductReadResponse,
                              ProductUpdateRequest, ProductUpdateResponse,)

"""
Тут должна быть бизнес-логика
"""


class ProductService:
    def __init__(self, repository: ProductRepository) -> None:
        self.repository = repository

    def get_product(self, product_id: int) -> ProductReadResponse:
        if not self.repository.is_id_exists(product_id):
            raise ValueError(f"The product with id {product_id} was not found")
        else:
            response_data = self.repository.read_product(product_id)
            return ProductReadResponse(**response_data)

    def add_product(self, product_schema: ProductCreateRequest) -> ProductCreateResponse:
        category_id = product_schema.category_id
        if not CategoryRepository.is_id_exists(category_id):
            raise ValueError(f"The category with id {category_id} was not found")
        else:
            response_data = self.repository.create_product(product_schema.dict())
            return ProductCreateResponse(**response_data)

    def update_product(self, product_id: int, product_schema: ProductUpdateRequest) -> ProductUpdateResponse:
        category_id = product_schema.category_id
        if not self.repository.is_id_exists(product_id):
            raise ValueError(f"The product with id {product_id} was not found")
        elif not CategoryRepository.is_id_exists(category_id):
            raise ValueError(f"The category with id {category_id} was not found")
        else:
            response_data = self.repository.update_product(product_id, product_schema.dict())
            return ProductUpdateResponse(**response_data)

    def delete_product(self, product_id: int) -> None:
        if not self.repository.is_id_exists(product_id):
            raise ValueError(f"The product with id {product_id} was not found")
        else:
            self.repository.delete_product(product_id)
