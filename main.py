from fastapi import FastAPI
import pymysql

app = FastAPI(
    title="API de Ciência de Dados",
    description="API construída pela turma durante a Aula 1.",
    version="1.0.0",
)

def conectar():
    # Em um sistema real, a senha ficaria numa variável de ambiente,
    # nunca escrita no código.
    return pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="ceub123456",
        database="escola",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )


@app.get("/")
def inicio():
    return {"mensagem": "Minha primeira API!"}

@app.get("/saude")
def saude():
    try:
        with conectar() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute("SELECT DATABASE() AS banco, VERSION() AS versao")
                info = cursor.fetchone()
    except pymysql.err.OperationalError:
        raise HTTPException(
            status_code=503,
            detail="Não foi possível conectar ao banco de dados",
        )

    return {
        "status": "ok",
        "banco": info["banco"],
        "versao": info["versao"],
    }


@app.get("/sobre")
def sobre():
    return {
        "disciplina": "Programação para Ciência de Dados",
        "aula": 1,
        "versao_api": "1.0.0",
    }

@app.get("/alunos")
def listar_alunos():
    sql = """
        SELECT a.id, a.nome, a.email, a.ano_ingresso, c.sigla AS curso
        FROM alunos a
        JOIN cursos c ON c.id = a.curso_id
        ORDER BY a.id
    """
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql)
            alunos = cursor.fetchall()

    return {
        "total": len(alunos),
        "alunos": alunos,
    }
