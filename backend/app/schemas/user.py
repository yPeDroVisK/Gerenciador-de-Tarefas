# Schema representa os dados necessários , nesse caso para cadastrar o usuário

from datetime import datetime
from typing import Annotated

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    StringConstraints,
)

Name = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True, # Remove espaços do começo e final , caso houver
        min_length=1, # Mínimo de caracter
        max_length=100, # Máximo de caracter
    ),
]

class UserCreate(BaseModel):

    name:Name
    email:EmailStr
    password:str = Field(
        min_length=8,
        max_length=128,
    )

class UserResponse(BaseModel):

    id:int
    name:str
    email:EmailStr
    created_at:datetime
    updated_at:datetime

    model_config = ConfigDict(
        from_attributes=True,
    )
