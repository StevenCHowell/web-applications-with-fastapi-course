import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()


@router.get("/account")
@template()
def index():
    return {}


@router.get("/account/register")
@template()
def register():
    return {}


@router.get("/account/login")
@template()
def login():
    return {}


@router.get("/account/logout")
@template()
def logout():
    return {}
