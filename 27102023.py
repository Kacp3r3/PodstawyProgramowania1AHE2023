# Przykładowe rozszerzenia pliku .txt .png .mp3 .mp4

#Jak system operuje na plikach
#Uchwyt

#Prosty przykład
# file = open("example.file", "rt")

# zawartosc = file.readlines()

# print(zawartosc)

# file.close()




#try:
    #a = int(input("Podaj A: "))
    #b = int(input("Podaj B: "))
    #print(a/b)
#except ZeroDivisionError:
#    print("Proba dzielenia przez zero!!!!")



#Poprawny sposób
# with open as f
#Czytanie z pliku
# with open("example.file", "rt") as file:
#     zawartosc = file.readlines()
#     print(zawartosc)


# #Zapisywanie danych do pliku
# with open("output.file", "a") as file:
#     user_input = input("Podaj jakis tekst: ")
#     file.write(user_input)
#     file.write("\n")


# wynik = 0
# user_answer = ""
# good_answer = ""
# with open("questions.quiz", "rt") as f:
#     questions_nr = int(f.readline()) #Wczytanie liczby pytan, pierwsza linijka
    
#     for i in range(questions_nr):
#         pytanie = f.readline()
#         odpA = f.readline()
#         odpB = f.readline()
#         odpC = f.readline()
#         odpD = f.readline()
#         good_answer=f.readline()

#         print(pytanie, odpA, odpB, odpC, odpD, sep="")
#         user_answer = input("Podaj odpowiedz: ")

#         if user_answer == good_answer:
#             wynik += 1
#             print("Poprawna odpowiedz")
#         else:
#             print("Bledna odpowiedz")

#     print("Twoj wynik to", wynik, "na", questions_nr, "możliwych punktow")


#Witaj w programie
#1. Podaj swoje dane
#2. Pokaz moje dane

#w Przypadku 1
# Program zapyta o imie nazwisko wiek

#w Przypadku 2
# Program wypisze nasze dane na ekranie
# Imie: xyz Naziwsko: xyz Wiek: x lat


# while True:
#     print("Witaj w programie")
#     print("1. Podaj swoje dane")
#     print("2. Pokaz moje dane")


#     user_choice = input(">")

#     match user_choice:
#         case "1":
#             imie = input("Podaj imie: ")
#             nazwisko = input("Podaj nazwisko: ")
#             wiek = input("Podaj wiek: ")

#             with open("dane", "wt") as f:
#                 f.write(imie + "\n")
#                 f.write(nazwisko + "\n")
#                 f.write(wiek + "\n")
        
#         case "2":
#             with open("dane", "rt") as f:
#                 imie = f.readline()
#                 nazwisko = f.readline()
#                 wiek = f.readline()

#             print(imie, end="")
#             print(nazwisko, end="")
#             print(wiek.rstrip("\n"))
#         case _:
#             print("wyjscie")
#             break



# A B C D
# Przesuniecie = 2
# C D E F


file_name = input("Podaj nazwe pliku do wczytania tekstu: ")
przesuniecie = int(input("Podaj przesuniecie: "))

zakodowany_tekst = ""
with open(file_name, "rt") as f:
    tekst = f.read()
    for litera in tekst:
        #ord(znak)
        #chr(liczba)
        #if litera != " " and litera != "\n":
        if litera not in ["\n", " ", "\t"]:
            if ord(litera) >= 97:
                #Mamy doczynienia z mala litera
                litera = ord(litera)# Zamiana na liczbe
                litera += przesuniecie # Dodanie przesuniecia
                #Sprawdzamy czy wyszlismy poza zakres
                if litera > 122:
                    reszta = litera%122
                    litera = 97 + reszta - 1
                zakodowany_tekst += chr(litera) # Zamiana spowrotem na znak i dodanie na koniec zmiennej
            else:
                litera = ord(litera)# Zamiana na liczbe
                litera += przesuniecie # Dodanie przesuniecia
                #Sprawdzamy czy wyszlismy poza zakres
                if litera > 90:
                    reszta = litera%90
                    litera = 65 + reszta - 1
                #Mamy doczynienia z duza litera
                zakodowany_tekst += chr(litera)
            
        else:
            zakodowany_tekst += litera
with open("tekst.zakodowany", "wt") as f:
    f.write(zakodowany_tekst)

# z - 122
# +3
# 122+3
# 125
# if 125 > 122:
#  125%122 = 3
#  97+3-1
# c - 99