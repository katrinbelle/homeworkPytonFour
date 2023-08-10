 # Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

#*Пример:*

#A = 3; B = 5 -> 243 (3⁵)
 #   A = 2; B = 3 -> 8 
numberA=int(input("Введите первое число-> "))
numberB=int(input("Введите второе число-> "))
def Power (a,b):
    if b==1 or b==0:
        return a
    else:
        a*=a
        return Power(a,b-1)
print(Power(numberA,numberB))