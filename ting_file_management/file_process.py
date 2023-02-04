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
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
