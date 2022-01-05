import time
import sys


def moveleft(n=1000):
    """Returns unicode string to move cursor left by n"""
    return u"\u001b[{}D".format(n)


def loading():
    """Prints a loading message"""
    print("Loading...")
    for i in range(100):
        time.sleep(0.05)
        sys.stdout.write(moveleft() + str(i + 1) + "%")
        sys.stdout.flush()
    print()

def loadingBar():
    """Prints a loading bar"""
    barLen = 50
    for i in range(barLen):
        time.sleep(0.05)
        sys.stdout.write(moveleft() + "[" + ''.join(["." if j <= i else " " for j in range(barLen)]) + "] " + str(i + 1) + "%")
        sys.stdout.flush()
    print()


if __name__ == '__main__':
    # loading()
    loadingBar()
