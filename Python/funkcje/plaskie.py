
from math import pi as PI


# Pola pp
def pp_kwadartu(a: float) -> float:
    return a**2


def pp_prostokata(a: float, b: float) -> float:
    return a*b


def pp_rownolegloboku(a: float, h: float) -> float:
    return a*h


def pp_trapezu(a: float, b: float, h: float) -> float:
    return (a+b)*h*0.5


def pp_trojkata(a: float, h: float) -> float:
    return a*h*0.5


def pp_kola(r: float) -> float:
    return PI*r*r


def pp_rombu(a: float, h: float) -> float:
    return a*h


def legenda_pp() -> None:
    print("a - pp_kwadartu")
    print("b - pp_prostokata")
    print("c - pp_rownolegloboku")
    print("d - pp_trapezu")
    print("e - pp_trojkata")
    print("f - pp_kola")
    print("g - pp_rombu")


def pola_pp() -> None:
    legenda_pp()
    inp = input().lower().strip()

    if inp == "a":
        a = float(input("a: "))
        print(f"dla kwadratu o boku {a} pp = {pp_kwadartu(a)}")

    elif inp == "b":
        a = float(input("a: "))
        b = float(input("b: "))
        print(f"dla prostokata o bokach {a} i {b} pp = {pp_prostokata(a,b)}")

    elif inp == "c":
        a = float(input("a: "))
        h = float(input("h: "))
        print(f"dla rownolegloboku o boku {a} i h = {h} pp = {pp_rownolegloboku(a,h)}")

    elif inp == "d":
        a = float(input("a: "))
        b = float(input("b: "))
        h = float(input("h: "))
        print(f"dla trapezu o bokach {a} i {b} i h = {h} pp = {pp_trapezu(a,b,h)}")

    elif inp == "e":
        a = float(input("a: "))
        h = float(input("h: "))
        print(f"dla trojkata o podstawie {a} i wysokosci {h} pp = {pp_trojkata(a,h)}")

    elif inp == "f":
        r = float(input("r: "))
        print(f"pp kola o promieniu {r} = {pp_kola(r)}")

    elif inp == "g":
        a = float(input("a: "))
        h = float(input("h: "))
        print(f"dla rombu o podstawie {a} i wysokosci {h} pp = {pp_rombu(a,h)}")

    else:
        print("nie ma takiej komendy")


# --------------------------------------------
# Obwody

def obw_kwadratu(a: float) -> float:
    return 4*a


def obw_prostokata(a: float, b: float) -> float:
    return 2*a+2*b


def obw_rownolegloboku(a: float, b: float) -> float:
    return 2*a+2*b


def obw_trapezu(a: float, b: float, c: float, d: float) -> float:
    return a+b+c+d


def obw_trojkata(a: float, b: float, c: float) -> float:
    return a+b+c


def obw_kola(r: float) -> float:
    return 2*PI*r


def obw_rombu(a: float) -> float:
    return 4*a


def legenda_obw() -> None:
    print("a - obw_kwadratu")
    print("b - obw_prostokata")
    print("c - obw_rownolegloboku")
    print("d - obw_trapezu")
    print("e - obw_trojkata")
    print("f - obw kola")
    print("g - obw rombu")


def obwody() -> None:
    legenda_obw()
    inp = input().lower().strip()

    if inp == "a":
        a = float(input("a: "))
        print(f"Dla kwadratu o boku {a} obw = {obw_kwadratu(a)}")

    elif inp == "b":
        a = float(input("a: "))
        b = float(input("b: "))
        print(f"Dla prostokata o bokach {a} i {b} obw = {obw_prostokata(a,b)}")

    elif inp == "c":
        a = float(input("a: "))
        b = float(input("b: "))
        print(f"dla rownolegloboku o bokach {a} {b} obw = {obw_rownolegloboku(a,b)}")

    elif inp == "d":
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        d = float(input("d: "))
        print(f"dla trapezu o bokach {a} {b} {c} {d} obw = {obw_trapezu(a,b,c,d)}")

    elif inp == "e":
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        print(f"dla trojkata o bokach {a} {b} {c} obw = {obw_trojkata(a,b,c)}")

    elif inp == "f":
        r = float(input("r: "))
        print(f"dla kola o promieniu {r} wynosi {obw_kola(r)}")

    elif inp == "g":
        a = float(input("a: "))
        print(f"Dla rombu o boku {a} obw = {obw_rombu(a)}")

    else:
        print("nie ma takiej komendy")


# ----------------------------------------------

def plaskie() -> None:
    print("Wzory na figury plaskie")
    print("a - pola pp")
    print("b - obwody")

    inp = input().lower().strip()

    if inp == "a":
        pola_pp()
    elif inp == "b":
        obwody()
    else:
        print("Nie ma takiej komendy")
