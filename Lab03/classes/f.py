prime = lambda x : x > 1 and all(x % i != 0 for i in range(2, x - 1))
numbers = [78, 110, 53, 71, 83, 98, 633, 89]
prime_numbers = list(filter(prime, numbers))
print(prime_numbers)
