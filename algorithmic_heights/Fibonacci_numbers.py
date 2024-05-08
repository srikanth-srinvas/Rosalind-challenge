def Fibonacci_number_generator(number):
    old, new = 1, 1
    for itr in range(number - 1):
        new, old = old, old + new
    return new


print(Fibonacci_number_generator(23))