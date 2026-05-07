from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field


class DogBase(SQLModel):
    name: str
    size: str
    dangerous: bool
    sterilized: bool
    breed: str


class Dog(DogBase, table=True):
    __tablename__ = "dogs"

    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    created: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False
    )


class DogCreate(DogBase):
    pass


class DogUpdate(SQLModel):
    name: Optional[str] = None
    size: Optional[str] = None
    dangerous: Optional[bool] = None
    sterilized: Optional[bool] = None
    breed: Optional[str] = None