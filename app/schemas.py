from itertools import count
from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional

#pydantic model
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    create_at: datetime
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str]

class ProjectBase(BaseModel):
    name: str
    costs_id: str
    budget: float
    planned_start_date: date
    planned_end_date: date
    actual_start_date: Optional[date]
    actual_end_date: Optional[date]
    code: Optional[str]

    class Config:
        orm_mode = True

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    create_at: datetime
    created_by: int
    created: UserOut

class ProjectItemCount(BaseModel):
    Project: Project
    count: int
    
    class Config:
        orm_mode = True

class ProjectItemBase(BaseModel):
    project_id: int
    item_no: int
    description: str
    parent_item_no: Optional[int]
    resource_id: Optional[int]
    start_date: Optional[date]
    end_date: Optional[date]
    assigned_hours: Optional[float]
    skill_id: Optional[str]
    dependency_item_no: Optional[int]
    class Config:
        orm_mode = True

class ProjectItemCreate(ProjectItemBase):
    pass

class ProjectItem(ProjectItemBase):
    # status: Optional[str]
    # hierarchy: Optional[int]
    create_at: datetime
    created_by: int

class ResourceBase(BaseModel):
    id: int
    user_id: Optional[int]
    identification: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    created_at: int
    start_date: Optional[date]
    end_date: Optional[date]
    role_id: int

class Resource(ResourceBase):
    pass