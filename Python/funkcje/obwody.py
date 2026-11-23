# Obwody 
def obw_kwadratu(a:float)->float:
    return 4*a

def obw_prostokata(a:float,b:float)->float:
    return 2*a+2*b

def obw_rownolegloboku(a:float,b:float)->float:
    return 2*a+2*b

def obw_trapezu(a:float,b:float,c:float,d:float)->float:
    return a + b + c + d

def obw_trojkota(a:float,b:float,c:float)->float:
    return a+b+c

def obw_kola(r:float)->float:
    return 2*PI*r

def obw_rombu(a:float)->float:
    return 4*a

def legenda_obw()->None:
    print("a - obw_kwadratu")
    print("b - obw_prostokata")
    print("c - obw_rownolegloboku")
    print("d - obw_trapezu")
    print("e - obw_trojkata")
    print("f - obw kola")
    print("g - obw rombu")

def obwody()->None:
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
        print(f"dla trojkata o bokach {a} {b} {c} obw = {obw_trojkota(a,b,c)}")
    elif inp == "f":
        r = float(input("r: "))
        print(f"dla kola o promieniu {r} wynosi {obw_kola(r)}")
    elif inp == "g":
        a = float(input("a: "))
        print(f"Dla rombu o boku {a} obw = {obw_rombu(a)}")
    else:
        print("nie ma takiej komendy")
   

