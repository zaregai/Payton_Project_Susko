#1. Дано вещественное число A и целое число N (>0). Найти A в степени N: AN = AA ... •A (числа A перемножаются N раз).

a = input("Введите вещественное число:")
n = input("Введите степень:")

while type(a) != float:
    try:
        a = float(a)
    except ValueError:
        print(" Введено неверное знгачение")
        a = input("Введите число")


while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("неверно ввели степень")
        n = input("Введите степень")
n-=1
h=a
while n > 0:
    a= h * a
    n -= 1
print("ответом будет:")
print(a)

