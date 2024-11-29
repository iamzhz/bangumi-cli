"""
    a `line` has:
       verb: the main command that is like the verb in a sentence (must have)
       args: the words that come after the verb, separated by spaces (may have)
    eg. 'download the_pictuce'
"""
def parse_line(line):
    words = line.split()
    verb = words[0]
    args = words[1:]
    return verb, args