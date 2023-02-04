import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if any(file['nome_do_arquivo'] == path_file for file in instance._queue):
        return

    data = txt_importer(path_file)
    dict_file = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(data),
        'linhas_do_arquivo': data
    }

    instance.enqueue(dict_file)
    return sys.stdout.write(f"{dict_file}\n")


def remove(instance):
    if len(instance._queue) == 0:
        return sys.stdout.write("Não há elementos\n")

    removed_element = instance.dequeue()
    return sys.stdout.write(
        f"Arquivo {removed_element['nome_do_arquivo']} removido com sucesso\n"
    )


def file_metadata(instance, position):
    try:
        return sys.stdout.write(f"{instance.search(position)}\n")

    except IndexError:
        return sys.stderr.write("Posição inválida\n")
