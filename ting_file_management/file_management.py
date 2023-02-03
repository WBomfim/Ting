import sys


def txt_importer(path_file):
    try:
        if path_file.endswith(".txt"):
            with open(path_file, "r") as file:
                return list(file.read().splitlines())

        return sys.stderr.write("Formato inválido")

    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
