# Ввести с клавиатуры шестизначный номер трамвайного (троллейбусного) билета,
# и определить является ли он счастливым (совпадают суммы трёх первых и трёх последних цифр билета).
n = input('Введите номер вашего трамвайного (троллейбусного) билета: ')
s1 = int(n[0]) + int(n[1]) + int(n[2])
s2 = int(n[3]) + int(n[4]) + int(n[5])
if s1 == s2:
    print('Вам попался счастливый билет!')
else:
    print('Вам попался обычный билет')