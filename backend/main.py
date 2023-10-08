from fastapi import FastAPI
from routes import auth_route, report_route

app = FastAPI()

app.include_router(auth_route.router)
app.include_router(report_route.router)





