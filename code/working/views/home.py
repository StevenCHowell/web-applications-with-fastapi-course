import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

from viewmodels.home.indexviewmodel import IndexViewModel

router = fastapi.APIRouter()


@router.get("/")
# Instead of explicitly providing the template_file like this:
# @template(template_file="home/index.pt")
# the template decorater can infer it from the file name "home.py"
# and the method name "index()"
@template()
def index(request: Request):
    vm = IndexViewModel(request)
    return vm.to_dict()


@router.get("/about")
@template()
def about():
    return {}
