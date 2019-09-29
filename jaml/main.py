import os
import sys
import yaml 
import json
import signal
import argparse

from shutil import which

from .identify import (
    is_json,
    opposing_file_extension_for,
    detect_indentation,
    has_trailing_whitespace,
)
from .hash import md5_hash_for

default_editors = [
    'nano',
    'pico',
    'xo',
    'emacs',
    'vim',
    'vi',
]


def _parse_args():
    parser = argparse.ArgumentParser(
        description='Interchangeably edit YAML as JSON and vice versa',
    )

    parser.add_argument('file_name', help='The file to edit')
    parser.add_argument(
        '-i',
        '--indent',
        help='How indented the output data should be',
        type=int,
        default=None,
    )
    parser.add_argument(
        '-t',
        '--trailing-whitespace',
        help='Add trailing whitespace to the end of the output',
        action='store_true',
        default=True,
    )
    args = parser.parse_args()

    return args


def load_yaml(f):
    return yaml.load(f.read(), Loader=yaml.FullLoader)


def dump_yaml(data, indent):
    return yaml.dump(data, indent=indent, default_flow_style=False, sort_keys=False)


def load_json(f):
    return json.loads(f.read())


def dump_json(data, indent):
    return json.dumps(data, indent=indent)


def get_funcs(file_name):
    json_funcs = [load_json, dump_json]
    yaml_funcs = [load_yaml, dump_yaml]
    
    if is_json(file_name):
        return [json_funcs, yaml_funcs]
    
    return [yaml_funcs, json_funcs]


def _interchange_contents(old_name, new_name, dump, load, indent, trailing=False):
    with open(old_name, 'r') as old:
        with open(new_name, 'w') as new:
            new.write(dump(load(old), indent=indent).rstrip())
            
            if trailing:
                new.write('\n')


def main():
    """
    Generates a JSON copy of your YAML files for convenient editing.
    
    Also works in reverse, if you like YAML for some reason.
    """
    args = _parse_args()
    [native_load, native_dump], [foreign_load, foreign_dump] = get_funcs(
        args.file_name,
    )
    
    indent = args.indent
    if indent is None:
        indent = detect_indentation(args.file_name) or 2

    editor = os.getenv('EDITOR')
    if editor is None:
        editor = [ed for ed in default_editors if which(ed) is not None][0]
        
    trailing = args.trailing_whitespace
    if trailing is None:
        trailing = has_trailing_whitespace(args.file_name)

    new_file_name = os.path.join(
        '/tmp',
        md5_hash_for(args.file_name) + opposing_file_extension_for(args.file_name),
    )
    
    # Prepare for a SIGINT before any files are modified
    def _sigint_handler(sig, frame):
        print('Removing tmp file and exiting gracefully...')
        os.remove(new_file_name)
        sys.exit(0)
    signal.signal(signal.SIGINT, _sigint_handler)

    _interchange_contents(
        args.file_name,
        new_file_name,
        foreign_dump,
        native_load,
        indent,
        trailing=trailing,
    )

    os.system(f'{editor} {new_file_name}')

    _interchange_contents(
        new_file_name,
        args.file_name,
        native_dump,
        foreign_load,
        indent,
        trailing=trailing,
    )
    
    os.remove(new_file_name)
