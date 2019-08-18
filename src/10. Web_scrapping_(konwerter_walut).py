# coding = <utf-8>
import requests
from bs4 import BeautifulSoup

def value_convert(currency):


    if currency == 1:
        currency = "usd"
    elif currency == 2:
        currency = "eur"
    elif currency == 3:
        currency = "gbp"
    elif currency == 4:
        currency = "chf"
    elif currency == 5:
        currency = "dkk"
    elif currency == 6:
        currency = "cad"
    elif currency == 7:
        currency = "aud"
    elif currency == 8:
        currency = "try"
    elif currency == 9:
        currency = "pln"
    else:
        currency = "usd"
    return currency

def wchih_value():
    while 1:
        try:
            print("Dolar(1)")
            print("Euro(2)")
            print("Funt(3)")
            print("Frank Szwajcarski(4)")
            print("Korona Duńska(5)")
            print("Dolar Kanadyjski(6)")
            print("Dolar Australijski(7)")
            print("Lira Turecka(8)")
            currency = int(input("Zloty Polski(9):"))

            if currency > 0 and currency < 10:
                break
            else:
                print("zla liczba!")
        except ValueError:
            print("Uch! to nie jest poprawna liczba! Spróbuj jeszcze raz...")


    currency = value_convert(currency)
    return currency

def exchange_import_from_page(currency, currency_1):
    p = {"s": currency + currency_1}
    odpowiedz = requests.get("http://stooq.pl/q/?", params=p)
    soup = BeautifulSoup(odpowiedz.text, 'html.parser')
    exchange_mark = soup.find("span", id=f"aq_{currency}{currency_1}_c5")
    exchange = float(exchange_mark.text)
    return exchange

def convert():
    print("             Konwertuj z:")
    currency = wchih_value()
    print("             Konwertuj na:")
    currency_1 = wchih_value()
    if currency != currency_1 :
        exchange = exchange_import_from_page(currency,currency_1)
        print(f"            1{currency} ="+" {:.4f}".format(exchange)+f"{currency_1}")
        #money_ = input(f"Wprowadz wartosc {currency} ")

        while 1:
            try:
                money_ = float(input("Proszę wprowadzić liczbę: "))
                break
            except ValueError:
                print("Uch! to nie jest poprawna liczba! Spróbuj jeszcze raz...")

        money = float(money_)
        output = float(money) * float(exchange)
        print("             {:.2f}".format(money) + f"{currency} = " + "{:.2f}".format(output) + f"{currency_1}" )
    else:
        print("1{} = 1{}".format(currency, currency_1))

def money_converter():
    while True:
        while 1:
            try:
                option = int(input("Convert(1) Out(0)"))
                if option >=0 and option<2:
                  break
                else:
                    pass
            except ValueError:
                pass
        if option == 1:
            convert()
        elif option == 0:
            break

def main():
    money_converter()

if __name__ == "__main__":
    money_converter()