# !5 = 5 * 4 * 3 * 2 * 1 
def factorial(n):
    print (n)
    if n == 1:
        return 1
    
    return n * factorial(n-1)

print(factorial(5))