# Sztuczna Inteligencja
# Projekt 1
#
# Dynowski Kacper     174061
# Janczuk Maciej      121483
# Turkiewicz Michał   197155

### Import potrzebnych bibliotek domyślnych w Python
from tkinter import *
from tkinter import ttk
import math


if __name__ == '__main__':
    Miasta = []  # Tablica obiektów klasy miasto
    Macierz = [] # Lista miast w środkowej kolumnie
    Graf = []   # Macierz sąsiedztwa

# Deklaracja klasy w celu łatwieszego zarządzania danymi
    class miasto:
        def __init__(self,wsp_x,wsp_y,numer):
            self.x = wsp_x
            self.y = wsp_y
            self.nr = numer
        def f(self):
            print(self.x,self.y)
        def x(self):
            return self.x
        def y(self):
            return self.y
        def nr(self):
            return self.nr

### DEFINICJE FUNKCJI POMOCNICZYCH DO WIZUALIZACJI I OKRESLANIA KOORDYNATÓW MIAST, ODLEGŁOŚCi
    def Kolory(numer): # Wybór kolorów wykorzystanych w aplikacji do oznaczania miast
        ListaKolorow = ('red', 'blue', 'green', 'black', 'magenta', 'gold', 'yellow','firebrick1','goldenrod',
                        'indigo','cyan','crimson','beige','aquamarine3', 'deepskyblue3')
        return(ListaKolorow[numer])
    def WyczyscMacierz(): # OBSŁUGA GUI
        Macierz.delete(*Macierz.get_children())
        Graf.clear()
    def DodajMiasto(e): # FUNKCJA DODAJACA MIASTO PO KLIKNIECIU MYSZKA
        if len(Miasta)<15: # LIMIT MIAST
            Miasta.append(miasto(e.x,e.y,len(Miasta)))
        LiczbaMiast = ListaMiast.size()
        if LiczbaMiast<15:
            Plotno.create_oval(e.x-6,e.y-6,e.x+6,e.y+6,fill=Kolory(LiczbaMiast))
            Plotno.create_text(e.x,e.y-10,text='M'+ f'{(LiczbaMiast):02d}')
            ListaMiast.insert(END,'M'+ f'{(LiczbaMiast):02d}' + ' [X:' + f'{(e.x):03d}'+',Y:'+f'{(e.y):03d}'+']')
            WyczyscMacierz()
            for i in range(LiczbaMiast + 1):
                Wiersz = ['M'+ f'{(i):02d}']
                MiastaShift = Miasta
                for j in range(LiczbaMiast + 1):
                    Wiersz.append(Odleglosc2(MiastaShift, i, j))
                Macierz.insert("", END,iid=Kolumny[i], values=Wiersz)
                Graf.append(Wiersz[1:])
    def Wyczysc(): # OBSŁUGA GUI
        Plotno.delete(ALL)
        ListaMiast.delete(0,ListaMiast.size())
        Miasta.clear()
        WyczyscMacierz()
        txZach.set('')
        txWsp.set('')
        txGlab.set('')
    def Koordynaty2(numer): # Zwraca koordynaty X,Y
        return(int(Miasta[numer].x),int(Miasta[numer].y))
    def Koordynaty2off(numer,odstep): # OBSŁUGA GUI
        return((int(Miasta[numer].x)+odstep),(int(Miasta[numer].y)+odstep))
    def KoordynatyListaNumer(Miasta, numer):
        return(int(Miasta[numer].x),int(Miasta[numer].y))
    def KoordynatyMiasta(Miasto):
        return(int(Miasto.x),int(Miasto.y))
    def Odleglosc(m1,m2):
        (x1,y1) = Koordynaty2(m1)
        (x2,y2) = Koordynaty2(m2)
        return round(math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2)),1)
    def Odleglosc2(ls,m1,m2):
        (x1,y1) = KoordynatyListaNumer(ls, m1)
        (x2,y2) = KoordynatyListaNumer(ls, m2)
        return round(math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2)),1)
    def OdlegloscMiast(m1, m2):
        (x1,y1) = KoordynatyMiasta(m1)
        (x2,y2) = KoordynatyMiasta(m2)
        return round(math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2)),1)
    def Srodek(m1,m2): # Wyznacza punkt srodkowy miedzy miastami
        (x1,y1) = Koordynaty2(m1)
        (x2,y2) = Koordynaty2(m2)
        return ((x2+x1)/2, (y2+y1)/2)
    def SrodekMiast(m1,m2): # Wyznacza punkt srodkowy operujac na klasach
        (x1,y1) = (m1.x,m1.y)
        (x2,y2) = (m2.x,m2.y)
        return ((x2+x1)/2, (y2+y1)/2)
    def PolaczMiastaNrKolorOffset(M1, M2, kolor, odstep): # OBSŁUGA GUI
        Plotno.create_text(Srodek(M1,M2),text=f'{(Odleglosc(M1,M2)):0.1f}',)
        Plotno.create_line(Koordynaty2off(M1,odstep),(Koordynaty2off(M2,odstep)),fill=kolor, width = 2 )
    def WybranyZListy(): # FUNKCJA DO OKREŚLENIA MIASTA STARTOWEGO
        Nr = ListaMiast.curselection()
        if Nr==():
            return 0
        else:
            return Nr[0]
    def UsunStrzalki(): # NARYSOWANIA NA NOWO MIAST NA PŁÓTNIE BEZ STRZAŁEK
        Plotno.delete(ALL)
        for e in Miasta:
            Plotno.create_oval(e.x - 6, e.y - 6, e.x + 6, e.y + 6, fill=Kolory(e.nr))
            Plotno.create_text(e.x, e.y - 10, text='M' + f'{(e.nr):02d}')

