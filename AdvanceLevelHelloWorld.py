import time

def helloWorldPrint(hello):
    for char in hello:
        for pointer in "!,ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            print(pointer, end="\r")
            time.sleep(0.1)
            if char == pointer:
                break
        
        print(char)
        time.sleep(0.5)

if __name__ == "__main__":
    hello = "Hello, World!"
    helloWorldPrint(hello)