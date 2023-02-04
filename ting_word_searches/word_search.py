def exists_word(word, instance):
    results = []

    for file in instance._queue:
        occurrence_lines = []

        for index, line in enumerate(file['linhas_do_arquivo']):
            if word.lower() in line.lower():
                occurrence_lines.append({'linha': index + 1})

        if occurrence_lines:
            results.append({
                        'palavra': word,
                        'arquivo': file['nome_do_arquivo'],
                        'ocorrencias': occurrence_lines
                    })

    return results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
