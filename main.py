from fastapi import FastAPI
from src.routers import authorisation, students, teachers, login ,fileupload
import uvicorn

app = FastAPI()


@app.get('/')
def welcome():
    return "welcome"


app.include_router(authorisation.router)
app.include_router(students.router)
app.include_router(teachers.router)
app.include_router(login.router)
app.include_router(fileupload.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8002, reload=True)
