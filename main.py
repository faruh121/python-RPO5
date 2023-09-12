#Python_DZ_Modul__01
# Задание 1
# Пользователь вводит с клавиатуры три числа. Необходимо найти сумму чисел, произведение чисел. Результат
# вычислений вывести на экран.
while True:
    print("Вас приветствует програма которая считает сумму и произведение чисел!")
    num_1 = int(input("Введите 1 число:"))
    num_2 = int(input("Введите 2 число:"))
    znak = input("найти сумму или произведение:")
    if znak=="сумму":
        print("Сумма этих чисел равна:", num_1+num_2)
        break
    elif znak=="произведение":
        print("Произведение этих чисел равно:",num_1*num_2)
        break
    else:
        print("вы ввели не правельное слово")
        perezapusk = input("попробуете еще:для перезапуска нажмите любую букву или  нажмите нет для отмены ")
        if perezapusk=="нет":
            print("удачи")
            break
        else:
            print("loading...")
            print("loading.../..")
            print("loading...////.....")
# Задание 2
# Пользователь вводит с клавиатуры три числа. Первое
# число — зарплата за месяц, второе число — сумма месячного платежа по кредиту в банке, третье число — задолженность за коммунальные услуги. Необходимо вывести
# на экран сумму, которая останется у пользователя после
# всех выплат.
lang=input("select a language rus or eng:")
if lang=="rus":
     num_1_r=int(input("Каков ваш ежемесячный доход? "))
     num_2_r= int(input("Сколько вы платите в месяц за кредит? "))
     num_3_r= int(input("Сколько вы платите в месяц за коммунальные услуги? "))
     if num_1_r-num_2_r-num_3_r<0:
         print("вы будете должны",num_1_r-num_2_r-num_3_r)
     elif num_1_r-num_2_r-num_3_r == 0:
         print("в этом месяце вы на диете(")
     else:
         print("у вас осталось:", num_1_r-num_2_r-num_3_r)
elif lang=="eng":
     num_1_e=int(input("What is your monthly income? "))
     num_2_e= int(input("How much do you pay per month for a loan? "))
     num_3_e= int(input("How much do you pay per month for communal services? "))
     if num_1_e-num_2_e-num_3_e<0:
         print("you will have to",num_1_e-num_2_e-num_3_e)
     elif num_1_e-num_2_e-num_3_e == 0:
         print("you are on a diet this month(")
     else:
         print("you have left:", num_1_e-num_2_e-num_3_e)
# Задание 3
# Напишите программу, вычисляющую площадь ромба. Пользователь с клавиатуры вводит длину двух его
# диагоналей.
while True:
    print("Здравствуйте вас приветствует програма-калькулятор которая считает площадь ромба по его диоганалям!")
    d_1 = int(input("введите 1 диоганаль:"))
    d_2 = int(input("введите 2 диоганаль:"))
    print("Площадь ромба равна",d_1*d_2/2)
    perez = input("желаете перезапуск? нажмите любая букву если да или напишите нет:")
    if perez=="нет":
        print("удачи))")
        break
    else:
        print("загрузка.....")   
# Задание 4
# Выведите на экран надпись To be or not to be на разных
# строках. Пример вывода:
print("To be\nor not\nto be")
# Выведите на экран надпись «Life is what happens when
# you're busy making other plans» John Lennon на разных
# строках. Пример вывода:
print("'Life is what happens\n   when\n     you're busy making other plans'\n                                  John Lennon")
