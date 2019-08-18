#funkcja wykonujaca jakies czynnosic, ta akurat nie ma argumentow
def witaj_swiecie():
    print("Hello, world!")

#funkcja jednoargumentowa zracajaca wartosc
def potega_kwadratowa(x):
    return x*x

#funkcja dwuargumentowa zwracajaca wartosc
def Ktora_wieksza(x,y):
    if x>y:
        return x
    elif x<y:
        return y
    else:
        return True

#wywolywanie funkcji przez funkcje
def Jaka_jest_ta_liczba(x,y):
    decyzja = Ktora_wieksza(x,y)
    if decyzja == x:
        print("Wiekszy jest x, {}".format(x))
    elif decyzja == y:
        print("Wieksza jest y, {}".format(y))
    else:
        print("Liczby sa rowne")

#rekurencja
def silnia(n):
    if n == 0:
        return 1
    else:
        return n*silnia(n-1)





witaj_swiecie()
print(potega_kwadratowa(2))
Jaka_jest_ta_liczba(3,2)

print(silnia(2))
