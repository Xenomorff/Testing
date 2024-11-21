from fastapi import APIRouter
from utils import get_fib

router = APIRouter(prefix='/math')

@router.get("/fibonacci/{n}")
async def fib(n: int):
    '''проверяет корректность введенных данных'''
    if type(n) != int or n < 0:
        raise TypeError('Введите натуральное число')
    result = get_fib(n)
    return result