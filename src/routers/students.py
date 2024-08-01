from fastapi import APIRouter,status
from src.utilities.dbutils import DButils

router = APIRouter(
    tags=["Students"]
)


@router.get('/listStudents',status_code=status.HTTP_200_OK)
def listAllStudents():
    db = DButils()
    response = db.select_query('students')
    return {
        "message":'success',
        "data": response
    }
