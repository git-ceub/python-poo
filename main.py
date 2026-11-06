from fastapi import FastAPI

app = FastAPI(
    title="API de Ciência de Dados",
    description="API construída pela turma durante a Aula 1.",
    version="1.0.0",
)

@app.get("/")
def inicio():
    return {"mensagem": "Minha primeira API!"}


@app.get("/sobre")
def sobre():
    return {
        "disciplina": "Programação para Ciência de Dados",
        "aula": 1,
        "versao_api": "1.0.0",
    }

alunos = [
    {"id": 1, "nome": "Ana", "nota": 8.5},
    {"id": 2, "nome": "Bruno", "nota": 6.0},
    {"id": 3, "nome": "Carla", "nota": 9.2},
    {"id": 4, "nome": "Diego", "nota": 7.0},
]

# inicio() e sobre() continuam como no Passo 2
@app.get("/alunos")
def listar_alunos():
    return {
        "total": len(alunos),
        "alunos": alunos,
    }