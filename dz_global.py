
# задачи на строки (str):
# Номер 2.1
# var1 = "22"
# var2 = "2.2"
# var3 = "2_000_002"
# print(var1,var2,var3,sep=",")
# print(f"{var1},{var2},{var3}",sep= ",")

# Номер 2.2


# Задачи на условия (if else):
# Номер 9.1
# int(input("Введите данные: "))
# c = ""
# int = c 
# if not int:
#    print(False)
# else:
#    print(True)

# Номер 9.2
#x1 = int(input("Введите делимое: "))
#x2 = int(input("Введите делитель: "))
#if (x2!=0):
#    print(x1/x2)
#else:
#    print("Erorr")

# Номер 9.3
#x = int(input("Введите число: "))
#if (x%3==0):
#    print("Yes")
#else:
#    print("No")

# Номер 9.4
#x = int(input("Введите сумму покупки: "))
#if (x>20):
#   print ((x*0.65),'','- сумма покупки со скидкой в 35%')
#else:
#    print("Скидка только при покупке от 20 у.е")

# Номер 9.5
#x = int(input("Введите число: "))
#if (x<9 and x>=0):
#    print("Введёная переменная является цифрой десятичной системы счисления")
#else:
#    print("Введённая переменная не является цифрой десятичной системы счисления")

# Номер 9.6
# x = int(input("Введите число: "))
# if x==0:
#   print(x, "- это ноль")
# elif x==1:
#   print(x, "- это один")
# elif x==2:
#   print(x, "- это два")
# elif x==3:
#   print(x, "- это три")
# elif x==4:
#   print(x, "- это четыре")
# elif x==5:
#   print(x, "- это пять")
# elif x==6:
#   print(x, "- это шесть")
# elif x==7:
#   print(x, "- это семь")
# elif x==8:
#   print(x, "- это восемь")
# elif x==9:
#   print(x, "- это девять")
# else:
#    print("Введите цифру 10-й СС")

# Номер 9.8
# x = int(input("Введите денежную сумму: "))
# if (x<0 or x%2!=0):
#     print("Извините, но размен невозможен")
# else:
#     hun = x // 100
#     x = x%100
#     tens = x//10
#     x = x%10
#     two = x//2
# print(f"Размен: 100x{hun}, 10x{tens}, 2x{two}")

# Номер 9.9
# x = 130
# y = 25
# z = 70
# if x>y>z:
#    print(z)
# elif x<y<z:
#     print(x)
# else:
#     print(y)

# Номер 9.10
# x= int(input("x="))
# y= int(input("y="))
# if x>0 and y>0:
#     print("1 четверть")
# elif x<0 and y>0:
#     print("2 четверть")
# elif x<0 and y<0:
#     print("3 четверть")
# elif x>0 and y<0:
#     print("4 четверть")

# Номер 9.11
# a = float(input("a="))
# b = float(input("b="))
# c = float(input("c="))
# if a + b > c and a + c > b and b + c > a and min(a, min(b, c)) > 0:
#    if a == b == c:
#     print("Равносторонний треугольник")
#    elif a == b or a == c or b == c:
#     print("Равнобедренный треугольник")
#    else:
#     print("Разносторонний треугольник")
# else:
#  print("Такого треугольника не существует")
     
# Номер 9.12
# num = int(input("Введите число: "))
# if num<1 or num>12:
#     print("Ошибка, введите другое число")
# elif num==1:
#  print("Январь, зима")
# elif num==2:
#  print("Февраль, зима")
# elif num==3:
#  print("Март, весна")
# elif num==4:
#  print("Апрель, весна")
# elif num==5:
#  print("Май, весна")
# elif num==6:
#  print("Июнь, лето")
# elif num==7:
#  print("Июль, лето")
# elif num==8:
#  print("Август, лето")
# elif num==9:
#  print("Сентябрь, осень")
# elif num==10:
#  print("Октябрь, осень")
# elif num==11:
#  print("Ноябрь, осень")
# elif num==12:
#  print("Декабрь, зима")


# задачи на циклы (for, while):
# Упражнение 1
# while True:
#     num1 = int(input("Введите первое число: "))
#     num2 = int(input("Введите второе число: "))
#     print("Сумма чисел: ",num1+num2)
#     nz = input ("Нажмите Y или y для завершения программы:")
#     if (nz == "Y" or nz=="y"): break

# Упражнение 2



# https://okpython.net/python/python_zadachnik/python_zadachnik.html#ex_10



# задачи на списки (array):
# Упражнение 1 
# list1 = [1,2,10,13,22,25,77,89,20,94,93]
# index = list1.index(20)
# list1[index]=200
# print(list1)

#Упражнение 3
# x=[1,2,3,4,5,6,7]
# for i in (x):
#    x=i**2
#    print("Квадрат числа",i,"=",x)

#Упражнение 4
# list = [2,5,20,10,11,33,20,55]
# list.remove(20)
# print(list)

#Упражнение 5
# x = [2,5,20,10,11,33,20,55]
# list.reverse(x)
# print(x)

#Упражнение 6
# list = ["Ann","Jane","Mike","Koul","Tito"]
# list.extend(["Max","Alex"])
# list.pop()
# print(list)

#Упражнение 7
# mat = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 80]
# ]
# for i in range(3):
#     for a in range(3):
#         print(mat[i][a], end = " ")
#     print()

#Упражнение 8
# numbers = []
# squares = []
# cubes = []
# start = 1
# end = 10
# for count in range (start, end+1) :
#     numbers.append (count)
#     squares.append (count**2)
#     cubes.append (count**3)
# print ("numbers: ",numbers)
# print ("squares: ",squares)
# print ("cubes : ",cubes)

#Упражнение 9
# list_txt = [11, 22, 33, 44, 55]
# print("Список чисел:",list_txt)
# for i in (list_txt):
#     if (i%2==0):
#      list_txt.remove(i)
# print("Список с нечётными числами:" ,list_txt)

#Упражнение 10
# list_a=[1, 2, 3, 4]
# list_b=[5, 6, 7, 8]
# summed_list= list_a+list_b
# print(summed_list)

#Упражнение 3.4
# list = ['Санкт', '+', 'Петербург']
# del list[1]
# list.insert(1,'-')
# print(list[0],list [1], list [2])

#Упражнение 3.5
# list_obw = ['a', '1', 'b', '2', 'c', '3']
# list_num = []
# list_letters = []
# list_obw.clear
# print(list_num,list_letters)



# задачи на словари:
#Упражнение 5.1
# d = {'1': 0, 2: 0, '3': 0}
# print(d)
# for key,value in d.items():
#     print(key,"-",value)

# Упражнение 5.2
# dict = {"имя": "Антон","возраст": 29, "пол": "мужской"}
# print(dict)

# Упражнение 5.3
# d = {'1': 1.29, '2': 0.43}




# https://metanit.com/python/practice/8.php
# https://pythonist.ru/python-slovari-zadachi-dlya-nachinayushhih/



# задачи на функции (function):
# https://okpython.net/python/python_zadachnik/python_zadachnik.html#ex_12
# https://pynative.com/python-functions-exercise-with-solutions/
# https://proglib.io/p/funkcii-v-python-5-zadach-dlya-trenirovki-args-kwargs-i-lambda-funkciy-2022-06-15



# задачи на рекурсию (function):
# (внизу) https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-13-rekursivnye-funkcii-2023-01-23
# https://w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php