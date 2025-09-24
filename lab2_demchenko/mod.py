def product_odd(n):
    dob = 1
    for i in range(1, 2*n, 2):
        dob *= i
    return dob
