from http import HTTPStatus
from fastapi import FastAPI
from schemas import Message, UserSchema, UserPublic

app = FastAPI()

@app.get('/mensagem', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'mensagem': 'olá'}

@app.post('/users/', response_model= UserPublic)
def create_user(user: UserSchema):
    return user
