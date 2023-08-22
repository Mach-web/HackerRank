import importlib
if __name__ == '__main__':
    N = int(input())
    myList = []
    for _ in range(N):
        inputs = input()
        inputs = inputs.split()
        if len(inputs) == 3:
            myList.__getattribute__(inputs[0])(int(inputs[1]), int(inputs[2]))
        elif len(inputs) == 2:
            myList.__getattribute__(inputs[0])(int(inputs[1]))
        elif inputs[0] == "print":
            print(myList)
        else:
            myList.__getattribute__(inputs[0])

