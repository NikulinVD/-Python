# Ввести число, и выяснить - положительное оно, отрицательное, или равно нулю?
a = float(input('Введите число: '))
if a < 0:
    print('Число отрицательное')
elif a > 0:
    print('Число положительное')
else:
    print('Число равно нулю')