def report_word_in_file(word, file):
    occurrence_lines = []

    for index, line in enumerate(file['linhas_do_arquivo']):
        if word.lower() in line.lower():
            occurrence_lines.append({'linha': index + 1})

    return occurrence_lines


def generate_report_word_in_file(word, instance, report_method):
    results = []

    for file in instance._queue:
        occurrence_lines = report_method(word, file)

        if occurrence_lines:
            results.append({
                        'palavra': word,
                        'arquivo': file['nome_do_arquivo'],
                        'ocorrencias': occurrence_lines
                    })

    return results


def exists_word(word, instance):
    return generate_report_word_in_file(word, instance, report_word_in_file)


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
