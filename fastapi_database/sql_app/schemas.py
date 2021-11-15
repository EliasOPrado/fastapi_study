from typing import List, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

# inherits from ItemBase
class ItemCreate(ItemBase):
    pass

# inherits from ItemBase not ItemCreate
class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str

# inherits from UserBase
class UserCreate(UserBase):
    password: str

# inherits from UserBase not UserCreate
class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        # orm_mode that gives the migration..
        orm_mode = True