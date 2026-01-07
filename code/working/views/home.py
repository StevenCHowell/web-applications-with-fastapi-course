import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()


@router.get("/")
# Instead of explicitly providing the template_file like this:
# @template(template_file="home/index.pt")
# the template decorater can infer it from the file name "home.py"
# and the method name "index()"
@template()
def index(user: str = "anonymous"):
    return {"user_name": user}


@router.get("/about")
@template()
def about():
    return {}