###### ALGORYTMY #####################################################
    def Zachlanny():
        ## FUNKCJA OKREŚLAJĄCA NAJBLIŻSZE MIASTO Z LISTY MIAST ZWRACA DWIE WARTOŚCI [NAJBLIŻSZE MIASTO, JEGO ODLEGŁOŚĆ]
        def MinimumZachalnne(BADANA_LISTA_ODLEGŁOSCI, LISTA_DOSTEPNOSC):
            MINIMUM_LOKALNE = max(BADANA_LISTA_ODLEGŁOSCI)
            NAJBLIŻSZE_MIASTO = BADANA_LISTA_ODLEGŁOSCI.index(MINIMUM_LOKALNE)
            for i in range(len(BADANA_LISTA_ODLEGŁOSCI)):
                ODLEGŁOŚĆ = BADANA_LISTA_ODLEGŁOSCI[i]
                if ODLEGŁOŚĆ < MINIMUM_LOKALNE and ODLEGŁOŚĆ != 0:
                    PRETENDET = BADANA_LISTA_ODLEGŁOSCI.index(ODLEGŁOŚĆ)
                    if PRETENDET in LISTA_DOSTEPNOSC:
                        MINIMUM_LOKALNE = ODLEGŁOŚĆ
                        NAJBLIŻSZE_MIASTO = PRETENDET
            return (MINIMUM_LOKALNE, NAJBLIŻSZE_MIASTO)

        ## SKOPIOWANIE MACIERZY SĄSIEDZTWA DO ALGORYTMU
        LISTA_ODLEGLOSCI_MIEDZY_MIASTAMI = Graf

        # START
        MIASTO_STARTOWE = WybranyZListy()
        FINALNA_KOLEJNOSC = []
        FINALNA_KOLEJNOSC.append(MIASTO_STARTOWE)
        FINALNA_ODLEGŁOSC = 0.0

        # PRZYGOTOWANIE MACIERZY MIASTO DO SPRAWDZENIA
        LISTA_MIAST_DO_PRZEJRZENIA = []
        for a in range(len(LISTA_ODLEGLOSCI_MIEDZY_MIASTAMI)):
            LISTA_MIAST_DO_PRZEJRZENIA.append(a)
        LISTA_MIAST_DO_PRZEJRZENIA.remove(MIASTO_STARTOWE)

        AKTUALNE_GDZIE_JESTESMY = MIASTO_STARTOWE

        # DOPÓKI JEST JAKIEŚ MIASTO DO SPRAWDZENIA
        while LISTA_MIAST_DO_PRZEJRZENIA != []:
            WYNIK_NAJMNIEJSZY = MinimumZachalnne(LISTA_ODLEGLOSCI_MIEDZY_MIASTAMI[AKTUALNE_GDZIE_JESTESMY],
                                                 LISTA_MIAST_DO_PRZEJRZENIA)
            FINALNA_ODLEGŁOSC = WYNIK_NAJMNIEJSZY[0] + FINALNA_ODLEGŁOSC
            FINALNA_KOLEJNOSC.append(WYNIK_NAJMNIEJSZY[1])
            PolaczMiastaNrKolorOffset(AKTUALNE_GDZIE_JESTESMY,WYNIK_NAJMNIEJSZY[1],'green',5)
            AKTUALNE_GDZIE_JESTESMY = WYNIK_NAJMNIEJSZY[1]
            LISTA_MIAST_DO_PRZEJRZENIA.remove(WYNIK_NAJMNIEJSZY[1])

        print('Algorytm zachłanny   : ',FINALNA_KOLEJNOSC,FINALNA_ODLEGŁOSC)
        txZach.set('Algorytm zachłanny              KOLEJNOŚĆ = ' + str(FINALNA_KOLEJNOSC) + '      DROGA = ' + str(FINALNA_ODLEGŁOSC))

    def Wspinaczkowy():
        # FUNKCJA LICZĄCA AKTUALNĄ DROGE
        def DrogaWspinaczkowy(BADANA_LISTA_ODLEGLOSCI, KOLEJNOSC):
            Suma = 0.0
            for i in range(len(KOLEJNOSC) - 1):
                Suma = Suma + BADANA_LISTA_ODLEGLOSCI[KOLEJNOSC[i]][KOLEJNOSC[i + 1]]
            return (Suma)
        # FUNKCJA ZAMIANY SPRAWDZANYCH MIAST
        def ZmianaMiejscWspiczkowy(LISTA_KOLEJNOSCI, PIERWSZY_ELEMENT, DRUGI_ELEMENT):
            LISTA_KOLEJNOSCI[DRUGI_ELEMENT], LISTA_KOLEJNOSCI[PIERWSZY_ELEMENT] = LISTA_KOLEJNOSCI[PIERWSZY_ELEMENT], \
                                                                                  LISTA_KOLEJNOSCI[DRUGI_ELEMENT]

        LISTA_ODLEGLOSCI_MIEDZY_MIASTAMI = Graf

        MIASTO_STARTOWE = WybranyZListy()
        OPTYMALNA_KOLEJNOSC = []

        ### OKRESLENIE PIERWSZEGO ROZWIAZANIA JAKO LISTY MIAST W KOLEJNOSCI ROSNACEJ Z ZAMIANĄ PIERWSZEGO MIASTA NA STARTOWE
        for a in range(len(LISTA_ODLEGLOSCI_MIEDZY_MIASTAMI)):
            OPTYMALNA_KOLEJNOSC.append(a)
        OPTYMALNA_KOLEJNOSC.index(MIASTO_STARTOWE)
        ZmianaMiejscWspiczkowy(OPTYMALNA_KOLEJNOSC, 0,OPTYMALNA_KOLEJNOSC.index(MIASTO_STARTOWE))

        OPTYMALNA_DROGA = DrogaWspinaczkowy(LISTA_ODLEGLOSCI_MIEDZY_MIASTAMI, OPTYMALNA_KOLEJNOSC)

        # WIZUALIZACJA PIERWSZEJ KOLEJNOŚCI
        print('Algorytm wspinaczkowy: ',OPTYMALNA_KOLEJNOSC,OPTYMALNA_DROGA)

        DLUGOSC_KOLEJNOSCI = len(OPTYMALNA_KOLEJNOSC)
        DLUGOSC_SWAPOWANIA = len(OPTYMALNA_KOLEJNOSC) - 1

        # SPRAWDZENIE PO KOLEI MOZLIWOSCI ZAMIANY KAZDEJ Z POZYCJI CZY OSIĄGA LEPSZY REZULTAT
        i = 1
        while i != DLUGOSC_SWAPOWANIA:
            for j in range(1, DLUGOSC_KOLEJNOSCI - i):
                TESTOWANA_KOLEJNOSC = list(OPTYMALNA_KOLEJNOSC)
                ZmianaMiejscWspiczkowy(TESTOWANA_KOLEJNOSC, i, i + j)
                TESTOWANA_DROGA = DrogaWspinaczkowy(LISTA_ODLEGLOSCI_MIEDZY_MIASTAMI, TESTOWANA_KOLEJNOSC)
                if TESTOWANA_DROGA < OPTYMALNA_DROGA:
                    # ZNALEZIONO LEPSZE ROZWIAZNIA WYPISANIE W KONSOLI
                    OPTYMALNA_KOLEJNOSC = list(TESTOWANA_KOLEJNOSC)
                    OPTYMALNA_DROGA = TESTOWANA_DROGA
                    print('Algorytm wspinaczkowy: ', OPTYMALNA_KOLEJNOSC, OPTYMALNA_DROGA)
                    # SPRAWDZANIE OD NOWA WSZYSTKICH DRÓG
                    i = 0
                    j = 1
                    break
            i = i + 1

        # WIZUALIZACJA
        for i in range(len(OPTYMALNA_KOLEJNOSC)-1):
            PolaczMiastaNrKolorOffset(OPTYMALNA_KOLEJNOSC[i], OPTYMALNA_KOLEJNOSC[i+1],'blue',0)
        txWsp.set('Algorytm wspinaczkowy      KOLEJNOŚĆ = ' + str(OPTYMALNA_KOLEJNOSC) + '      DROGA = ' + str(OPTYMALNA_DROGA))

    def Glab():
        def Lista_Mozliwosci(NumerMiasta):  # Funkcja realizujaca permutacje bez powtorzeń oparta na algorytmie Heap'a
            n = len(NumerMiasta)
            c = [0] * n  # Macierz wymian
            Wynik = [NumerMiasta[:]]
            i = 0
            while i < n:  # Dopoki nie sprawdzimy wszystkich przypadków
                if c[i] < i:
                    if i % 2 == 0:
                        NumerMiasta[0], NumerMiasta[i] = NumerMiasta[i], NumerMiasta[0]
                    else:
                        NumerMiasta[c[i]], NumerMiasta[i] = NumerMiasta[i], NumerMiasta[c[i]]

                    Wynik.append(NumerMiasta[:])
                    c[i] += 1
                    i = 0
                else:
                    c[i] = 0
                    i += 1
            return Wynik

        def DrogaWglab(BADANA_LISTA_ODLEGLOSCI, KOLEJNOSC): ## SPRAWDZENIE CZY DROGA JEST KRÓTSZA
            Suma = 0.0
            for i in range(len(KOLEJNOSC) - 1):
                Suma = Suma + BADANA_LISTA_ODLEGLOSCI[KOLEJNOSC[i]][KOLEJNOSC[i + 1]]
            return (Suma)

        #START
        LISTA_ODLEGLOSCI_MIEDZY_MIASTAMI = Graf
        MIASTO_STARTOWE = WybranyZListy()
        AKTUALNA_KOLEJNOSC = []
        for a in range(len(LISTA_ODLEGLOSCI_MIEDZY_MIASTAMI)):
            AKTUALNA_KOLEJNOSC.append(a)
        AKTUALNA_KOLEJNOSC.remove(MIASTO_STARTOWE)

        TESTOWANA_KOLEJNOSC = []
        TESTOWANA_KOLEJNOSC.append(MIASTO_STARTOWE)
        for a in AKTUALNA_KOLEJNOSC:
            TESTOWANA_KOLEJNOSC.append(a)

        AKTUALNA_DROGA = DrogaWglab(LISTA_ODLEGLOSCI_MIEDZY_MIASTAMI, TESTOWANA_KOLEJNOSC)
        print('Algorytm wgłąb       : ', TESTOWANA_KOLEJNOSC, AKTUALNA_DROGA)

        # PRZETASOWANIE KOLEJNOŚCI
        A = Lista_Mozliwosci(AKTUALNA_KOLEJNOSC)
        AKTUALNA_KOLEJNOSC = TESTOWANA_KOLEJNOSC
        # SPRAWDZENIE WSZYSTKICH MIAST
        for a in A:
            TESTOWANA_KOLEJNOSC = []
            TESTOWANA_KOLEJNOSC.append(MIASTO_STARTOWE)
            for b in a:
                TESTOWANA_KOLEJNOSC.append(b)
            TestowanaDroga = DrogaWglab(LISTA_ODLEGLOSCI_MIEDZY_MIASTAMI, TESTOWANA_KOLEJNOSC)

            # ZNALEZIENIE LEPSZEGO ROZWIĄZANIA
            if TestowanaDroga < AKTUALNA_DROGA:
                AKTUALNA_KOLEJNOSC = TESTOWANA_KOLEJNOSC
                AKTUALNA_DROGA = TestowanaDroga
                print('Algorytm wgłąb       : '+ str(AKTUALNA_KOLEJNOSC) +  str(AKTUALNA_DROGA))

        # WIZUALIZACJAA
        for i in range(len(AKTUALNA_KOLEJNOSC)-1):
            PolaczMiastaNrKolorOffset(AKTUALNA_KOLEJNOSC[i], AKTUALNA_KOLEJNOSC[i+1],'red',-5)
        txGlab.set('Algorytm wgłąb                     KOLEJNOŚĆ = '+ str(AKTUALNA_KOLEJNOSC) + '      DROGA = ' + str(AKTUALNA_DROGA))


