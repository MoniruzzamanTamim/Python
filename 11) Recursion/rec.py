

def fact(n):
    if n == 15:
        return n
    else :
        print(n)
        
    fact(n+1)

fact(6)


def factorial(n):
    if n == 0:
        return 1     # base case
    else:
        return n * factorial(n - 1)   # recursive case

print(factorial(5))  # Output: 120


#Recursion ON Fibonacci

def fibonacci(n):
    if n <= 1:
        return n  # base case
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("fibonacci in Recursion: ", fibonacci(10))  # Output: 55
