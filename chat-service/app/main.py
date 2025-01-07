from fastapi import FastAPI
from routes import users, messages

app = FastAPI()

# Регистрируем маршруты пользователей
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(messages.router, prefix="/messages", tags=["messages"])
