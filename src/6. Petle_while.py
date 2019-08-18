liczba = 0

while liczba < 4:
    print(liczba)
    liczba+=1
print('-------------')

###########################
#break
liczba_ = 0

while True:
    print(liczba_)
    liczba_+=1
    if liczba_ > 4:
        break
print('-------------')

##########################
#continue
liczba__ = 0

while liczba__ < 10:
    liczba__+=1
    if liczba__ %2 == 0:
        continue
    print(liczba__)