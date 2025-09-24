import math
from mod import product_odd

def expression(alpha):
    z = math.cos(alpha) + math.cos(2*alpha) + math.cos(6*alpha) + math.cos(7*alpha)
    return z

alpha = float(input("Введіть значення α: "))
print("Значення виразу z = ", expression(alpha))

n = int(input("Введіть натуральне число n: "))
print("Добуток непарних чисел до (2n-1) = ", product_odd(n))