#################################################################


#### PRZYGOTOWANIE ELEMENTÓW GUI I ICH INICJALIZACJA Z WYMIARAMI
    root = Tk()
    root.title('Mapa')
    Plotno = Canvas(root,width=400,height=400,bg="white")
    ListaMiast = Listbox(root, selectmode=SINGLE)
    Kasowanie = Button(root, width=15, height=2, text='Usuń \nmiasta',command=Wyczysc)
    UsStrz = Button(root, width=15, height=2, text='Usuń \nstrzałki',command=UsunStrzalki)

### PRZYCISKI WYWOLUJACE FUNKCJE Z ALGORYTMAMI
    Zach = Button(root, width=15, height=2, text='Algorytm \nZachłanny',bg='green', fg='white', command=Zachlanny)
    Wsp = Button(root, width=15, height=2, text='Algorytm \nWspinaczkowy',bg='blue', fg='white', command=Wspinaczkowy)
    Gla = Button(root, width=15, height=2, text='Algorytm \nWgłąb',bg='red', fg='white', command=Glab)

### POLA PODSUMOWUJACE DZIALANIA ALGORYTMÓW
    txZach = StringVar()
    KonsolaZach = Entry(root,textvariable=txZach, xscrollcommand=True)
    txWsp = StringVar()
    KonsolaWsp = Entry(root, textvariable=txWsp, xscrollcommand=True)
    txGlab = StringVar()
    KonsolaGlab = Entry(root, textvariable=txGlab, xscrollcommand=True)

    Kolumny = ('Odl.',)
    for i in range(15):
        Kolumny = Kolumny + ("M" + f'{(i):02d}',)

