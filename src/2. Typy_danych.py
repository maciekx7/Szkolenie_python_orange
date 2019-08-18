#Jaki typ ma zmienna? Funkcja type(zmienna)

#string - bylo

#INT
x = 5
print(f'x = {x}, {type(x)}')

#FLOAT
y = 3.2
print(f'y = {y}, {type(y)}')

#COMPLEX
z = 3+2j
print(f'z = {z}, {type(z)}')

#BOOL
l = True
print(f'l = {l}, {type(l)}')

#LISTA
print()
print("-----------------------------")
list = []
print(f'list = {list}, {type(list)}')
list.append(x)
print(list)
list.append(z)
list.append(y)
print(list)
list.clear()
print(list)

print("-----------------------------")
print()
#slownik

dic = {'key1': 120, 'key2': 254, 'alfabet': 24 }
print(f'dic = {dic}, {type(dic)}')
klucze = dic.keys()
print(klucze, type(klucze))




