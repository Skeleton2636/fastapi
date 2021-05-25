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

@app.get('/page/{integer}')
def get_course_id(integer: int):
    course = integer - 1
    return fakedb[course]

@app.post("/page")
def add_course(item: Init):
    fakedb.append(item.dict())
    return fakedb[-1]

@app.delete("/page/{integer}")
def delete_course(integer: int):
    fakedb.pop(integer-1)
    return {"Task": "Successful"}
