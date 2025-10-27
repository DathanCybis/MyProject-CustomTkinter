import sqlite3
DB = "sistema_escolar.db"

# -------------- FUNÇÕES DO BANCO DE DADOS -------------- 

# -------------- ALUNOS -------------- 
def conectar_banco_alunos():
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




# -------------- TURMAS --------------
def conectar_banco_turmas():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS turmas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,    
            turma TEXT NOT NULL,
            professor TEXT,                
            turno TEXT NOT NULL,
            capacidade INTEGER,
            sala TEXT
        )
    """)
    conn.commit()


def cadastrar_turmas(turma, professor, turno, capacidade, sala):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("INSERT INTO turmas (turma, professor, turno, capacidade, sala) VALUES (?, ?, ?, ?, ?)", (turma, professor, turno, capacidade, sala))
    conn.commit()


def listar_turmas():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT id, turma, professor, turno, capacidade, sala FROM turmas ORDER BY id")
    return cur.fetchall()


def atualizar_turmas(id_, turma, professor, turno, capacidade, sala):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("UPDATE turmas SET turma=?, professor=?, turno=?, capacidade=?, sala=? WHERE id=?", (turma, professor, turno, capacidade, sala, id_))
    conn.commit()


def excluir_turmas(id_):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("DELETE FROM turmas WHERE id=?", (id_))
    conn.commit()


def buscar_turmas(id_):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT turma, professor, turno, capacidade, sala FROM turmas WHERE id=?", (id_))
    turma = cur.fetchone()
    conn.close()
    return turma

