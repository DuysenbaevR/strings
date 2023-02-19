#2) Вводится строка, состоящая из букв и пробелов.
# Составить из входящих в нее букв несколько любых их сочетаний (слов) любой длины.
# Каждую букву строки можно использовать неограниченное количество раз.
import random

s = input('Tekst kirtin: ')
n = int(input('Neshe soz payda etiw kerek: '))
new_string = ''.join(s.split())
for i in range(n):
    print(new_string[0:random.randrange(len(new_string))])