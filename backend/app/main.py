from fastapi import FastAPI

# Testando coneção com API

app = FastAPI(
    title="TaskFlow API",
    description="API do gerenciador de tarefas TaskFlow",
    version="0.1.0",
)

@app.get("/")

def root():
    return{
        "message": "TaskFlow API está rodando",
        "status": "Sucesso",
    }
