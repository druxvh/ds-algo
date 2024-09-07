# Printing N Natural Numbers
def printN(n):
    if n > 0:
        printN(n-1)
        print(n, end=' ')

printN(100)

# Printing N Natural Numbers Reversed
def printN_Rev(n):
    if n > 0:
        print(n, end=' ')
        printN_Rev(n-1)

printN_Rev(10)

# Printing N Odd Natural Numbers
def printOddN(n):
    if n > 0:
        printOddN(n-1)
        print(2*n-1, end=' ')

printOddN(10)

# Printing N Even Natural Numbers
def printEvenN(n):
    if n > 0:
        printEvenN(n-1)
        print(2*n, end=' ')

printEvenN(10)

# Printing N Odd Natural Numbers Reversed
def printOddN_Rev(n):
    if n > 0:
        print(2*n-1, end=' ')
        printOddN_Rev(n-1)

printOddN_Rev(10)

# Printing N Even Natural Numbers Reversed
def printEvenN_Rev(n):
    if n > 0:
        print(2*n, end=' ')
        printEvenN_Rev(n-1)

printEvenN_Rev(10)

# Sum of N natural numbers
def sum_of_N(n):
    if n == 0:
        return 0
    return n + sum_of_N(n-1)

print(sum_of_N(5))


# Sum of N Odd natural numbers
def sumN_odd(n):
    if n == 0:
        return 0
    return (2*n-1) + sumN_odd(n-1)

print(sumN_odd(10))

# Sum of N Even natural numbers
def sumN_Even(n):
    if n == 0:
        return 0
    return (2*n) + sumN_Even(n-1)

print(sumN_Even(10))

# factorial of N natural numbers
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

print(fact(6))


# Sum of N natural Square numbers
def sumSqr(n):
    if n == 0:
        return 0
    return (n*n) + sumSqr(n-1)

print(sumSqr(5))
