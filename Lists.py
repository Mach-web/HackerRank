'''https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true'''

if __name__ == '__main__':
    N = int(input())
    myList = []
    for _ in range(N):
        inputs = input()
        inputs = inputs.split()
        # Place the inputs into a list
        if len(inputs) == 3:
            # Use __getattribute__ to input a variable as a function
            myList.__getattribute__(inputs[0])(int(inputs[1]), int(inputs[2]))
        elif len(inputs) == 2:
            myList.__getattribute__(inputs[0])(int(inputs[1]))
        elif inputs[0] == "print":
            print(myList)
        else:
            myList.__getattribute__(inputs[0])()

