from fastapi import FastAPI, Security
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import user, project, resource, auth, projectitem

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(resource.router)
app.include_router(project.router)
app.include_router(projectitem.router)

@app.get("/")
async def root():
    return {"message": "Hello there, you should not have done this."}