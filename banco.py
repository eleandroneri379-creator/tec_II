import sqlite3

def iniciar_banco():
    conn = sqlite3.connect("eventos.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS eventos (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            data TEXT,
            descricao TEXT
        )
    """)
    conn.commit()
    conn.close()

def inserir_evento(nome, data, descricao):
    conn = sqlite3.connect("eventos.db")
    conn.execute("INSERT INTO eventos (nome, data, descricao) VALUES (?, ?, ?)", (nome, data, descricao))
    conn.commit()
    conn.close()

def buscar_eventos():
    conn = sqlite3.connect("eventos.db")
    eventos = conn.execute("SELECT nome, data, descricao FROM eventos ORDER BY data").fetchall()
    conn.close()
    return eventos

def deletar_evento(nome):
    conn = sqlite3.connect("eventos.db")
    conn.execute("DELETE FROM eventos WHERE nome = ?", (nome,))
    conn.commit()
    conn.close()