### LOKACJA ELEMENTÓW W APLIKACJI
    Macierz = ttk.Treeview(root,columns=Kolumny,show='headings')
    Macierz.heading('1', text="Odl.")
    Macierz.column('1', minwidth=0, width=37, stretch=NO)
    for i in range(16):
        Macierz.heading(Kolumny[i],text=Kolumny[i])
        Macierz.column(Kolumny[i], minwidth=0, width=37, stretch=NO)
    Plotno.grid(row=0, columnspan=3, column=0,pady=2)
    ListaMiast.grid(row=0,column=3,pady=2,sticky=NSEW)
    Macierz.grid(row=0,column=4,pady=2,sticky=NS)
    Kasowanie.grid(row=1,column=3,pady=2)
    UsStrz.grid(row=1,column=4,pady=2)
    Zach.grid(row=1, column=0, pady=2)
    Wsp.grid(row=1, column=1, pady=2)
    Gla.grid(row=1, column=2, pady=2)
    KonsolaZach.grid(row=2,columnspan=5,sticky=EW,pady=3)
    KonsolaWsp.grid(row=3,columnspan=5,sticky=EW,pady=3)
    KonsolaGlab.grid(row=4,columnspan=5,sticky=EW,pady=3)

### FUNKCJA PRZECHWYTUJACA KLIKNIECIE NA OBSZARZE PŁÓTNA I DODAJACA MIASTO
    Plotno.bind('<Button-1>', DodajMiasto)

    root.mainloop()
