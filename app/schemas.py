from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

# Test
class Movie_Create(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    year: int = Field(ge=1888, le=2100)
    genre: str = Field(min_length=1, max_length=100)

class Movie_Update(BaseModel):
    title: Optional[str] = Field(default=None,min_length=1, max_length=200)
    year: Optional[int] = Field(default=None,ge=1888, le=2100)
    genre: Optional[str] = Field(default=None,min_length=1, max_length=100)

class Movie_Out(BaseModel):
    id: int
    title: str
    year:Optional[int]
    genre: Optional[str]
    model_config = ConfigDict(from_attributes=True)
