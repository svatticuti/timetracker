from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter

router = APIRouter()

#Local memory
# my_projects = [{ "Name": "EPIC MapRewrite", "WBSNo": "EPICMAP1", "ID" : 1}, { 
#     "Name": "EPIC SRO", "WBSNo": "EPICSRO2", "ID" : 2}]
# 
# def find_project(id):
#     for p in  my_projects:
#         if p['ID'] == id:
#             return p
# 
# def find_index_project(id):
#     for i, p in enumerate(my_projects):
#         if p['ID'] == id:
#             return i
#below code is no longer needed


# @router.post("/projectsDummy")
# async def projects(payload: dict = Body(...)):
#     print(payload)
#     return {"project": f"Name: {payload['name']} WBSNo: {payload['wbsno']}" }