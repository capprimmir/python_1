'''Module for demonstrate exceptions'''
def convert(s):
    x = -1
    try:
        x = int(s)
        print("Conversion sucessful! x= ", x)
    except (ValueError, TypeError):
        print("Incorrect value!")
    return x