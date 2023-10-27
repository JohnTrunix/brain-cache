---
icon: material/console
---

# argparse

!!! info "Command Line Arguments"

    The `argparse` module enables the parsing of command line arguments.

[Python `argparse` Documentation :material-file-document-arrow-right-outline:](https://docs.python.org/3/library/argparse.html){ .md-button target="\_blank"}

**Example Usage**

```terminal
python main.py -i input.txt -o output.txt --verbose
```

## Defining Arguments

Arguments are defined by creating an `ArgumentParser` object and adding arguments to it.

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='Input file')
parser.add_argument('-o', '--output', help='Output file')
```

### Input Parameters for `ArgumentParser.add_argument()`

| Parameter  | Description                               | Values                                                                                     |
| ---------- | ----------------------------------------- | ------------------------------------------------------------------------------------------ |
| `...`      | Name or flags of the argument.            |                                                                                            |
| `action`   | How argument should be handled.           | `store`, `store_const`, `store_true`, `append`, `append_const`, `count`, `help`, `version` |
| `choices`  | List of allowed values.                   | `List[str]`, `range(1,10)`, `Container`                                                    |
| `default`  | Default value if argument is not provided | Default: `None`                                                                            |
| `const`    | Value to be used for `store_const`        | If flag is set, store `const` value                                                        |
| `help`     | Help text for the argument.               |                                                                                            |
| `type`     | Type of the argument.                     |                                                                                            |
| `required` | Whether the argument is required.         | `True` or `False`                                                                          |
| `nargs`    | Number of times argument can be reused    | `int`, `?`, `*`, `+`                                                                       |

**`action`**

| Value          | Description                                                   |
| -------------- | ------------------------------------------------------------- |
| `store`        | Store the argument value in the `args` namespace.             |
| `store_const`  | Store the value specified by `const` in the `args` namespace. |
| `store_true`   | Store the value `True` in the `args` namespace.               |
| `append`       | Append the value to a list, useful for multiple argument use. |
| `append_const` | Append the value specified by `const` to a list.              |
| `count`        | Count the number of times the argument is used.               |
| `help`         | Print help text and exit.                                     |
| `version`      | Print version text and exit.                                  |

**Example Usage**

```python
parser.add_argument(
    '-i', '--input',
    action='store',
    choices=['a', 'b', 'c'],
    default='a',
    type=str,
    required=True,
    nargs=1,
    help='Input file'
    )
```

```terminal
python main.py -i a
python main.py --input a

### parser.input = 'a'
```

### Positional Arguments

Postitional arguments are arguments which are not preceded by a flag. They get interpreted in the order they are defined. Normally, positional arguments are used for required arguments.

```python
parser.add_argument('input')
```

```terminal
python main.py input
```

### Optional Arguments

Optional arguments are arguments which are preceded by a flag. They can be used in any order.

```python
parser.add_argument("--optional_arg", type=str, help="optional")
```

```terminal
python main.py --optional_arg
```

### Argument with Value

Arguments can be defined with a value. The value can be accessed by the `args` namespace.

```python
parser.add_argument("--value", type=int, choices=range(1,10+1))
```

```terminal
python main.py --value 2
```

### Argument Shortcuts

`add_argument` can take multiple flags for the same flag.

```python
parser.add_argument("-i", "--input", type=str)
```

```terminal
python main.py -i test
python main.py --input test
```

## Help

`Argparse` adds `-h` and `--help` flags by default.

```terminal
python main.py --help
```

## Subparser

If `argparse` should solve multiple different problems/tasks subparsers are a great solution. For each sub task we can define a subparser.

Add subparser to the main parser:

```python
import argparse

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest="command")
```

Create two differen parsers for differend usecases:

```python
add = subparser.add_parser("add")
rm = subparser.add_parser("del")
```

Now we can get the specified command over the argparse Namespace from `command`:

```python
args = parser.parse_args()

if args.command == "add":
    print("add")
elif args.command == "del":
    print("delete")
```
