import time

def printHelloWorld(hello):
    for char in hello:
        print(char, end="")
        time.sleep(.2)

if __name__ == "__main__":
    hello = "Hello, World!"
    printHelloWorld(hello)