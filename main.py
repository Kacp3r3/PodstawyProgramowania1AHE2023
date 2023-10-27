



# liczba = 5
# zmiennoprzecinkowa = 2.1
# napis = "Hello"
# litera = '*'
# foo = True
# bar = False

# suma = liczba + zmiennoprzecinkowa

# foo = napis * liczba

# print(foo)


# lista = [4,5,6,7,8,9]

#print(lista[2])


#Pętla wypisująca elementy z tablicy
# for i in range(len(lista)):
#     print(lista[i])


# a = 5
# while a < 15:
#     print("*")
#     a = a + 1


# id = input("Podaj nazwe uzytkownika: ")
# password = int(input("Podaj haslo: "))

# if id  == "kacper" and password == 420:
#     print("Przyznano dostep")
# elif id == "abc" and password == "def":
#     print("Przyznano dostep abcd")
# else:
#     print("Bledne haslo lub nazwa uzytkownika")




# import random

# wylosowana_liczba = random.randint(0,1000)
# input_uzytkownika = -1

# print("Wylosowalem: ", wylosowana_liczba)

# while True:
#     input_uzytkownika = int(input("Podaj mi liczbe: "))

#     if input_uzytkownika > wylosowana_liczba:
#         print("Podales wieksza liczbe!")
#     elif input_uzytkownika < wylosowana_liczba:
#         print("Podales mniejsza liczbe!")
#     else:
#         break

# print("Wygrales!")


# l1 = 10
# l2 = 24
# l3 = 100
# l4 = 120

# if l1 > l2 and l1 > l3:
#     print("Najwieksza jest liczba 1 i ma wartosc", l1)
# elif l2> l1 and l2 > l3:
#     print("Najwieksza jest liczba 2 i ma wartosc", l2)
# else:
#     print("Najwieksza jest liczba 3 i ma wartosc", l3)



liczby = [10,12,1,42,50,102,320,4444]

maks = liczby[0]

for i in range(len(liczby)):
    if liczby[i] > maks:
        maks = liczby[i]


print("Maks w zbiorze to:", maks)







