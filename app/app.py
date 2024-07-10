import uvicorn
from fastapi import FastAPI
from app.src.routing.products import router as products_router
from app.src.routing.categories import router as categories_router
from app.src.database import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI(openapi_url="/core/openapi.json", docs_url="/core/docs")

app.include_router(products_router)
app.include_router(categories_router)


@app.get("/")
def main():
    ...

#
# if __name__ == '__main__':
#     uvicorn.run("app:app")
