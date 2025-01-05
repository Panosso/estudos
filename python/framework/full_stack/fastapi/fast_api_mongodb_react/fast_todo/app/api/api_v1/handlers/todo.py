from fastapi import APIRouter, Depends
from schemas.todo_schema import TodoDetail, TodoCreate, TodoUpdate
from models.user_model import User
from api.dependencies.user_deps import get_current_user
from services.todo_service import TodoService
from models.todo_model import Todo
from typing import List
from uuid import UUID

todo_router = APIRouter()

@todo_router.get('/', summary="Lista Todas as Notas", response_model=List[TodoDetail])
async def list(current_user: User = Depends(get_current_user)):
    return await TodoService.list_todos(current_user) 

@todo_router.post('/create', summary="Adicionando Nota", response_model=Todo)
async def create_todo(data: TodoCreate, current_user: User = Depends(get_current_user)):
    return await TodoService.create_todo(current_user, data)

@todo_router.get('/{todo_id}', summary='Detalhe de Nota por Id', response_model=TodoDetail)
async def detail(todo_id: UUID, current_user: User = Depends(get_current_user)):
    return await TodoService.detail(current_user, todo_id)

@todo_router.put('/{todo_id}', summary='Atualiza Nota', response_model=TodoDetail)
async def update(todo_id: UUID, data: TodoUpdate, current_user: User = Depends(get_current_user)):
    return await TodoService.update_todo(current_user, todo_id, data)

@todo_router.delete('/{todo_id}', summary='Exclui Nota')
async def delete(todo_id: UUID, current_user: User = Depends(get_current_user)):
    await TodoService.delete_todo(current_user, todo_id)
    return None
