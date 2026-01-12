import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

from viewmodels.account.index_viewmodel import IndexViewModel
from viewmodels.account.login_viewmodel import LoginViewModel
from viewmodels.account.register_viewmodel import RegisterViewModel
from viewmodels.shared.viewmodel import ViewModelBase

router = fastapi.APIRouter()


@router.get("/account")
@template()
def index(request: Request):
    vm = IndexViewModel(request)
    return vm.to_dict()


@router.get("/account/register")
@template()
def register(request: Request):
    vm = RegisterViewModel(request)
    return vm.to_dict()


@router.get("/account/login")
@template()
def login(request: Request):
    vm = LoginViewModel(request)
    return vm.to_dict()


@router.get("/account/logout")
@template()
def logout(request: Request):
    vm = ViewModelBase(request)
    # TODO: Use this vm
    return vm.to_dict()  # TODO: replace this return value
