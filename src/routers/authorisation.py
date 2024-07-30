from fastapi import APIRouter
from src.utilities.dbutils import DButils
from src.models.registration import Registration

router = APIRouter(
    tags=["Authorisation"]
)


@router.post('/signup')
def userSignup(request:Registration):
    try:
        db = DButils()
        username = request.username
        email = request.email
        contact = request.contact
        password = request.password
        course_id = request.course_id
        user_role = request.user_role
        
    except Exception as e:
        raise e
