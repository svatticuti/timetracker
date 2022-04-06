from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter

router = APIRouter(
    prefix="/resources",
    tags=['Resources']
)

@router.get("/")
async def resources():
    return {"message": "Get Resources!!"}

@router.get("/{id}")
async def get_resource():
    return {"message": "Get One Resources!!"}

@router.post("/")
async def create_resource():
    return {"message": "Post Resources!!"}

@router.put("/{id}")
async def update_resources():
    return {"message": "Update Resources!!"}

@router.delete("/{id}")
async def delete_resources():
    return {"message": "Delete Resources!!"}