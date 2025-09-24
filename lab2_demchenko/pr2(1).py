import math

def expression(alpha):
    z = math.cos(alpha) + math.cos(2*alpha) + math.cos(6*alpha) + math.cos(7*alpha)
    return z

def product_odd(n):
    dob = 1
    for i in range(1, 2*n, 2):
        dob *= i
    return dob

alpha = float(input("Введіть значення α: "))
print("Значення виразу z = ", expression(alpha))

n = int(input("Введіть натуральне число n: "))
print("Добуток непарних чисел до (2n-1) = ", product_odd(n))
