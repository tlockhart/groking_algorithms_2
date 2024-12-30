# NOTE: The numbers.append(equation) line appends the intermediate 
# Fibonacci numbers during every recursive call. As a result, 
# numbers will contain duplicates because the same Fibonacci number 
# gets calculated multiple times.

# Solution Memoization or Interative solution
def fib(num, numbers):
    # Base Case:
    if num <= 1:
        # if num == 1:
            # numbers.append(num)
        return num
    
    equation = fib(num - 1, numbers) + fib(num - 2, numbers)
    numbers.append(equation)
    return equation

numbers = []
print("Fib:" , fib(5, numbers))
print("numbers:", numbers)