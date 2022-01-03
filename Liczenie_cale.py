"""
prostokat
kwadrat
trojkat
trapez
kolo
"""

while (True):

    print("Aby policzyć pole prostakata wybierz 1")
    print("Aby policzyć pole kwadratu wybierz 2")
    print("Aby policzyć pole trójkąta wybierz 3")
    print("Aby policzyć pole trapezu wybierz 4")
    print("Aby policzyć pole koła wybierz 5")
    print("Aby zakończyć program wybierz 6")

    wybor = input("Co chcesz zrobić?: ")

    if wybor == "1":
        a = float(input("Podaj pierwsza długość boku: "))
        b = float(input("Podaj drugą długość boku: "))


        def poleprostokata (a , b):
            return a * b


        print("Pole prostokata wynosi: ", poleprostokata(a,b))

    elif wybor == "2":
        a = float(input("Podaj długośc boku: "))

        def polekwadratu (a):
            return a * a

        print("Pole kwadratu wynosi: ", polekwadratu(a))

    elif wybor == "3":
        a = float(input("Podaj długość podstawy: "))
        h = float(input("Podaj długość wysokości: "))

        def poletrojkata(a , h):
            return(a * h)/2

        print("Pole trójkąta wynosi: ", poletrojkata(a , h))

    elif wybor == "4":
        a = float(input("Podaj długośc pierwszej podstawy: "))
        b = float(input("Podaj długość drugiej podstawy: "))
        h = float(input("Podaj długość wysokości: "))

        def poletrapezu (a, b, h):
            return ((a + b) * h) / 2

        print("Pole trapezu wynosi: ", poletrapezu(a, b, h))

    elif wybor == "5":
        r = float(input("Podaj długość promienia: "))

        def polekola (r):
            return 3.14 * (r * r)

        print("Pole koła wynosi: ", polekola(r))

    elif wybor == "6":
        print("Program zakończono")
        break
        
    
    
        
