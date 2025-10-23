import sqlite3
DB = "alunos.db"




# -------------- FUNÇÕES DO BANCO DE DADOS -------------- 
def conectar_banco():
    ### Cria a tabela se não existir ###
    conn = sqlite3.connect(DB) # ou #with sqlite3.connect(DB) as conn:
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            datanasc TEXT NOT NULL,
            turma TEXT NOT NULL
        )
    """)
    conn.commit()


def cadastrar_alunos(nome, datanasc, turma):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("INSERT INTO alunos (nome, datanasc, turma) VALUES (?, ?, ?)", (nome, datanasc, turma))
    conn.commit()


def listar_alunos():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT id, nome, datanasc, turma FROM alunos ORDER BY id")
    return cur.fetchall()


def atualizar_alunos(id_, nome, datanasc, turma):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("UPDATE alunos SET nome=?, datanasc=?, turma=? WHERE id=?", (nome, datanasc, turma, id_))
    conn.commit()


def excluir_alunos(id_):
    conn = sqlite3.connect(DB) 
    cur = conn.cursor()
    cur.execute("DELETE FROM alunos WHERE id=?", (id_,))
    conn.commit()


def buscar_alunos(id_):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT nome, datanasc, turma FROM alunos WHERE id=?", (id_,))
    aluno = cur.fetchone()
    conn.close()
    return aluno


def limpa_banco():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("DELETE FROM alunos")  # limpa tudo
    conn.commit()
    conn.close()

