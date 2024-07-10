from app.src.repositories.categories import CategoryRepository
from app.src.services.categories import CategoryService

from app.src.repositories.products import ProductRepository
from app.src.services.products import ProductService

product_repository = ProductRepository()
product_service = ProductService(product_repository)

category_repository = CategoryRepository()
category_service = CategoryService(category_repository)


def get_product_service() -> ProductService:
    return product_service


def get_category_service() -> CategoryService:
    return category_service
