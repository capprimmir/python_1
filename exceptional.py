'''Module for demonstrate exceptions'''
def convert(s):
    try:
        x = int(s)
        print("Conversion sucessful")
    except ValueError:
        x = -1
        print("Incorrect value!")
    except TypeError:
        x = -1
        print("Incorrect value!")
    return x