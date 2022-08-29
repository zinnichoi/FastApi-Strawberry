def unpack_row(rows, object_name):
    results = []
    for row in rows:
        results.append(row[object_name])

    return results


def camel_2_snake(string: str, separate_number: bool = False):
    return ''.join(
        ['_' + i.lower() if (i.isupper() or (separate_number and i.isnumeric())) else i for i in string]).lstrip('_')