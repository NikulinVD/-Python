# Марафонец прошел S километров со скоростью V метров в секунду (расстояние и скорость вводятся с клавиатуры).
# Определить, сколько времени он был в пути (часов, минут, секунд)? 
s = float(input('Введите расстояние: '))*1000
v = float(input('Введите скорость: '))
t = s/v
print('Марафонец был в пути ' + '%d' % (t//3600) + ' ч. ' + '%d' %(t%3600//60) + ' мин. '+ '%d' %(t%60) +' сек.')