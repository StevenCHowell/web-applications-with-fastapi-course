import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

from viewmodels.home.index_viewmodel import IndexViewModel

router = fastapi.APIRouter()


# Instead of explicitly providing the template_file like this:
# @template(template_file="home/index.pt")
# the template decorator can infer it from the file name "home.py"
# and the method name "index()"
@router.get("/")
@template()
def index(request: Request):
    vm = IndexViewModel(request)
    return vm.to_dict()


@router.get("/about")
@template()
def about():
    return {}
