from fastapi import APIRouter,status
from src.utilities.dbutils import DButils

router = APIRouter(
    tags=["teachers"]
)


@router.get('/listTeachers',status_code=status.HTTP_200_OK)
def listAllTeachers():
    db = DButils()
    response = db.select_query('teachers')
    return {
        "message":'success',
        "data": response
    }
