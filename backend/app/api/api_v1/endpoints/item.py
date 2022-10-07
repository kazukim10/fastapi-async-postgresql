from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get(
    "/",
    response_model=List[schemas.Item]
)
async def read_items(
    db: Session = Depends(deps.get_session),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve items.
    """
    
    items = await crud.item.get_multi(db, skip=skip, limit=limit)
    return items


@router.post(
    "/",
    response_model=schemas.Item
)
async def create_item(
    *,
    db: Session = Depends(deps.get_session),
    item_in: schemas.ItemCreate,
) -> Any:
    """
    Create new item.
    """
    item = await crud.item.create(db=db, obj_in=item_in)
    return item