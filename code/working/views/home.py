import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()

@app.get("/")
@template(template_file="index.html")
def index(user: str = "anonymous"):
    return {"user_name": user}


@app.get("/about")
def about():
    return {}
