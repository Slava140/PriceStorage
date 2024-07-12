import uvicorn
from fastapi import FastAPI
from src.routing.products import router as products_router
from src.routing.categories import router as categories_router
from src.database import Base, engine

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
