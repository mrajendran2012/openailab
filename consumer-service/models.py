import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Consumer(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    username: str = Field(...)
    password: str = Field(...)
    email: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "username": "consumer1_username",
                "password": "consumer1_password",
                "email": "..."
            }
        }

class ConsumerUpdate(BaseModel):
    username: Optional[str]
    password: Optional[str]
    email: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "username": "consumer1_username",
                "password": "consumer1_password",
                "email": "consumer1@lifeplore.com"
            }
        }