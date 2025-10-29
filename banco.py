import sqlite3
DB = "sistema_escolar.db"

# -------------- FUNÇÕES DO BANCO DE DADOS -------------- 

# -------------- -------------- -------------- ALUNOS -------------- -------------- -------------- 
def conectar_banco_alunos():
    ### Cria a tabela se não existir ###
    conn = sqlite3.connect(DB)
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




# -------------- -------------- -------------- TURMAS -------------- -------------- --------------
def conectar_banco_turmas():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS turmas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,    
            turma TEXT NOT NULL,
            professor TEXT NOT NULL,                
            turno TEXT NOT NULL,
            capacidade INTEGER,
            sala TEXT
        )
    """)
    conn.commit()


def cadastrar_turmas(turma, professor, turno, capacidade=None, sala=None):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("INSERT INTO turmas (turma, professor, turno, capacidade, sala) VALUES (?, ?, ?, ?, ?)", (turma, professor, turno, capacidade, sala))
    conn.commit()


def listar_turmas():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT id, turma, professor, turno, capacidade, sala FROM turmas ORDER BY id")
    dados = cur.fetchall()
    return dados


def buscar_nome_turmas():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT turma FROM turmas ORDER BY turma")
    turms = [t[0] for t in cur.fetchall()]
    conn.close()
    return turms if turms else ["Nenhuma cadastrada"]


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




# -------------- -------------- -------------- PROFESSORES -------------- -------------- --------------
def conectar_banco_professores():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS professores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data_nasc TEXT NOT NULL,
            especialidade TEXT NOT NULL,
            telefone TEXT,
            email TEXT
        )
    """)
    conn.commit()
    conn.close()


def cadastrar_professor(nome, data_nasc, especialidade, telefone=None, email=None):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("INSERT INTO professores (nome, data_nasc, especialidade, telefone, email) VALUES (?, ?, ?, ?, ?)", (nome, data_nasc, especialidade, telefone, email))
    conn.commit()
    conn.close()


def listar_professores():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT id, nome, data_nasc, especialidade, telefone, email FROM professores ORDER BY id")
    dados = cur.fetchall()
    conn.close()
    return dados


def buscar_nome_professores():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT nome FROM professores ORDER BY nome")
    profs = [p[0] for p in cur.fetchall()]
    conn.close()
    return profs if profs else ["Nenhum cadastrado"]


def buscar_professor(id_):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT nome, data_nasc, especialidade, telefone, email FROM professores WHERE id = ?", (id_,))
    dados = cur.fetchone()
    conn.close()
    return dados


def atualizar_professor(id_, nome, data_nasc, especialidade, telefone, email):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("UPDATE professores SET nome = ?, data_nasc = ?, especialidade = ?, telefone = ?, email = ? WHERE id = ?", (nome, data_nasc, especialidade, telefone, email, id_))
    conn.commit()
    conn.close()


def excluir_professor(id_):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("DELETE FROM professores WHERE id = ?", (id_,))
    conn.commit()
    conn.close()




# -------------- -------------- -------------- AULAS -------------- -------------- --------------
def conectar_banco_aulas():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS aulas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            disciplina TEXT NOT NULL,
            professor TEXT NOT NULL,
            turma TEXT NOT NULL,
            horario TEXT NOT NULL,
            sala TEXT
        )
    """)
    conn.commit()
    conn.close()

def cadastrar_aula(disciplina, professor, turma, horario, sala):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("INSERT INTO aulas (disciplina, professor, turma, horario, sala) VALUES (?, ?, ?, ?, ?)", (disciplina, professor, turma, horario, sala))
    conn.commit()
    conn.close()

def listar_aulas():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT id, disciplina, professor, turma, horario, sala FROM aulas ORDER BY id")
    dados = cur.fetchall()
    conn.close()
    return dados

def atualizar_aula(id_, disciplina, professor, turma, horario, sala):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("UPDATE aulas SET disciplina=?, professor=?, turma=?, horario=?, sala=? WHERE id=?", (disciplina, professor, turma, horario, sala, id_))
    conn.commit()
    conn.close()

def excluir_aula(id_):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("DELETE FROM aulas WHERE id=?", (id_,))
    conn.commit()
    conn.close()
