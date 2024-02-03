def exists_word(word, instance):
    result = []

    for file_data in instance.items:
        file_name = file_data["nome_do_arquivo"]
        lines = file_data["linhas_do_arquivo"]

        found_lines = []

        for line_number, line in enumerate(lines, 1):
            if word.lower() in line.lower():
                found_lines.append({"linha": line_number})
        if found_lines:
            result.append(
                {"arquivo": file_name,
                    "ocorrencias": found_lines,
                    "palavra": word})

    return result


def search_by_word(word, instance):
    result = []

    for file_data in instance.items:
        file_name = file_data["nome_do_arquivo"]
        lines = file_data["linhas_do_arquivo"]

        found_lines = []

        for line_number, line in enumerate(lines, 1):
            if word.lower() in line.lower():
                found_lines.append(
                    {"linha": line_number, "conteudo": line.strip()})

        if found_lines:
            result.append(
                {"arquivo": file_name,
                 "ocorrencias": found_lines,
                 "palavra": word}
                )

    return result
