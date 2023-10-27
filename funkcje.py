#def nazwa()
def kwadrat():
    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))

    znak_krawedzi = input("Podaj znak krawedzi ")
    znak_wypelniania = input("Podaj znak wypelnienia ")

    for j in range(b):
        for i in range(a):
            if j == 0 or i == 0 or j == b-1 or i == a-1:
                print(znak_krawedzi, end="")
            else:
                print(znak_wypelniania, end="")
        print()

def trojkat():
    a = int(input("Podaj a: "))
    for wiersz in range(a):
        for kolumna in range(wiersz+1):
            if wiersz == 0 or wiersz == a-1  or kolumna == 0 or kolumna == wiersz:
                print("*",end="")
            else:
                print(" ",end="")
        print()

def menu():
    print("Witaj w programie rysuj")
    print("1. Kwadrat")
    print("2. Trojkat")
    print("3. Wyjdz")