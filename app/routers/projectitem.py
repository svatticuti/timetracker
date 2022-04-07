from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from typing import List, Optional
from .. import schemas, models, oauth2
from ..database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import func

router = APIRouter(
    prefix="/projectitem",
    tags=['ProjectItem']
)

@router.get("/", response_model=List[schemas.ProjectItemCount])
async def projectitem(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),
limit: int = 10, skip: int = 0, search: Optional[str] = ""):

    result = db.query(models.Project, func.count(models.ProjectItem.project_id).label("count")).join(
        models.ProjectItem, models.ProjectItem.project_id == models.Project.id, isouter=True).group_by(models.Project.id).filter(
            models.Project.name.contains(search)).limit(limit).offset(skip).all()
    
    return result
    

@router.get("/{id}")
async def get_projectitem():

    return {"message": "Get One projectitem!!"}

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ProjectItem)
async def create_projectitem(projectitem: schemas.ProjectItemCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    new_projectitem = models.ProjectItem(created_by=current_user.id, **projectitem.dict())
    db.add(new_projectitem)
    db.commit()
    db.refresh(new_projectitem)
    print(new_projectitem)
    return new_projectitem


@router.put("/{id}")
async def update_projectitem():
    return {"message": "Update projectitem!!"}

@router.delete("/{id}")
async def delete_projectitem():
    return {"message": "Delete projectitem!!"}