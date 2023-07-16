# Задача 3

# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером.

# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.

# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.

# Вам требуется написать программу, которая проверяет
# счастливость билета с номером n и выводит на экран yes или no.

n = int(input('Enter your number of ticket (6 digits): '))
while len(str(n))!=6:
    n = int(input('There must be 6 digits in your ticket\'s number. Try again: '))


sumfirst = n//100000 + n//10000%10 + n//1000%10
sumlast = n%10 + n//10%10 + n//100%10

if sumfirst == sumlast:
    print("yes")
else:
    print ("no")