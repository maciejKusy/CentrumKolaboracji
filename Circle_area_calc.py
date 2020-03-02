PI = 3.141592   # Deklarując te zmienna w funkcji tworzysz ja przy kazdym wykonaniu, w rzeczywistosci wystarczy utworzyc
                # ja raz przy uruchomieniu programu, co prawda lepiej uważać na globalne zmienne, ale maja swoje zastosowania.
                # Do tego, istnieje konwencja - w roznych jezykach - ze nazwy stałych / constów są pisane uppercase, ale naturalnie nie ma przymusu


def circle_area(radius):
    return PI * (float(radius) ** 2)    # Python ma skrocony zapis podnoszenia do potegi - przydatna sprawa.
                                        # Imo najlepsze sa czyste funkcje (pure function) bez efektów ubocznyc (np. printowania wartosci, modyfikowania argumentów, etc.)
                                        # takie najłatwiej się reużywa w wielu miejsach i łątwiej je testowac. daltego usunalem tego printa.
                                        # Co do krótkich nazw zmiennch, takich jak np 'x', łątwo sie to pisze, ale jak wrócisz do kodu za pół roku to możesz mieć problem :P
                                        # dla komputera to wszystko jedno, także lepiej pisać zrozumiale dla ludzi


def is_invalid_input(input):                        # tworzac funkcje pomocnicze, kod staje sie bardzie czytelny, szczególnie jak warunki stają sie bardzo skomplikowane
    return input.isalpha() or float(input) < 0      # na tym przykładzie można wymyślić wiecej invalid input, np. '1a2', etc. wiec ta funkcja by sie rozrastala, ja dodalem tylo warunek liczby dodatniej.


def is_user_leaving(input):     # Można by pewnie stwierdzić, że taka odzielna funkcja to overkill, ale lepiej mieć dużo małych funkcji, niż kilka skomplikowanych, ułatwia to rozumowanie
    return input == "q"         # Przy funkcjach zwracajacych booleany, istnieje crossjezykowa konwencja żeby miały forme pytania, zaczynały sie od is, are, has, etc.


def process_user_query(question, calculation, answer):      # warto tworzyć troszke bardziej abstraksyjne funkcje, tak żeby można je było użyć z różnymi danymi
    while True:                                             # pewnie że to może już przesada, ale na dobrą sprawe mozna tego uzyc rowniez w sphere_volume_calc.py albo innym kalkulatorze
        user_input = input(question).lower()

        if is_user_leaving(user_input):
            break
        elif is_invalid_input(user_input):
            print("Sorry, incorrect input, try again.\n")
            continue
        else:
            result = calculation(user_input)
            print(answer.format(user_input, round(float(result), 4)))   # przeniosłem sobie printa z wynikiem tutaj, teraz cała podstawowa komunikacje z userem mam w jednej funkcji, a pozostale
                                                                        # zwracaja mi tylko wartości


def circle_area_calculator():       # te funkcje wydzieliłem tylko po to, zeby reszta mogła byc bardziej generyczna i reuzywalna
    question = """Enter radius value in cm
    or enter Q to quit: \n"""
    answer = "The area of a wheel with a radius of {}cm is {}cm2.\n"    # Python ma kilka sposów łączenia strignów i interpolacji, łączenie z '+' jest absolutnie poprawne, ale imo sa czytelniejsze formy

    process_user_query(question, circle_area, answer)


circle_area_calculator()
