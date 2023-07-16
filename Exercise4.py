# Задача 4

# Определите, можно ли от шоколадки размером a × b долек 
# отломить c долек, если разрешается сделать один разлом 
# по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# Выведите yes или no соответственно.

# Пример:
# a, b, c = 3, 2, 4 -> yes
# a, b, c = 3, 2, 1 -> no

a = int(input('Enter your a: '))
b = int(input('Enter your b: '))
c = int(input('Enter your c: '))

chocolateSquare = a*b
partToTake = c
if partToTake > chocolateSquare:
    print("no")
elif partToTake == chocolateSquare: # ситуация, когда отламывать шоколадку не надо, а можно просто взять единственную дольку
    print("yes")
else:
    if partToTake%a == 0 or partToTake%b == 0:
        print("yes")
    else:
        print("no")
