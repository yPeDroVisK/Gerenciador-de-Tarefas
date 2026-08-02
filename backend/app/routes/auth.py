from fastapi import APIRouter, HTTPException, status

from ..dependencies import DatabaseSession
from ..exceptions import EmailAlreadyRegisteredError
from ..schemas import UserCreate, UserResponse
from ..services import register_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)

def register(
    user_data:UserCreate,
    session:DatabaseSession,
) -> UserResponse:
    try:
        user = register_user(
            session=session,
            user_data=user_data,
        )

    except EmailAlreadyRegisteredError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="E-mail já cadastrado.",
        ) from error

    return user