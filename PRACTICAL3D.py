def factorial(num):
    if num < 0:
        print(' Cannot find factorial of a negative number')
        return -1
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def factorial_iterate(num):
    if num < 0:
        print('Cannot find factorial of a negative number')
        return -1
    fact = 1
    while(num > 0):
        fact = fact * num
        num = num - 1
    return fact

if __name__ == '__main__':
    userInput = 6
    print('Using Recursion of', userInput, 'Factorial is:', factorial(userInput))
    print('Using Iteration of', userInput, 'Factorial is:', factorial_iterate(userInput))
