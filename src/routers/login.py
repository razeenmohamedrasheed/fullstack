from fastapi import APIRouter,HTTPException,status
from src.models.login import Login
from passlib.context import CryptContext
from src.utilities.dbutils import DButils

router = APIRouter()

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


@router.post('/login')
def userLogin(request: Login):
    db = DButils()
    query = f"""select * from teachers where username = '{request.username}' """
    response = db.execute_query(query,True)
    if len(response)==0:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    user_password = request.password
    check = pwd_context.verify(user_password,response[0]['password'])
    if not check:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    # hashed_password = pwd_context.hash(request.password)
