from datetime import date
from enum import unique
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Date, Float, TIMESTAMP,text
from sqlalchemy.sql.expression import null
from sqlalchemy.orm import relationship
from .database import Base

#sqlalchemy model
# table names are case sensitive     
class Skill(Base):
    __tablename__ = "skill"

    id = Column(Integer, primary_key=True, nullable=False)
    skill = Column(String, nullable=True)

class ResourceRole(Base):
    __tablename__ = "resourcerole"

    id = Column(Integer, primary_key=True, nullable=False)
    role = Column(String, nullable=True)

class SignOff(Base):
    __tablename__ = "signoff"

    id = Column(Integer, primary_key=True, nullable=False)
    sign_off = Column(String, nullable=True)

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    create_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class ResourceSkill(Base):
    __tablename__ = "resourceskill"

    resource_id = Column(Integer, ForeignKey("resource.id"), primary_key=True, nullable=False)
    skill_id = Column(Integer, ForeignKey("skill.id"), primary_key=True, nullable=False)

class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    costs_id = Column(String, nullable=False)
    budget = Column(Float, nullable=True) 
    planned_start_date = Column(Date, nullable=True)
    planned_end_date = Column(Date, nullable=True)
    actual_start_date = Column(Date, nullable=True)
    actual_end_date = Column(Date, nullable=True)
    code = Column(String, nullable=True)
    create_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    created_by = Column(Integer, ForeignKey("user.id"), nullable=False)

    # Below code doesn't update anything in the database, this just allows us to get the foreign relation data, 
    # notice User starts with Capital U, this is model name and not database table name
    created = relationship("User")    

class ProjectItem(Base):
    __tablename__ = "projectitem"

    project_id = Column(Integer, ForeignKey("project.id"), primary_key=True, nullable=False)
    item_no = Column(Integer, primary_key=True, nullable=False)
    description = Column(String, nullable=False)
    status = Column(String, nullable=True)
    parent_item_no = Column(Integer, nullable=True)
    hierarchy = Column(Integer, nullable=True)
    drill_status = Column(String, nullable=True)
    resource_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    assigned_hours = Column(Float, nullable=True) 
    skill_id = Column(String, nullable=True)
    dependency_item_no = Column(Integer, nullable=True)
    create_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    created_by = Column(Integer, ForeignKey("user.id"), nullable=False)

class Resource(Base):
    __tablename__ = "resource"

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False, unique=True)
    identification =  Column(String, nullable=False, unique=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    role_id = Column(Integer, ForeignKey("resourcerole.id"), nullable=False)
#     location = Column(String, nullable=True)
#     "team_lead_id" integer,

class ResourceTimeLog(Base):
    __tablename__ = "resourcetimelog"

    project_id = Column(Integer, primary_key=True, nullable=False)
    project_item_no = Column(Integer, primary_key=True, nullable=False)
    resource_id = Column(Integer, primary_key=True, nullable=False)
    date = Column(Date, primary_key=True, nullable=False)
    hours_worked = Column(Float, nullable=False)
    status = Column(String, nullable=True)
    notes = Column(String, nullable=True)

class ProjectStakeHolder(Base):
    __tablename__ = "projectstakeholder"

    project_id = Column(Integer, ForeignKey("project.id"), primary_key=True, nullable=False)
    resource_id = Column(Integer, ForeignKey("resource.id"), primary_key=True, nullable=False)
    resource_role_id = Column(Integer, ForeignKey("resourcerole.id"), primary_key=True, nullable=False)
    sign_off_id = Column(Integer, ForeignKey("signoff.id"), primary_key=True, nullable=False)
