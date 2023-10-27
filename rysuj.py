from funkcje import kwadrat, trojkat, menu

while True:
    menu()

    wybor = input("Jaki ksztalt chcesz narysowac: ")

    if wybor == "1":
        print("Wybrales kwadrat")
        kwadrat()
    elif wybor == "2":
        print("Wybrales trojkat")
        trojkat()
    elif wybor == "3" or wybor == "q" or wybor == "Q":
        print("Wychodzisz z programu")
        break
    else:
        print("Nie ma takiej opcji!")