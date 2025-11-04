import FreeSimpleGUI as sg
import sqlite3

def iniciar_banco():
    conn = sqlite3.connect("eventos.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS eventos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data TEXT NOT NULL,
            descricao TEXT
        )
    """)
    conn.commit()
    conn.close()

def adicionar_evento(nome, data, descricao):
    conn = sqlite3.connect("eventos.db")
    conn.execute("INSERT INTO eventos (nome, data, descricao) VALUES (?, ?, ?)", (nome, data, descricao))
    conn.commit()
    conn.close()

def listar_eventos():
    conn = sqlite3.connect("eventos.db")
    eventos = conn.execute("SELECT nome, data, descricao FROM eventos ORDER BY data").fetchall()
    conn.close()
    return eventos

def excluir_evento(nome):
    conn = sqlite3.connect("eventos.db")
    conn.execute("DELETE FROM eventos WHERE nome = ?", (nome,))
    conn.commit()
    conn.close()

def iniciar_agenda():
    iniciar_banco()

    layout = [
        [sg.Text("Nome do Evento:"), sg.Input(key="nome")],
        [sg.Text("Data (DIA-MÊS-ANO):"), sg.Input(key="data")],
        [sg.Text("Descrição:"), sg.Input(key="descricao")],
        [sg.Button("Adicionar"), sg.Button("Listar"), sg.Button("Excluir"), sg.Button("Sair")],
        [sg.Output(size=(60, 10))]
    ]

    janela = sg.Window("Agenda de Eventos", layout)

    while True:
        evento, valores = janela.read()
        if evento in (sg.WINDOW_CLOSED, "Sair"):
            break
        elif evento == "Adicionar":
            adicionar_evento(valores["nome"], valores["data"], valores["descricao"])
            print(" Evento adicionado!\n")
        elif evento == "Listar":
            print(" Eventos cadastrados:")
            for e in listar_eventos():
                print(f"{e[0]} | {e[1]} | {e[2]}")
            print()
        elif evento == "Excluir":
            excluir_evento(valores["nome"])
            print(f" Evento '{valores['nome']}' excluído.\n")

    janela.close()

if __name__ == "__main__":
    iniciar_agenda()