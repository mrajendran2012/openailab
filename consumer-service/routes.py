from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import Consumer, ConsumerUpdate

router = APIRouter()

# Route to create a new consumer in the database 
@router.post("/", response_description="Create a new consumer", status_code=status.HTTP_201_CREATED, response_model=Consumer)
def create_consumer(request: Request, consumer: Consumer = Body(...)):
    consumer = jsonable_encoder(consumer)
    new_consumer = request.app.database["consumer"].insert_one(consumer)
    created_consumer = request.app.database["consumer"].find_one(
        {"_id": new_consumer.inserted_id}
    )

    return created_consumer

# Route to get a consumer by id
@router.get("/", response_description="List all consumers", response_model=List[Consumer])
def list_consumers(request: Request):
    consumers = list(request.app.database["consumer"].find(limit=100))
    return consumers

# Route to get a consumer by id
@router.put("/{id}", response_description="Update a consumer", response_model=Consumer)
def update_consumer(id: str, request: Request, consumer: ConsumerUpdate = Body(...)):
    consumer = {k: v for k, v in consumer.dict().items() if v is not None}
    if len(consumer) >= 1:
        update_result = request.app.database["consumer"].update_one(
            {"_id": id}, {"$set": consumer}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Consumer with ID {id} not found")

    if (
        existing_consumer := request.app.database["consumer"].find_one({"_id": id})
    ) is not None:
        return existing_consumer

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Consumer with ID {id} not found")

# Route to delete a consumer by id
@router.delete("/{id}", response_description="Delete a consumer")
def delete_consumer(id: str, request: Request, response: Response):
    delete_result = request.app.database["consumer"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Consumer with ID {id} not found")