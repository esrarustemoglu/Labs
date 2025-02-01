def filter_prime(lst):
    for x in lst:
        if x < 2:
            continue
        is_prime = True
        for i in range (2, x - 1):
            if x % i == 0:
                is_prime = False
                break
        if is_prime:
            print(x)  
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filter_prime(lst)