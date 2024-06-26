import time

from fastapi import APIRouter, status, Response, HTTPException
from starlette.responses import JSONResponse

from schemas.categories import CategoryCreateRequest, CategoryUpdateRequest
from depends import get_category_service

router = APIRouter(prefix="/categories", tags=["categories"])
service = get_category_service()


@router.post('/')
def create(category_schema: CategoryCreateRequest) -> JSONResponse:
    result_json = service.add_category(category_schema)
    return JSONResponse(
        status_code=201,
        content=result_json
    )


@router.get('/{category_id}')
def read(category_id: int) -> JSONResponse:
    result_json = service.get_category(category_id)
    try:
        return JSONResponse(
            status_code=200,
            content=result_json
        )
    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Something went wrong"
        )


@router.get('/')
def read_all(limit: int = 10, page: int = 0) -> JSONResponse:
    try:
        return JSONResponse(
            status_code=200,
            content={"categories": service.get_categories(limit, page)}
        )
    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Something went wrong"
        )


@router.put('/{category_id}')
def update(category_id: int, category_schema: CategoryUpdateRequest) -> JSONResponse:
    try:
        return JSONResponse(
            status_code=200,
            content=service.update_category(category_id, category_schema)
        )
    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.delete('/{category_id}')
def delete(category_id: int) -> Response:
    try:
        service.delete_category(category_id)
        return Response(status_code=204)
    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )
