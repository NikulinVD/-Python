# Ввести с клавиатуры 3-значное число и «перевернуть» его (например, ввести 357 – получить и вывести 753).

strNumber=input('Введите трехзначное число ')[:3]
print('Число без средней цифры: '+strNumber[0]+strNumber[2])