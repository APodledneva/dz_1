"""Задача 6: Вы пользуетесь общественным транспортом?
Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером,
де сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.
*Пример:*
385916 -> yes
123456 -> no """

ticket = int(input("Введите билет из 6 знаков "))
sum_1 = (ticket % 1000) % 10 + ((ticket % 1000) // 10) % 10 + ((ticket % 1000) // 100) % 10
sum_2 = (ticket // 1000) % 10 + ((ticket // 1000) // 10) % 10 + ((ticket // 1000) // 100) % 10
if sum_1 == sum_2:
    print('Ура, счастливый билет!')
else:
    print('Повезет потом')
