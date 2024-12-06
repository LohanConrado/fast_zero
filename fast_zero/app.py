from http import HTTPStatus
from fastapi import FastAPI, HTTPException
from schemas import (Message, UserSchema, UserPublic, UserDB, UserList)

app = FastAPI()

database = []

@app.get('/mensagem', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'mensagem': 'olá'}

@app.post('/users/', status_code=HTTPStatus.OK, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(
        id=len(database) + 1,
        #model_dump() converte em dicionário
        # **user
        **user.model_dump()
    )

    database.append(user_with_id)

    return user_with_id

@app.get('/users/', response_model = UserList)
def read_users():
    return {'users': database}

@app.put('/users/{user_id}', status_code= HTTPStatus.OK, response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=user_id)

    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado'
            )
        
    database[user_id - 1] = user_with_id
    return user_with_id

@app.delete('/users/{user_id}', status_code= HTTPStatus.OK, response_model=Message)
def delete_user(user_id: int):
    
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado'
        )
    del database[user_id - 1]
    return {'message' : 'Usuário deletado'}

@app.get('/user/{user_id}', status_code= HTTPStatus.OK, response_model=UserSchema)
def read_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail= 'usuário não encontrado'
            )

    return database[user_id - 1]
