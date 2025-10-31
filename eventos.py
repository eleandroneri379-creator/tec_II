from banco import inserir_evento, buscar_eventos, deletar_evento

def adicionar_evento(nome, data, descricao):
    if nome and data:
        inserir_evento(nome, data, descricao)

def listar_eventos():
    return buscar_eventos()

def excluir_evento(nome):
    deletar_evento(nome)