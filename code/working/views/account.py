import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()

@app.get("/account")
def index():
    return {}


@app.get("/account/register")
def register():
    return {}


@app.get("/account/login")
def login():
    return {}


@app.get("/account/logout")
def logout():
    return {}
