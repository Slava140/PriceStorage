from pydantic import BaseModel, Field
from models.enums import Unit


class ProductBase(BaseModel):
    name: str = Field(min_length=3)
    price: int
    unit: Unit
    category_id: int


class ProductCreateRequest(ProductBase):
    ...


class ProductCreateResponse(ProductBase):
    id: int


class ProductReadResponse(ProductBase):
    id: int


class ProductUpdateRequest(ProductBase):
    ...


class ProductUpdateResponse(ProductBase):
    id: int
