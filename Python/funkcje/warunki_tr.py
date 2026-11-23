
def cz_mg_zr_tr(a: float, b: float, c: float) -> str:
    if a > 0 and b > 0 and c > 0:
        if a+b > c and c+b > a and c+a > b:
            return "tak"
        else:
            return "nie"
    else:
        return "nie"


# --------------------------------------------

def trojkaty() -> None:
    print("Czy trojkat o danych bokach istnieje?")

    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    wynik = cz_mg_zr_tr(a, b, c)
    print(wynik)
