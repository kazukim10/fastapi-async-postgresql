from typing import Any

from fastapi import APIRouter

router = APIRouter()

@router.get(
    "/"
)
def health_check() -> Any:
    return {"connecting":"hello world"}
