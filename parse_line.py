"""
    a `line` has:
       verb: the main command that is like the verb in a sentence (must have)
       args: the words that come after the verb, separated by spaces (may have)
    eg. 'download the_pictuce'
"""


def line_to_args_py(line):
    return line.split()


try:
    import c_ext
    line_to_args = c_ext.line_to_args
except ImportError:
    print("Warning: c_ext not found, using python implementation")
    line_to_args = line_to_args_py


def parse_line(line):
    words = line_to_args(line)
    if len(words) == 0:
        return None, None
    verb = words[0]
    args = words[1:]
    return verb, args
