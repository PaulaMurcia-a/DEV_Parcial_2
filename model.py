from datetime import datetime, timezone
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

    id: Optional[int] = Field(default=None, primary_key=True)
    created: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
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



class BookBase(SQLModel):
    name: str
    author: str
    pages: int
    available: bool
    language: str


class Book(BookBase, table=True):
    __tablename__ = "books"

    id: Optional[int] = Field(default=None, primary_key=True)
    created: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        nullable=False
    )


class BookCreate(BookBase):
    pass


class BookUpdate(SQLModel):
    name: Optional[str] = None
    author: Optional[str] = None
    pages: Optional[int] = None
    available: Optional[bool] = None
    language: Optional[str] = None


# ─────────────────────────────────────────
#  STICKER
# ─────────────────────────────────────────

class StickerBase(SQLModel):
    name: str
    package: str
    hologram: bool
    obtained: bool
    size: str


class Sticker(StickerBase, table=True):
    __tablename__ = "stickers"

    id: Optional[int] = Field(default=None, primary_key=True)
    created: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        nullable=False
    )


class StickerCreate(StickerBase):
    pass


class StickerUpdate(SQLModel):
    name: Optional[str] = None
    package: Optional[str] = None
    hologram: Optional[bool] = None
    obtained: Optional[bool] = None
    size: Optional[str] = None