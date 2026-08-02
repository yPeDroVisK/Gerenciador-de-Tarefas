from fastapi import FastAPI

from .routes import auth_router

# Testando coneção com API

app = FastAPI(
    title="TaskFlow API",
    description="API do gerenciador de tarefas TaskFlow",
    version="0.1.0",
)

app.include_router(auth_router)

@app.get("/")
def root():
    return{
        "message": "TaskFlow API está rodando",
        "status": "Sucesso",
    }
