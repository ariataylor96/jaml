# jaml

Lets you edit JSON as YAML, and vice versa, with only one command!

 - Intelligently detects output settings based on the input file type
 - Respects your $EDITOR if it can, otherwise tries to find one it can use
 - Is made with love


## Installation
```
pip install jaml-edit
```

## Usage
```
$ jaml --help
usage: jaml [-h] [-i INDENT] [-t] file_name

Interchangeably edit YAML as JSON and vice versa

positional arguments:
  file_name             The file to edit

optional arguments:
  -h, --help            show this help message and exit
  -i INDENT, --indent INDENT
                        How indented the output data should be
  -t, --trailing-whitespace
                        Add trailing whitespace to the end of the output
```
