from typing import Optional

from pydantic import BaseModel, Field



class UserCreateSchema(BaseModel):
    name: Optional[str] = Field(..., min_length=1)
    age: Optional[int] = Field(None, gt=0)


class UserUpdateSchema(BaseModel):
    age: Optional[int] = Field(None, gt=0)


class UserPatchSchema(BaseModel):
    name: Optional[str] = Field(..., min_length=1)
    age: Optional[int] = Field(None, gt=0)
