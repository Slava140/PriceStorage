from typing import Mapping

from repositories.categories import CategoryRepository
from schemas.categories import CategoryCreateRequest, CategoryUpdateRequest

"""
Тут должна быть бизнес-логика
"""


class CategoryService:
    def __init__(self, repository: CategoryRepository) -> None:
        self.repository = repository

    def get_categories(self, limit: int, page: int) -> list[Mapping]:
        result_data = self.repository.read_categories(limit, page*limit)
        if result_data:
            return result_data
        else:
            raise ValueError(f"The categories were not found")

    def get_category(self, category_id: int) -> Mapping:
        if not self.repository.is_id_exists(category_id):
            raise ValueError(f"The category with id {category_id} was not found")
        else:
            return self.repository.read_category(category_id)

    def add_category(self, category_schema: CategoryCreateRequest) -> dict:
        return dict(
            self.repository.create_category(category_schema.dict())
        )

    def update_category(self, category_id: int, category_schema: CategoryUpdateRequest) -> dict:
        if not self.repository.is_id_exists(category_id):
            raise ValueError(f"The category with id {category_id} was not found")
        else:
            return self.repository.update_category(category_id, category_schema.dict())

    def delete_category(self, category_id: int) -> None:
        if not self.repository.is_id_exists(category_id):
            raise ValueError(f"The category with id {category_id} was not found")
        else:
            self.repository.delete_category(category_id)
