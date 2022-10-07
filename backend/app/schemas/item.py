from typing import Optional

from pydantic import BaseModel


# Shared properties
class TutorialBase(BaseModel):
    name: Optional[str] = None


# Properties to receive on item creation
class TutorialCreate(TutorialBase):
    name: str


# Properties to receive on item update
class TutorialUpdate(TutorialBase):
    pass


# Properties shared by models stored in DB
class TutorialInDBBase(TutorialBase):
    tutorial_id: int
    name: str

    class Config:
        orm_mode = True


# Properties to return to client
class Tutorial(TutorialInDBBase):
    pass


# Properties properties stored in DB
class TutorialInDB(TutorialInDBBase):
    pass