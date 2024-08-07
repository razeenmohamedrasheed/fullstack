from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile


class UploadFiles(BaseModel):
    student_id: int
