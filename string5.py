#5) Найти в строке указанную подстроку и заменить ее на новую.
# Строку, ее подстроку для замены и новую подстроку вводит пользователь.

s = input('Tekst kiritin: ')
a = input('Tekst bolegin kiritin: ')
b = input('Taza qatar kiritin: ')
if a in s:
    print(s.replace(a, b))