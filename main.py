from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from src.routes.index_route import router as index_router
from src.routes.user_route import router as user_router
from src.routes.material_route import router as material_router
from src.routes.purchase_route import router as purchase_router
from src.routes.order_route import router as order_router
from src.routes.truck_route import router as truck_router

app = FastAPI()

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

origins = ["http://localhost", "http://localhost:4200"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(index_router)
app.include_router(user_router)
app.include_router(material_router)
app.include_router(purchase_router)
app.include_router(truck_router)
app.include_router(order_router)
