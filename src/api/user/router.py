from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from contexts.user.usecase.user_cmd_schema import CreateUserSchema, UpdateUserSchema
from contexts.user.usecase.user_cmd_usecase import UserCmdUsecase

from contexts.user.usecase.user_query_schema import SearchByEmailSchema
from contexts.user.usecase.user_usecase import UserUsecase

from contexts.user.domain.user_exception import EmailExistError, EmailInvalidError, PasswordWeakError, EmailNotFound

from marshmallow.exceptions import ValidationError


from contexts.shared.schemas.response_schema import ResponseErrorSchema

router = APIRouter()


@router.get("/")
async def list_webhooks():

    return {"ok"}


@router.post("/create")
async def create_user(new_user: CreateUserSchema):

    try:
        response = await UserUsecase().create_user(new_user)
        return response
    except EmailExistError as e:
        error_response = ResponseErrorSchema(success=False, message=e.message)
        return JSONResponse(content=error_response.dict(), status_code=status.HTTP_409_CONFLICT)
    except EmailInvalidError as e:
        error_response = ResponseErrorSchema(success=False, message=e.message)
        return JSONResponse(content=error_response.dict(), status_code=status.HTTP_409_CONFLICT)
    except ValidationError as e:
        # error_response = ResponseErrorSchema(success=False, message=e.messages)
        error_message = '; '.join(
            [f'{k}: {v[0]}' for k, v in e.messages.items()])
        error_response = ResponseErrorSchema(
            success=False, message=error_message)
        return JSONResponse(content=error_response.dict(), status_code=status.HTTP_409_CONFLICT)
    except PasswordWeakError as e:
        error_response = ResponseErrorSchema(success=False, message=e.message)
        return JSONResponse(content=error_response.dict(), status_code=status.HTTP_409_CONFLICT)


@router.put("/update/{user_id}")
async def update_user(user_id: str, user: UpdateUserSchema):

    try:
        response = await UserUsecase().update_user(user_id, user)
        return response
    except EmailExistError as e:
        error_response = ResponseErrorSchema(success=False, message=e.message)
        return JSONResponse(content=error_response.dict(), status_code=status.HTTP_409_CONFLICT)
    except EmailInvalidError as e:
        error_response = ResponseErrorSchema(success=False, message=e.message)
        return JSONResponse(content=error_response.dict(), status_code=status.HTTP_409_CONFLICT)
    except ValidationError as e:
        # error_response = ResponseErrorSchema(success=False, message=e.messages)
        error_message = '; '.join(
            [f'{k}: {v[0]}' for k, v in e.messages.items()])
        error_response = ResponseErrorSchema(
            success=False, message=error_message)
        return JSONResponse(content=error_response.dict(), status_code=status.HTTP_409_CONFLICT)
    except PasswordWeakError as e:
        error_response = ResponseErrorSchema(success=False, message=e.message)
        return JSONResponse(content=error_response.dict(), status_code=status.HTTP_409_CONFLICT)


@router.post("/email")
async def search_by_email(email: SearchByEmailSchema):

    try:
        return_email = await UserUsecase().search_by_email(email)
        return return_email
    except EmailNotFound as e:
        error_response = ResponseErrorSchema(success=False, message=e.message)
        return JSONResponse(content=error_response.dict(), status_code=status.HTTP_409_CONFLICT)
