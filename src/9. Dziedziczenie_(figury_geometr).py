from abc import ABC, abstractmethod
import math

class Figura(ABC):
    ile = 0
    def __init__(self, name):
        self.name = name
        Figura.ile+=1
        self.nr = Figura.ile
        print(f"Stworzylem {self.whitch_figure()} {self.name} nr.{self.nr}")

    def __del__(self):
        print(f"Niszcze {self.whitch_figure()} {self.name} nr.{self.nr}")
        Figura.ile -=1

    @abstractmethod
    def pole(self):
        pass

    @abstractmethod
    def obwod(self):
        pass
    @abstractmethod
    def whitch_figure(self):
        pass

    def whats_your_name(self):
        return self.name

    def przedstaw_sie(self):
        print("Jestem {} o imieniu {}. Mam obwod {:.2f} i pole {:.2f}".format(self.whats_your_name(),self.name, self.obwod(), self.pole()))


class Kwadrat(Figura):
    def __init__(self,name,a):
        super().__init__(name)
        self.a = a

    @property
    def a(self):
        return self.__a
    @a.setter
    def a(self,a):
        if a <=0:
            self.__a = 0.1
        elif 0<a<100:
            self.__a = a
        else:
            self.__a = 100

    def __del__(self):
        super().__del__()

    def whitch_figure(self):
        return "Kwadrat"

    def obwod(self):
        return 4*self.a

    def pole(self):
        return self.a*self.a

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f"Mam bok o dlugosci {self.a}")

class Prostokat(Kwadrat):
    def __init__(self,name,a,b):
        super().__init__(name,a)
        self.b = b

    def __del__(self):
        super().__del__()

    @property
    def b(self):
        return self.__b
    @b.setter
    def b(self,b):
        if b <=0:
            self.__b = 0.1
        elif 0<b<100:
            self.__b = b
        else:
            self.__b = 100

    def whitch_figure(self):
        return "Prostokat"

    def obwod(self):
        return (2*self.a)+(2*self.b)

    def pole(self):
        return self.a*self.b

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f"A drugi bok mam dlugosci {self.b}")

class Kolo(Figura):
    def __init__(self,name,x,y,r):
        super().__init__(name)
        self.x = x
        self.y = y
        self.r = r

    def __del__(self):
        super().__del__()

    @property
    def r(self):
        return self.__r
    @r.setter
    def r(self, r):
        if r <= 0:
            self.__r = 0.1
        elif 0 < r < 100:
            self.__r = r
        else:
            self.__r = 100

    def whitch_figure(self):
        return "Kolo"

    def pole(self):
        return (2*math.pi*self.r)
    def obwod(self):
        return (math.pi * pow(self.r, 2))
    def przedstaw_sie(self):
        super().przedstaw_sie()
        print("Srodek znajduje sie w punkcie ({:.2f},{:.2f}), a promien jest dlugosci {:.2f}".format(self.x,self.y,self.r))




def main():
    A = Kwadrat("kwadracik",5)
    B = Prostokat("prostokacik", 120, -3)
    C = Prostokat("prostokat2", 12.4, 1.23)
    D = Kolo("kolko",2,1.5,4)

    lista_figur = [A,B,C,D]

    for figury in lista_figur:
        figury.przedstaw_sie()
        print("\n")


if __name__ == "__main__":
    main()

