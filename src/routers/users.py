from fastapi import APIRouter
from database import get_user_by_name, get_user_names, add_user

router = APIRouter(prefix='/users')

@router.get("/greet/{name}")
async def greets(name: str):
    if not isinstance(name, str):
        raise TypeError('Введите строковое значение')
    user = await get_user_by_name(name)
    if user:
        return {"Уже виделись": name.capitalize()}
    else:
        await add_user(name)
        return {"Hello": name.capitalize()}
    

@router.get("/get_all_names")
async def get_names():
    users = await get_user_names()
    return {"users": users}