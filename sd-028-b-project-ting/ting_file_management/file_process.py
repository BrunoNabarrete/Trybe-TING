import sys
from .file_management import txt_importer


def process(path_file, instance):
    if not any(
        file["nome_do_arquivo"] == path_file for file in instance.items
    ):
        data = txt_importer(path_file)
        if data:
            file_data = {
                "nome_do_arquivo": path_file,
                "qtd_linhas": len(data),
                "linhas_do_arquivo": data
            }
            instance.enqueue(file_data)
            print(file_data)
        else:
            print(f"Arquivo vazio ou inválido: {path_file}")
    else:
        print(f"Arquivo já processado: {path_file}")


def remove(instance):
    """Aqui irá sua implementação"""
    if len(instance) == 0:
        print("Não há elementos")
    else:
        fila_data = instance.dequeue()
        print(f"Arquivo {fila_data['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        fila_data = instance.search(position)
        print(fila_data)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
