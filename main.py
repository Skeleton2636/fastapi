from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.

fakedb = []

class Init(BaseModel):
    integer: int
    string: str
    float_var: float
    boolean: Optional[bool] = None

@app.get("/")
def home():
    return {"message":"Hello klhlh"}

@app.get('/page')
def get_courses():
    return fakedb

@app.get('/page/{course_id}')
def get_course_id(course_id: int):
    course = course_id - 1
    return fakedb[course]

@app.post("/page")
def add_course(course: Init):
    fakedb.append(course.dict())
    return fakedb[-1]

@app.delete("/page/{course_id}")
def delete_course(course_id: int):
    fakedb.pop(course_id-1)
    return {"Task": "Successful"}
