# Написать программу, которая переводит фунты в килограммы. Один фунт – 405.9 грамма задается в программе как константа.
# Затем, реализовать обратный перевод – из килограммов в фунты.
pounds = float(input())
kilogramm = pounds * 0.406
print(round(kilogramm, 2))

# Затем, реализовать обратный перевод – из килограммов в фунты.
kilogramm = float(input())
pounds = kilogramm * 2.204
print(round(pounds, 2))