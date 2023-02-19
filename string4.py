#4) Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef".

s = input('Tekst kiritin: ')
new_string = ''.join(s.split())
# for i in range(len(new_string)):
n = s.find(s[0])
print(n)
