from fastapi import APIRouter,HTTPException,status
from datetime import datetime, timedelta, timezone
from src.models.login import Login
from passlib.context import CryptContext
from src.utilities.dbutils import DButils
from typing import Optional
import jwt

router = APIRouter()

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

SECRET_KEY = "6dd51d6d-0ec3-4b45-a633-321782ff2f76"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


@router.post('/login')
def userLogin(request: Login):
    db = DButils()
    query = f"""select * from teachers where username = '{request.username}' """
    response = db.execute_query(query, True)

    if len(response) == 0:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    user_password = request.password
    check = pwd_context.verify(user_password, response[0]['password'])
    if not check:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    data = {
        "username": response[0]['username'],
        'userid': response[0]['teacher_id'],
        'email': response[0]['email'],
    }
    token = generateAccessToken(data)
    return token
    # generateAccessToken()
    # hashed_password = pwd_context.hash(request.password)


# def generateAccessToken(data: dict, expires_delta: Optional[timedelta]):
def generateAccessToken(data: dict, expires_delta=None):
    to_encode = data.copy()
    # if expires_delta:
    #     expire = datetime.now(timezone.utc) + expires_delta
    # else:
    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
