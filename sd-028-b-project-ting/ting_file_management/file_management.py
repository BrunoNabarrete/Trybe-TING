import sys


def txt_importer(path_file):
    try:
        with open(path_file, 'r') as file:
            if not path_file.lower().endswith('.txt'):
                raise ValueError("Formato inválido")

            lines = [line.strip() for line in file.readlines()]
            return lines

    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
        sys.stderr.flush()
    except ValueError as e:
        sys.stderr.write(f"{e}\n")
        sys.stderr.flush()

    return []
