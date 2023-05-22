from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel



app = FastAPI()


@app.get("/blog")  # decorator

def fetch_blog(limit, published: bool, sort: Optional[str] = None):
    
    if published:
        return {'data': f'{limit} Published Blogs from the database'}
    else:
        return {'data': f'{limit} All the Blogs from the database'}



@app.get("/show/{blog_id}")

def show_blog(blog_id : int):
    return {"data": blog_id}


@app.get("/show/{blog_id}/comments")

def show_comments(blog_id):
    return {"data": {"1", "2"}}



class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]
    



@app.post("/blog")
def create_blog(blog: Blog):
 
    return {"data": f"Blog is created successfully as title is {blog.title}"}

