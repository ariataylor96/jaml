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
