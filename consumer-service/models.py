import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Consumer(BaseModel):
    #id: str = Field(default_factory=uuid.uuid4, alias="_id")
    ConsumerId: str = Field(default_factory=uuid.uuid4, alias="_id")  # Will be primary key in database
    FirstName: str = Field(...)
    MiddleName: Optional[str]
    LastName: str = Field(...)
    PreferredFirstName: Optional[str]
    PreferredMiddleName: Optional[str]
    PreferredLastName: Optional[str]
    DateOfBirth: Optional[str]
    Address1: Optional[str]
    Address2: Optional[str]
    City: Optional[str]
    State: Optional[str]
    Country: Optional[str]
    ZipCode: Optional[str]
    Email: str = Field(...)
    Phone: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "ConsumerId": "066de609-b04a-4b30-b46c-32537c7f1f6e",  # Will be primary key in database
                "FirstName": "John",
                "MiddleName": "...", 
                "LastName": "Doe",  
                "PreferredFirstName": "...",
                "PreferredMiddleName": "...",
                "PreferredLastName": "...",
                "DateOfBirth": "...",
                "Address1": "...",
                "Address2": "...",
                "City": "...", 
                "State": "...",
                "Country": "...",
                "ZipCode": "...",
                "Email": "john.doe@lifeplore.com",
                "Phone": "7321234567" 
            }
        }

class ConsumerUpdate(BaseModel):
    FirstName: Optional[str]
    MiddleName: Optional[str]
    LastName: Optional[str]
    PreferredFirstName: Optional[str]
    PreferredMiddleName: Optional[str]
    PreferredLastName: Optional[str]
    DateOfBirth: Optional[str]
    Address1: Optional[str]
    Address2: Optional[str]
    City: Optional[str]
    State: Optional[str]
    Country: Optional[str]
    ZipCode: Optional[str]
    Email: Optional[str]
    Phone: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "ConsumerId": "066de609-b04a-4b30-b46c-32537c7f1f6e",  # Will be primary key in database
                "FirstName": "John",
                "MiddleName": "...", 
                "LastName": "Doe",  
                "PreferredFirstName": "...",
                "PreferredMiddleName": "...",
                "PreferredLastName": "...",
                "DateOfBirth": "...",
                "Address1": "...",
                "Address2": "...",
                "City": "...", 
                "State": "...",
                "Country": "...",
                "ZipCode": "...",
                "Email": "john.doe@lifeplore.com",
                "Phone": "7321234567" 
            }
        }