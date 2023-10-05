# Задание 1
# Пользователь вводит с клавиатуры два числа. Нужно
# посчитать отдельно сумму четных, нечетных и чисел,
# кратных 9 в указанном диапазоне, а также среднеарифметическое каждой группы.

start = int(input("Начало диапозона: "))
end = int(input("Конец диапозона: "))
sumnech = 0
summachet = 0
krat9 = 0
for i in range(start,end+1):
    if i%2!=0:
        sumnech+=i
    elif i%2==0:
        summachet+=i
    elif i%9==0:
        krat9+=i
print("Сумма нечетных - ",sumnech)
print("Cумма четных - ",summachet)
print("Cумма кратных 9 - ",krat9)

# Задание 2
# Пользователь вводит с клавиатуры длину линии и
# символ для заполнения линии. Нужно отобразить на
# экране вертикальную линию из введенного символа,
# указанной длины.
# Например, если было введено 5 и символ %, тогда
# вывод на экран будет такой:
# %
# %
# %
# %
# %
n = int(input("Длинна линии:"))
symvol = input("Символ")
for i in range(1,n+1):
    print(symvol)

# Задание 3
# Пользователь вводит с клавиатуры числа. Если число
# больше нуля нужно вывести надпись «Number is positive»,
# если меньше нуля «Number is negative», если равно нулю
# «Number is equal to zero». Когда пользователь вводит
# число 7 программа прекращает свою работу и выводит
# на экран надпись «Good bye!»

num = int(input("Введите число а програма проверит равно 0 , больше 0 , или меньше 0: "))
while True:
    if num>0 and num!=7:
        print("Number is positive")
    elif num<0:
        print("Number is negative")
    elif num==0:
        print("Number is equal to zero")
    elif num==7:
        print("Good bye!")
        break
    else:
        print("loading....")

# Задание 4
# Пользователь вводит с клавиатуры числа. Программа должна подсчитывать сумму, максимум и минимум,
# введенных чисел. Когда пользователь вводит число 7
# программа прекращает свою работу и выводит на экран
# надпись «Good bye!»

while True:
    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter last number: "))
    print("Maximum number:")
    print(max(num_1,num_2))
    print("Minimum number:")
    print(min(num_1,num_2))
    print("Summ numbers:")
    print(num_1+num_2)
    if num_1==7 or num_2==7:
        print("Good bye!")
        break
    else:
        print("loading.....")













    