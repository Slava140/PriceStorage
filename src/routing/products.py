from fastapi import APIRouter, status, Response
from fastapi.responses import JSONResponse

from schemas.errors import ErrorResponse
from schemas.products import (ProductCreateRequest, ProductCreateResponse,
                              ProductReadResponse,
                              ProductUpdateRequest, ProductUpdateResponse)
from depends import get_product_service

router = APIRouter(prefix="/products", tags=["products"])
service = get_product_service()


@router.post('/')
def create(product_schema: ProductCreateRequest) -> JSONResponse:
    status_code: int
    schema: ProductCreateResponse | ErrorResponse
    try:
        status_code = status.HTTP_201_CREATED
        schema = service.add_product(product_schema)
    except ValueError as error:
        status_code = status.HTTP_404_NOT_FOUND
        schema = ErrorResponse(description=str(error))
    return JSONResponse(
        status_code=status_code,
        content=schema.dict()
    )


@router.get('/{product_id}')
def read(product_id: int) -> JSONResponse:
    status_code: int
    schema: ProductReadResponse | ErrorResponse
    try:
        status_code = status.HTTP_200_OK
        schema = service.get_product(product_id)
    except ValueError as error:
        status_code = status.HTTP_404_NOT_FOUND
        schema = ErrorResponse(description=str(error))
    return JSONResponse(
        status_code=status_code,
        content=schema.dict()
    )


@router.put('/{product_id}')
def update(product_id: int, product_schema: ProductUpdateRequest) -> JSONResponse:
    status_code: int
    schema: ProductUpdateResponse | ErrorResponse
    try:
        status_code = status.HTTP_200_OK
        schema = service.update_product(product_id, product_schema)
    except ValueError as error:
        status_code = status.HTTP_404_NOT_FOUND
        schema = ErrorResponse(description=str(error))
    return JSONResponse(
        status_code=status_code,
        content=schema.dict()
    )


@router.delete('/{product_id}')
def delete(product_id: int) -> Response:
    status_code: int
    content: str | None
    try:
        service.delete_product(product_id)
        status_code = status.HTTP_204_NO_CONTENT
        content = None
    except ValueError as error:
        status_code = status.HTTP_404_NOT_FOUND
        content = ErrorResponse(description=str(error)).model_dump_json()
    return Response(
        status_code=status_code,
        content=content,
        media_type="application/json"
    )

