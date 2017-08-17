
def recursive_fibonacci(n):
    """ Recursive function to return a given Fibonacci number without memoization. """
    if n <= 1:
        return n
    else: return (recursive_fibonacci(n-1) + recursive_fibonacci(n-2))

def cached_fibonacci(n, cache={}):
    if n in cache:
        return cache[n]  
    elif n <= 1:
        cache[n] = n
    else:
        cache[n] = cached_fibonacci(n-1) + cached_fibonacci(n-2)
    return cache[n]