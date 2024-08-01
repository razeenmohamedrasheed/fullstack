from fastapi import FastAPI
from src.routers import authorisation,students,teachers
import uvicorn

app = FastAPI()


@app.get('/')
def welcome():
    return "welcome"


app.include_router(authorisation.router)
app.include_router(students.router)
app.include_router(teachers.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000,reload=True)
