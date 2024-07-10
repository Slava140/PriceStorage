from pydantic import BaseModel, Field
from app.src.models.enums import Unit


class CategoryBase(BaseModel):
    name: str = Field(min_length=3)


class CategoryCreateRequest(CategoryBase):
    ...


class CategoryCreateResponse(CategoryBase):
    id: int


class CategoryReadResponse(CategoryBase):
    id: int


class CategoryUpdateRequest(CategoryBase):
    ...


class CategoryUpdateResponse(CategoryBase):
    id: int
