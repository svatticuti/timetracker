from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import models, schemas, oauth2
from ..database import engine, get_db

router = APIRouter(
    prefix="/projects",
    tags=['Projects']
)

@router.get("/", response_model=List[schemas.Project])
async def projects(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),
limit: int = 10, skip: int = 0, search: Optional[str] = ""):
#    cursor.execute("""SELECT * FROM Projects""")
#    projects = cursor.fetchall()
    projects = db.query(models.Project).filter(models.Project.name.contains(search)).limit(limit).offset(skip).all()
    # return {"data": projects}
    return projects

@router.get("/{id}", response_model=schemas.Project)
async def get_project(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""SELECT * FROM Projects WHERE "ID" = %s """, (str(id),))
    # project = cursor.fetchone()
    project = db.query(models.Project).filter(models.Project.id == id).first()
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Project with ID: {id} was not found")
    # return {"data": project}
    return project

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Project)
async def create_projects(project: schemas.ProjectCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""INSERT INTO Projects ("Name", "CostsID", "Budget", "PlannedStartDate", "PlannedEndDate", "Code") VALUES (%s, %s, %s, %s, %s, %s) RETURNING * """, 
    # (project.Name, project.CostsID, project.Budget, project.PlannedStartDate, project.PlannedEndDate, project.Code))
    # new_project = cursor.fetchone()
    # conn.commit()
    #**will unpack the pydantic model data into dictionary

    new_project = models.Project(created_by=current_user.id, **project.dict())
    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    # return {"new_project": new_project }
    return new_project
    

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(id:int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    # cursor.execute("""DELETE FROM Projects where "ID" = %s RETURNING * """, (str(id),))
    # delete_project = cursor.fetchone()
    # conn.commit()
    project_query = db.query(models.Project).filter(models.Project.id == id)

    project = project_query.first()

    if project == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Project with ID: {id} was not found")
    if project.created_by != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail=f"Not authorized to perform requested action")

    project_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=schemas.Project)
async def update_project(id:int, update_project: schemas.ProjectCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    # cursor.execute("""UPDATE Projects SET "Name" = %s, "CostsID" = %s, "Budget" = %s, "PlannedStartDate" = %s, "PlannedEndDate" = %s, "ActualStartDate" = %s, "ActualEndDate" = %s, "Code"= %s where "ID" = %s RETURNING * """, 
    # (project.Name, project.CostsID, project.Budget, project.PlannedStartDate, project.PlannedEndDate, project.ActualStartDate, project.ActualStartDate, project.Code, str(id),))
    # updated_project = cursor.fetchone()
    # conn.commit()
    project_query = db.query(models.Project).filter(models.Project.id == id)
    project = project_query.first()

    if project == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Project with ID: {id} was not found")
    
    if project.created_by != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail=f"Not authorized to perform requested action")

    project_query.update(update_project.dict(), synchronize_session=False)
    db.commit()
    # return {"data": project_query.first()}
    return project_query.first()