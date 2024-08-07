from fastapi import APIRouter,UploadFile,File,Form,HTTPException,status
from src.models.fileUpload import UploadFiles
from src.utilities.dbutils import DButils
from fastapi.responses import FileResponse
import os

router = APIRouter()

@router.post('/upload')
def fileUpload(student_id: int = Form(...),payload:UploadFile = File(...)):
    file_path = f"src/data/{payload.filename}"
    with open(file_path, "wb") as f:
        f.write(payload.file.read())
        db = DButils()
        columns = ['uploaded_path','student_id']
        values =(
            file_path,
            student_id
        )
        db.insert_query('uploadedfiles',columns,values)
    return {"filename": "success"}

@router.get('/download')
def downloadData(id):
    db = DButils()
    query = f"""select * from uploadedfiles where student_id = {id} """
    data = db.execute_query(query,True)
    if len(data)== 0:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    file_path = data[0]['uploaded_path']
    if os.path.exists(file_path):
        return FileResponse(path=file_path, filename=file_path)



            # return HTTPException(status_code=status.HTTP_200_OK)


