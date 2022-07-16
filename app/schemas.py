import email
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class ArticleBase(BaseModel):
    title: str
    body: Optional[str] = None

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: EmailStr

    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    name: str
    email: str
    articles: List[ArticleBase] = []

    class Config:
        orm_mode = True


class ArticleCreate(ArticleBase):
    pass


class Article(ArticleBase):
    id: int
    author_id: int
    author: UserBase
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class ArticleUpdate(BaseModel):
    title: Optional[str]
    body: Optional[str]

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    articles: List[Article] = []

    class Config:
        orm_mode = True


class CommentBase(BaseModel):
    title: str
    body: Optional[str]


class CommentCreate(CommentBase):
    author: User


class Comment(CommentBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True
