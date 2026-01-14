import datetime
from typing import List, Optional

from data.package import Package
from data.release import Release


def package_count() -> int:
    return 280_000


def release_count() -> int:
    return 2_345_678


def latest_releases(limit: int = 5) -> List:
    packages = [
        {"id": "numpy", "summary": "Numerical Python package."},
        {"id": "fastapi", "summary": "A great web framework."},
        {"id": "uvicorn", "summary": "Your favorite ASGI server."},
        {"id": "httpx", "summary": "Requests for the async world."},
    ]
    return packages[:limit]


def get_package_by_id(package_name: str) -> Optional[Package]:
    package = Package(
        package_name,
        "This is he summary",
        "Full details here!",
        "https://fastapi.tiangolo.com/",
        "MIT",
        "Sebastian Ramirez",
    )
    return package


def get_latest_release_for_package(package_name: str) -> Optional[Release]:
    release = Release("1.42.0", datetime.datetime.now())
    return release
