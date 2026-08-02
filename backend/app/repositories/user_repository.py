from sqlalchemy import select
from sqlalchemy.orm import Session

from ..models import User

def get_user_by_email(  # Função para achar usuário via email
        session:Session, # Conexão com o banco;
        email:str,
) -> User | None: # Retorna usuário ou vazio
    statement = select(User).where( # Ex.: SELECT *  --  FROM users  --  WHERE email = 'pedro@email.com';
        User.email == email,
    )

    return session.scalar(statement)

def add_user(
        session:Session,
        user:User,
) -> User:
    session.add(user)
    session.flush()

    return user