import FreeSimpleGUI as sg
from eventos import adicionar_evento, listar_eventos, excluir_evento
from banco import iniciar_banco

def iniciar_agenda():
    iniciar_banco()

    layout = [
        [sg.Text("Nome:"), sg.Input(key="nome")],
        [sg.Text("Data (AAAA-MM-DD):"), sg.Input(key="data")],
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
            print("✅ Evento adicionado!\n")
        elif evento == "Listar":
            print("📅 Eventos:")
            for e in listar_eventos():
                print(f"{e[0]} | {e[1]} | {e[2]}")
            print()
        elif evento == "Excluir":
            excluir_evento(valores["nome"])
            print(f"🗑️ Evento '{valores['nome']}' excluído.\n")

    janela.close()