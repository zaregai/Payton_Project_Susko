# Дано целое число N (>0). С помощью операций деления нацело и взятия остатка от
#деления определить, имеются ли в записи числа N нечетные цифры. Если имеются,
#то вывести TRUE, если нет — вывести FALSE.

n=input("Введите число больше нуля:")

while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("НЕПРАВЕЛЬНО ВВЕЛИ!")
        n = input("Введите число ещё раз:")

# f=10
# v=1

# flag = True

while n > 0:
    ost = n % 10
    if ost % 2:
        print(True)
        # flag = False
        break
    else:
        n %= 10

    n -= 1
#
# if flag:
#     print(False)

if n < 0:
    print(False)
elif n>0:
    print("ss")
    print(n)

# b = n%f
    # c= b//v
    # v=v*10
    # f=f*10
    # if (((c/2)*10)%10) != 0:
    #     print("True")
    #     break
    # if c == 0:
    #     break
#
# if (((c/2)*10)%10) ==0:
#     print("false")