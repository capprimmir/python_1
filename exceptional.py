'''Module for demonstrate exceptions'''

import sys

def convert(s):
    '''convert to an integer'''
    try:
        return int(s)
        print("Conversion sucessful! x= ", x)
    except (ValueError, TypeError) as e:
        print("Conversion Error: {}".format(str(e)),file=sys.stderr)
        return -1