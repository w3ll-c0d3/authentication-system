from sqlmodel import SQLModel, Field
from sqlalchemy.orm import validates
from sqlalchemy import Column, String
from typing import Optional
from uuid import UUID
import re



class UserBase(SQLModel):
    cpf: str
    username: str
    password: str
    first_name: str
    last_name: str
    age: int

    @validates('cpf')
    def validate_cpf(self, key, value):
        valid_cpf = r'^(\d){11}$'
        result = re.match(valid_cpf, value)
        if not result:
            raise ValueError("Invalid CPF.")
        return value
    
    
class User(UserBase, table=True):
    cpf: str = Field(sa_column=Column("cpf", String(11), unique=True))
    username: str = Field(sa_column=Column("username", String, unique=True)) 
    password: str
    first_name: str
    last_name: str
    age: int
    id: Optional[UUID] = Field(default=None, primary_key=True)

class UserCreate(UserBase):
    pass

class LogIn(SQLModel):
    username: str
    password: str

class UserUpdate(SQLModel):
    cpf: Optional[str]
    username: Optional[str]
    password: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    age: Optional[int]


