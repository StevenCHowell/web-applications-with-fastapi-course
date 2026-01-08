from typing import List


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
