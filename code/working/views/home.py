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
    return {
        "package_count": 280_000,
        "release_count": 2_234_567,
        "user_count": 78_910,
        "packages": [
            {"id": "numpy", "summary": "The best numerical Python package."},
            {"id": "fastapi", "summary": "A great web framework."},
            {"id": "uvicorn", "summary": "Your favorite ASGI server."},
            {"id": "httpx", "summary": "Requests for the async world."},
        ],
    }


@router.get("/about")
@template()
def about():
    return {}
