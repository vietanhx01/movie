from fastapi import APIRouter
from model.user import User as UserModel
from schemas import User as UserSchema

router = APIRouter()

@router.get("/")
def users():
    return UserModel.get_users()

@router.post("/")
def add_user(user: UserSchema):
    new_user = UserModel.add_user(user.dict())
    return new_user.id

@router.delete("/{user_id}")
def delete_user(user_id):
    delete_rows = UserModel.delete_user(user_id)
    if delete_rows == 0:
        return False
    return True