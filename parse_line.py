"""
    a `line` has:
       verb: the main command that is like the verb in a sentence (must have)
       args: the words that come after the verb, separated by spaces (may have)
    eg. 'download the_pictuce'
"""

from say_error import say_error


def line_to_args_py(line: str) -> list:
    return line.split()


try:
    import c_ext
    if hasattr(c_ext, 'line_to_args'):
        line_to_args = c_ext.line_to_args
    else:
        raise ImportError("c_ext does not have line_to_args")
except ImportError:
    say_error.say("c_ext not found or line_to_args missing, using python implementation")
    line_to_args = line_to_args_py


def parse_line(line: str) -> (str, list):
    words = line_to_args(line)
    if len(words) == 0:
        return None, None
    verb = words[0]
    args = words[1:]
    return verb, args
