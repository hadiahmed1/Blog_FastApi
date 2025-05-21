from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/blog") #fetch all blogs
def bloglist(limit=2, published: bool=False, sort: Optional[str]=None): #limit from query params
    if published:
        return {'data':f'{limit} published blogs list'}
    return {'data':f'{limit} blogs list'}

@app.get("/blog/{blog_id}") #fetch blog with id= blog_id
def getBlog(blog_id : int):
    return {"data": {"blog":blog_id}}

@app.get("/blog/{blog_id}/comments") #comments on blog with id= blog_id
def getBlog(blog_id : int):
    return {"data": {"blog":str(blog_id)+": comments"}}