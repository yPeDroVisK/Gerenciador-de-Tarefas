from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from ..exceptions import EmailAlreadyRegisteredError
from ..models import User
from ..repositories import add_user, get_user_by_email
from ..schemas import UserCreate
from ..security import hash_password

def register_user(
        session:Session,
        user_data:UserCreate,
) -> User:
    email = str(user_data.email).strip().lower()

    existing_user = get_user_by_email(
        session,
        email,
    )

    if existing_user is not None:
        raise EmailAlreadyRegisteredError

    user = User(
        name=user_data.name,
        email=email,
        password_hash=hash_password(user_data.password),
    )

    try:
        add_user(session, user)
        session.commit()
        session.refresh(user)

    except IntegrityError as error:
        session.rollback()
        raise EmailAlreadyRegisteredError from error

    except Exception:
        session.rollback()
        raise

    return user
