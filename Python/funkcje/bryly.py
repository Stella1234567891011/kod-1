
from math import pi as PI


# Pc bryl
def pc_szescianu(a: float) -> float:
    return 6*a**2


def pc_prostopadloscianu(a: float, b: float, c: float) -> float:
    return 2*a*b + 2*a*c + 2*b*c


def pc_graniastoslupa(pb: float, pp: float) -> float:
    return 2*pp + pb


def pc_ostroslupa(pb: float, pp: float) -> float:
    return pb + pp


def pc_walca(r: float, h: float) -> float:
    return 2*PI*r**2 + 2*PI*r*h


def pc_stozka(r: float, l: float) -> float:
    return PI*r*r + PI*r*l


def pc_kuli(r: float) -> float:
    return 4*PI*r**2


def legenda_pc() -> None:
    print("a - pc_szescianu")
    print("b - pc_prostopadloscianu")
    print("c - pc_graniastoslupa")
    print("d - pc_ostroslupa")
    print("e - pc_walca")
    print("f - pc_stozka")
    print("g - pc_kuli")


def pc_bryl() -> None:
    legenda_pc()
    inp = input().lower().strip()

    if inp == "a":
        a = float(input("a: "))
        print(f"dla szescianu o krawedzi {a} pc = {pc_szescianu(a)}")

    elif inp == "b":
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        print(f"dla prostopadloscianu o krawedziach {a}, {b}, {c} pc = {pc_prostopadloscianu(a,b,c)}")

    elif inp == "c":
        pp = float(input("pp: "))
        pb = float(input("pb: "))
        print(f"dla graniastoslupa z pp {pp} i pb {pb} pc = {pc_graniastoslupa(pb,pp)}")

    elif inp == "d":
        pp = float(input("pp: "))
        pb = float(input("pb: "))
        print(f"dla ostroslupa z pp {pp} i pb {pb} pc = {pc_ostroslupa(pb,pp)}")

    elif inp == "e":
        r = float(input("r: "))
        h = float(input("h: "))
        print(f"dla walca z r {r} i h {h} pc = {pc_walca(r,h)}")

    elif inp == "f":
        r = float(input("r: "))
        l = float(input("l: "))
        print(f"dla stozka z r {r} i l {l} pc = {pc_stozka(r,l)}")

    elif inp == "g":
        r = float(input("r: "))
        print(f"dla kuli z r {r} pc = {pc_kuli(r)}")

    else:
        print("nie ma takiej komendy")


# Objętości brył
# ------------------------------------------------

def obj_szescianu(a: float) -> float:
    return a**3


def obj_prostopadloscianu(a: float, b: float, c: float) -> float:
    return a*b*c


def obj_graniastoslupa(pp: float, h: float) -> float:
    return pp*h


def obj_ostroslupa(pp: float, h: float) -> float:
    return pp*h/3


def obj_walca(r: float, h: float) -> float:
    return PI*r*r*h


def obj_stozka(r: float, h: float) -> float:
    return PI*r*r*h/3


def obj_kuli(r: float) -> float:
    return 4*PI*r**3/3


def legenda_obj() -> None:
    print("a - obj_szescianu")
    print("b - obj_prostopadloscianu")
    print("c - obj_graniastoslupa")
    print("d - obj_ostroslupa")
    print("e - obj_walca")
    print("f - obj_stozka")
    print("g - obj_kuli")


def obj_bryl() -> None:
    legenda_obj()
    inp = input().lower().strip()

    if inp == "a":
        a = float(input("a: "))
        print(f"obj szescianu o krawedzi {a} = {obj_szescianu(a)}")

    elif inp == "b":
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        print(f"obj prostopadloscianu = {obj_prostopadloscianu(a,b,c)}")

    elif inp == "c":
        pp = float(input("pp: "))
        h = float(input("h: "))
        print(f"obj graniastoslupa = {obj_graniastoslupa(pp,h)}")

    elif inp == "d":
        pp = float(input("pp: "))
        h = float(input("h: "))
        print(f"obj ostroslupa = {obj_ostroslupa(pp,h)}")

    elif inp == "e":
        r = float(input("r: "))
        h = float(input("h: "))
        print(f"obj walca = {obj_walca(r,h)}")

    elif inp == "f":
        r = float(input("r: "))
        h = float(input("h: "))
        print(f"obj stozka = {obj_stozka(r,h)}")

    elif inp == "g":
        r = float(input("r: "))
        print(f"obj kuli = {obj_kuli(r)}")

    else:
        print("nie ma takiej komendy")


# ------------------------------------------------

def bryly() -> None:
    print("a - pc bryl")
    print("b - objetosci bryl")

    inp = input().lower().strip()

    if inp == "a":
        pc_bryl()
    elif inp == "b":
        obj_bryl()
    else:
        print("nie ma takiej komendy")
