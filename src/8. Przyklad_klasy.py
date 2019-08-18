import math
import cmath

class Funkcja_kwadratowa:
    ile_funkcji = 0
    def __init__(self, a=1,b=2,c=-3):
        self.a = a
        self.b = b
        self.c = c
        Funkcja_kwadratowa.ile_funkcji+=1
        self.nr = Funkcja_kwadratowa.ile_funkcji
        print(f"To jest funkcja {self.nr}")
        print("Funkcja {}x^2+{}x+{} zostala stworzona".format(self.a,self.b,self.c))
        
    def __del__(self):
        print(f"Funkcja {self.nr} została zniszczona")
        Funkcja_kwadratowa.ile_funkcji-=1

    def Solve(self):
        if(self.a == 0):
            print("Nie jest to funkcja kwadratowa!")
        else:
            delta = pow(self.b,2)-4*self.a*self.c
            if(delta > 0):
                pierw_delta = math.sqrt(delta)
                x1 = (-self.b + pierw_delta)/(2*self.a)
                x2 = (-self.b - pierw_delta)/(2*self.a)
                print("Rozwiazaniami funkcji kwadratowej {}x^2+{}x+{} są:".format(self.a, self.b, self.c))
                print("x1 = {:.2f}, x2 = {:.2f}".format(x1,x2))
            elif(delta == 0):
                x1 = (-self.b)/(2*self.a)
                print("Funkcja {}x^2+{}x+{} posiada jedno rozwiązanie i jest nim:".format(self.a, self.b, self.c))
                print("x = {}".format(x1))
            elif(delta <0):
                pierw_delta = cmath.sqrt(delta)
                x1 = (-self.b + pierw_delta) / (2 * self.a)
                x2 = (-self.b - pierw_delta) / (2 * self.a)
                print("Funkcja nie ma rozwiązań rzeczywistych. Rozwiazaniami funkcji kwadratowej {}x^2+{}x+{} są:".format(self.a, self.b, self.c))
                print("x1 = {:.2f}, x2 = {:.2f}".format(x1,x2))

    @staticmethod
    def How_many_functions():
        return Funkcja_kwadratowa.ile_funkcji

def main():
    a = Funkcja_kwadratowa(1,1,1)
    b = Funkcja_kwadratowa(12,4,-4)
    a.Solve()
    b.Solve()
    print(Funkcja_kwadratowa.How_many_functions())

if __name__ == "__main__":
    main()
