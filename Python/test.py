
import funkcje.plaskie as pl
import funkcje.warunki_tr as tr
import funkcje.bryly as br


def legenda() -> None:
    print("a - bryly")
    print("b - plaskie")
    print("c - warunki tr")
    print("e - wyjdz z programu")


def main() -> None:
    while True:
        legenda()
        inp = input("Wybierz opcje: ").lower().strip()

        if inp == "a":
            br.bryly()
        elif inp == "b":
            pl.plaskie()
        elif inp == "c":
            tr.trojkaty()
        elif inp == "e":
            print("Program zakonczyl dzialanie")
            break
        else:
            print("Nie ma takiej komendy")


# ------------------------------------------
main()
