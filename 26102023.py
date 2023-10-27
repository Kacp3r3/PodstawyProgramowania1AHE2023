zmienna = 10

# liczby całkowite            int (5)
# liczby zmiennoprzecinkowe   float, double (25.3)
# Znak                        char ( 'A' )     
# Łańcuchy znaków             string ( "Example string" )
# Typ logiczny                bool (True/False)


# 'A' = 1 Bajt
# "A" = 2 Bajt = 'A' '\0'

# "ABC" = 4 Bajty = 'A' 'B' 'C' '\0'


#Funkcja ( argumenty):
print("Hello World", 25, zmienna, 25.3, [2,3,4])
print("Hello World", 25, zmienna, 25.3, [2,3,4], sep="-",)

# 'A' = 65
# 'a' = 97

A = 'A'
a = 'a'


#Castowanie/Rzutowanie - Zmiana jednego typu danych na inny
print(A,a)
#Chcemy zobaczyć liczbową reprezentacje znaków A i a
print(ord(A), ord(a) )   #ord() zamiana znaku na liczbę
print(chr(65), chr(97) ) #chr() zamiana liczby na znak

tekst = "255"
liczba = int(tekst)
print("Typ zmiennej tekst = ",  type(tekst)  ) #funkcja type() mówi jakiego typu jest dana zmienna
print("Typ zmiennej liczba = ",  type(liczba)  )


print( type(25) ) #Int
print( type(25.5) ) #Float
print( type(True) ) #Bool
print( type([]) ) # List


# foo = input("Podaj mi imie: ")

# print(type(foo))
# print("Cześć", foo)

#liczba1 = int(input("Podaj mi numer miesiaca: "))
#liczba2 = float(input("Podaj mi numer od 0.0 do 1.0: "))


a = 5
b = 2
print(type(a))
print(type(b))

dzialanie = a/b

print(type(dzialanie))
print(dzialanie)



#operatory
# wyraz z lewej      operator     wyraz z prawej
#      10               >             15
# Wyrazenie powyzej zwroci nam wartość False - Fałsz
#      20                >            15
# Wyrażenie zwróci nam True - Prawda

# <, <=
# >, >=
# ==
# !=
# not
# and
# or
budzet = 10
wiek = 18

kosztFilmu = 5
minimalnyWiek = 16

if budzet >= kosztFilmu  and  wiek >= minimalnyWiek:
    print("Mozesz wejsc do kina")
else:
    print("Nie mozesz wejsc do kina")




# ocena1 = 5
# ocena2 = 3
# ocena3 = 4

#Elementy listy numerujemy od zera
# oceny = [5,3,4]
# oceny[0] -> 5
# oceny[1] -> 3
# oceny[2] -> 4

# range(liczba) -> [x,y,z]
# range(4) - > [0, 1, 2, 3]

for i in range(10):
    print(i)


oceny = [5,4,3,2,5,5,5,3]

suma = 0
for ocena in oceny:
    suma += ocena

print(suma/len(oceny))

# for i in range(len(oceny)):
#     suma += oceny[i]


# x = input("Podaj litere: ")

# match x:
#     case "A":
#         print("Podałeś A")
#     case "B":
#         print("Podałeś B")
#     case _:
#         print("Nienznay input")



#def nazwa_funkcji(arguemnt1, argument2):
def example_function(example_arg_1 = 10, example_arg_2= 55):
    #print("Wywołuje funkcję example_function")

    dzialanie = example_arg_1/example_arg_2
    dzialanie = dzialanie*5

    #print("Koniec funkcji example_function")

    return dzialanie



print(example_function(5,10))
zmiennaA = example_function(example_arg_2=10, example_arg_1=5)
zmiennaB = example_function()

print(zmiennaA/zmiennaB)



# 0   1    1    0
#2^3 2^2  2^1  2^0
# 8   4    2    1 

# 6


# 1   1    0    1
#2^3 2^2  2^1  2^0
# 8   4    2    1 

#13


dziesietna = 10
szesnastkowo = 0xAF
binarna = 0b10000100

#0b10000100
#0b00100001

if ( binarna>>2 ) & 1:
    print("Grzane fotele wlaczone")


#0b10000100
#0b00000100
#&
#0b00000100 - > True


#0b10000000
#0b00000100
#&
#0b00000000 - > False


if binarna & 4:
    print("Grzane fotele wlaczone")

if ( binarna >> 7)&1:
    print("Aktywny temponat wlaczony")

if binarna&128:
    print("Aktywny temponat wlaczony")




binarnalewo = 0b00000001
print(binarnalewo)

#0b00000001<<3
#0b00001000
print(binarnalewo<<3)

#0b00000001<<3
#0b00100000
print(binarnalewo<<5)


"""
Napisz program, który prosi o podanie współczynników równania kwadratowego ax2 +bx+c = 0 i wypisuje
rozwiązania równania (lub informację o braku rozwiązań).
"""
import math

a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b+ math.sqrt(delta))/2*a
    x2 = (-b- math.sqrt(delta))/2*a

    print("Miejsca zerowe funkcji kwadratowej: ", x1, x2)

elif delta == 0:
    x0 = -b/(2*a)

    print("Miejsce zerowe funkcji kwadratowej: ", x0)

else:

    print("Funckja kwadratowa nie ma miejsc zerowych")





#Napisz program, który oblicza pole i obwód koła o promieniu podanym przez użytkownika

# r = int(input("Podaj promien kola: "))

# print("Pole koła wynosi: ", 3.14*r**2)
# print("Obwód koła wynosi: ", 2*3.14*r)



#Napisz funkcje obliczające silnię liczby podanej jako argument

# 3! = 3*2*1
# 5! = 5*4*3*2*1

# def silnia(liczba):
#     wynik = liczba
#     while liczba > 1:
#         liczba = liczba - 1
#         wynik = wynik*liczba
#     return wynik

# print(silnia(5))

"""
Napisz program, który prosi o podanie liczby naturalnej, a następnie wypisuje z ilu cyfr składa się wpisana wartość, 
a także informację o sumie tworzących ją cyfr. Dla uproszczenia załóż, że podana liczba jest
poprawna (czyli rzeczywiście naturalna).

"""


# 323 - 3 cyfry
# 323 - suma: 8

#   323 % 10 = 3
#   323 / 10 = 32
#   32 % 10 = 2
#   32 / 10 = 3

# number = int(input("Podaj liczbe naturalna: "))
# cyfry = []
# sumaCyfr = 0
# while number > 0:
#     cyfry.append(number%10)
#     number = int(number/10)
#     sumaCyfr += cyfry[-1] #Python pozwala na indeksy ujemne ( od konca tablicy )

# print("Suma cyfr: ", sumaCyfr)
# print("Cyfry z jakich sie sklada: ", cyfry[::-1])