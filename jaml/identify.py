import mimetypes


def is_json(file_name):
    return mimetypes.guess_type(file_name)[0] == 'application/json'


def is_yaml(file_name):
    return not is_json(file_name)


def opposing_file_extension_for(file_name):
    # YAML does not actually have a mimetype
    return {
        'application/json': '.yml',
    }.get(mimetypes.guess_type(file_name)[0], '.json')


def detect_indentation(file_name):
    indents = {}
    last = 0

    with open(file_name, 'r') as f:
        for line in f:
            leading_spaces = len(line) - len(line.lstrip())

            relative_indent = abs(leading_spaces - last)
            if relative_indent > 1:
                indents[relative_indent] = indents.get(relative_indent, 0) + 1

            last = relative_indent

    # If there is only one value in this list, items() returns
    # a different structure
    keys = list(indents.keys())
    values = list(indents.values())

    try:
        return keys[values.index(max(values))]
    except IndexError:
        return None


def has_trailing_whitespace(file_name):
    with open(file_name, 'r') as f:
        f.seek(-1, 2)
        return f.read() == '\n'
