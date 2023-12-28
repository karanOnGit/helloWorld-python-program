import time
import sys

def helloWorldPrint(hello):
    for char in hello:
        for alphabet_char in " ,!ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            sys.stdout.write(alphabet_char)
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write('\b')
            sys.stdout.flush()
            if alphabet_char == char:
                break

        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.5)

if __name__ == "__main__":
    hello = "Hello, World!"
    helloWorldPrint(hello)