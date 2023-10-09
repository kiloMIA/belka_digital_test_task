from fastapi import FastAPI
from routes import auth_route, report_route
from db import engine, Base

app = FastAPI()

app.include_router(auth_route.router)
app.include_router(report_route.router)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


