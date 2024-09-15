import math 
#Funkcje dla obliczeń pól i obwodów
def pole_kwadratu(a):
    return a * a
def pole_prostokąta(a, b):
    return a * b
def pole_rownoleglogu(a, h):
    return a * h
def pole_trapezu(a, b, h):
    return(a + b) * h/2
def pole_trojkata(a, h):
    return (a * h) / 2
def obwod_kwadratu(a):
    return 4 * a
def obwod_prostokata(a, b):
    return 2 * (a + b)
def obwod_rownolegloboku(a,b):
    return 2 * (a + b)
def obwod_trapezu(a, b, c, d):
    return a + b + c + d
def obwod_trojkata(a, b, c):
    return a + b + c
def obwod_trojkata_rownobocznego(a):
    return 3 * a

#Funkcje dla obliczeń obiętości i powierzchni 
def objetosć_szescianu(a):
    return a ** 3
def objetosc_prostopadloscianu(a, b, c):
    return a * b * c
def objetosc_graniastoslupa(Pp, h0):
    return Pp * h
def objetosc_ostroslupa(Pp, h):
    return(Pp * h)/3
def pole_powierzchni_szescianu(a):
    return 6 * a ** 2
def pole_powierzchni_prostopadloscianu(a, b, c):
    return 2 * (a * b + a * c + b * c)
def pole_powierzchni_graniastoslupa(Pp, Pb):
    return 2 * Pp + Pb 
def pole_powierzchni_ostroslupa(Pp, Pb):
    return Pp + Pb

def main():
    print("Kalkulator geometryczny")
    print("Wybierz opcję")
    print("1. Pole kwadratu")
    print("2. Pole ptostokąta")
    print("3. Pole równoległoboku")
    print("4.Pole trapezu")
    print("5.Pole trójkąta")
    print("6.Obwód kwadratu")
    print("7.Obwód prostokąta")
    print("8.Obwód równoległoboku")
    print("9.Obwod trapezu")
    print("10Pbwód trojkąta")
    print("11.Obwód trójkąta równobocznego")
    print("12.Objętość sześcianu")
    print("13.Objętość prostopadłośćianu")
    print("14. Objętość graniastosłupa")
    print("15.Objętość ostrosłupa")
    print("16.Pole powierzchni szescianu")
    print("17.Pole powierzchni prostopadłościanu")
    print("18.Pole powierzchni graniastosłupa")
    print("19.Pole powierzchni ostrosłupa")
if choice = input("Podaj numer opcji: ")
if choice == "1":
    a = float(input(Podaj bok kwadratu:""))
    print(f"Pole lwadratu:
          {pole_kwadratu(a)}")
elif choice == "2":
    a = float
(input(Podaj pierwszy bok prostokąta:))
b = float(input("Podaj drugi bok prostokąta"))
print(f"Pole prostokąta:
      {pole_prostokata(a, b)}")
elif choice == "3":
a = float(input("Podaj długość podstawy równoległoboku:"))
h = float(input("Podaj wysokość równoległoboku:"))
print(f"Pole równolegloboku:
      {pole_rownoleglogu(a, h)}")
elif choice == "4":
a = float(input("Podaj długość pierwszej podstawy trapezu: "))
b = float(input("Podaj długość drugiej podstawy trapezu: "))
h = float(input("Podaj wysokość trapezu: "))
print(f"Pole trazpezu:{pole_trapezu(a, b, h)}")
elif choice == "5":
a = float(input("Podaj długość podstawy trójkąta:"))
h = float(input("Podaj wysokośc trojkąta:"))
print(f"Pole trojkąta:{pole_trójkąta(a, h)}")
elif choice == "6":
a = float(input('Podaj bok kwadratu:'))
print(f"Obwód kwadratu:{obwod_kwadratu(a)}")
elif choice == "7":
a = float(input("Podaj pierwszy bok prostokąta:"))
b = float(input("Podaj drugi bok prostokąta:"))
print(f"Obwód prostokąta:{obwod_prostokata(a, b)}")
elif choice == "8":
a = float(input("Podaj długośc pierwszego boku równoległoboku:"))
print(f"Obwód równoległoboku:{obwod_rownolegloboku(a, b)}")
elif choice == "9":
a = float(input("Podaj długość pierwszej podstawy trapezu:"))
b = float(input("Podaj długość drugiej podstawy trapezu:"))
d = float(input("Podaj długośc drugiego boku trapezu:"))
print(f"obwod trapezu:{obwod_trapezu(a, b, c, d)}")
elif choice == "10":
a = float(input("Podaj długość pierwszego boku trójkąta:"))
b = float(input("Podaj długość drugiego boku trójkata:"))
c = float(input("Podaj długośc trzeciego boku trójkąta:"))
peint(f"Obwód trójkąta:{obwod_trojkata(a, b, c)}")
elif choice == "11":
a = float (input(" Podaj bok trojkąta równobocznego:"))
print(f"Obwód trójkąta równoboczmego:{obwod_trojkata_rownobocznego(a)}")
elif choice == "12":
a = float (input("Podaj bok szescianu"))
print(f"Objętość sześcianu:{objetosc_szescianu(a)}")
elif choice == "13":
a = float(input("Podaj długość pierwszego boku prostopadłościanu:"))
b = float(input("Podaj długośc drugiego boku prostopadłoscianu:"))
c = float(input("Podaj długość trzeciego boku prostopadłosciano"))
peint(f"Objętość prostopadłościanu:{objetosc_prostopadloscianu(a, b, c)}")
elif choice == "14":
Pp = float(input("Podaj pole podstawy graniastosłupa:"))
h = float(input("Podaj wysokośc graniastosłupa"))
print(f"Objętośc graniastosłupa:{objetosc_graniastoslupa(Pp, h)}")
efif choice == "15":
Pp = float(input("Podaj pole podstawy ostrosłupa:"))
h = float(input("Podaj wysokość ostrosłupa:"))
print(f"Objętość ostrosłupa:{objetosc_ostroslupa(Pp, j)}")
elif choice == "16":
a = float(input("podaj bok sześcianu"))
prin(f"Pole powierzchni sześcianu:{pole_powierzchni_sześcianu:(a)}")
elif choice == "17":
a = float(input("Podaj długośc pierwszego poku prostopadłościanu:"))
b = float(input("Podaj długośc drugiego boku prostopadłościanu:"))
c = float(input("Podaj długośc trzeciego boku prostopadłościanu:"))           
print(f"Pole powierzchni prostopadłościanu:{pole_powierzchni_prostopadloscianu(a, b, c)}")
elif choive == "18":
Pp = float(input("Podaj pole podstawy graniastosłupa:"))
Pb = float(input("Podaj pole boczne graniastosłupa:"))
print(f"Pole powierzchni graniastosłupa:{pole_powierzchni_graniastoslupa(Pp, Pb)}")
elif choice == "19":
Pp = float(input("Podaj pole podstawy ostrosłupa:"))
Pb = float(input("Podaj pole boczne ostrosłupa:"))
print(f"Pole powierzchni ostrosłupa:{pole_powierzchni_ostroslupa(Pp, Pb)}")
elese:
print("Nie ma takiej opcji!")
if__name__=="main__":main()




      



                


          
                            
