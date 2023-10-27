# print("Hello world!")

# imie = input("Podaj swoje imie: ")
# wiek = input("Podaj swoj wiek: ")

# print("Witaj", imie, "masz", wiek, "lat")

#Zapytaj uzytkownika o jego ulibioną potrawę i film lub grę
#i wyświetl jego odpowiedzi na konsoli

# film = input("Jaki jest twój ulubony film: ")
# gra = input("Jaka jest twoja ulubiona gra: ")

# print("Twoj ulubiony film to", film, "a gra", gra)











#Popros uzytkownika o podanie liczby i wykorzystaj ją w petli
#uzyj funkcji int() aby zmienic tekst na liczbe
# slowo = input("Podaj mi swoje imie: ")
# ile_razy = int(input("Ile razy: "))

# for i in range(ile_razy):
#     print(slowo)









# a = int(input("Podaj a: "))
# b = int(input("Podaj b: "))

# znak_krawedzi = input("Podaj znak krawedzi ")
# znak_wypelniania = input("Podaj znak wypelnienia ")

# for j in range(b):
#     for i in range(a):
#         #   True lub False lub  False  lub  False
#         if j == 0 or i == 0 or j == b-1 or i == a-1:
#             print(znak_krawedzi, end="")
#         else:
#             print(znak_wypelniania, end="")
#     print()

#Do powyzszego kodu dodaj dwie zmienne, wartosci pobierz od uzytkownika
#Zmienne te maja definiowac z czego sie sklada rysowany prostokąt




#Zmodyfikuj kod tak aby wyswietlil liczby nieparzyste od 1 do 100

#        range(start, stop, krok)


# for i in range(1, 100, 2):
#     # if i % 2 == 0:
#     #     print(i, end = " ")
#     print(i, end = " ")



# 10 % 3 = 1

# 10 - 3 = 7 -> 7>3 -> tak
# 7-3 = 4 -> 4>3 -> tak
# 4-3 =1 -> 1>3 -> nie 
# Wynik = 1


# a = int(input("Podaj a: "))

# # a=3    range = [0,1,2]
# for wiersz in range(a):
#     for kolumna in range(wiersz+1):
#         #  1 wiesz        ostatni wiersz   pierwsza kolumna
#         if wiersz == 0 or wiersz == a-1  or kolumna == 0 or kolumna == wiersz:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()




def add(a, b):
    return a+b

def sub(a, b):
    return a-b

print(add(5,7))
print(add(10,12))











