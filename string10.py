#10) Посчитать количество строчных (маленьких) и прописных (больших)
# букв в введенной строке. Учитывать только английские буквы.

s = input('Tekst kiritin: ')
count1 = 0
count2 = 0
for i in range(len(s)):
    if s[i].islower():
        count1 += 1
    elif s[i].isupper():
        count2 += 1
print(f"строчных букв {count1}, прописных букв {count2}")