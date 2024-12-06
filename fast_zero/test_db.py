from models import User, table_registry
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

def test_create_user():

    engine = create_engine('sqlite:///database.db')

    table_registry.metadata.create_all(engine)

    with Session(engine) as banco:

        user = User(username='lohan',
                    email='lohan@exemplo.com', 
                    password='senha123'
        )
    
        banco.add(user)
        banco.commit()
        banco.refresh(user)
        resultado = banco.scalar(
            select(User).where(User.email == 'lohan@exemplo.com')
        )
        
    assert user.username == 'lohan'

test_create_user()