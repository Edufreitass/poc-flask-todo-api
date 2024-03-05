from pydantic import BaseModel, Field
from typing import Optional


class PostCreateSchema(BaseModel):
    title: Optional[str] = Field(..., min_length=1)
    body: Optional[str] = Field(..., )
    user_id: int = Field(..., )


class PostUpdateSchema(BaseModel):
    title: Optional[str] = Field(None, max_length=255)
    body: Optional[str] = None
    user_id: Optional[int] = None
