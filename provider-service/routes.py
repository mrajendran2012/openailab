from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import Provider, ProviderUpdate

router = APIRouter()

# Route to create a new provider in the database 
@router.post("/", response_description="Create a new provider", status_code=status.HTTP_201_CREATED, response_model=Provider)
def create_provider(request: Request, provider: Provider = Body(...)):
    provider = jsonable_encoder(provider)
    new_provider = request.app.database["provider"].insert_one(provider)
    created_provider = request.app.database["provider"].find_one(
        {"_id": new_provider.inserted_id}
    )

    return created_provider

# Route to get a provider by id
@router.get("/", response_description="List all providers", response_model=List[Provider])
def list_providers(request: Request):
    providers = list(request.app.database["provider"].find(limit=100))
    return providers

# Route to get a provider by id
@router.put("/{id}", response_description="Update a provider", response_model=Provider)
def update_provider(id: str, request: Request, provider: ProviderUpdate = Body(...)):
    provider = {k: v for k, v in provider.dict().items() if v is not None}
    if len(provider) >= 1:
        update_result = request.app.database["provider"].update_one(
            {"_id": id}, {"$set": provider}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Provider with ID {id} not found")

    if (
        existing_provider := request.app.database["provider"].find_one({"_id": id})
    ) is not None:
        return existing_provider

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Provider with ID {id} not found")

# Route to delete a provider by id
@router.delete("/{id}", response_description="Delete a provider")
def delete_provider(id: str, request: Request, response: Response):
    delete_result = request.app.database["provider"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Provider with ID {id} not found")