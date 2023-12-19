# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *
from tkinter import ttk
#import random
import math
import time


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def paint(e):
    print("Hej")

# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    Miasta = []
    Macierz = []
    Graf = []

        #Macierz incydencji lub inna, zadanie jako roziwązanie grafu
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

    def Kolory(numer):
        ListaKolorow = ('red', 'blue', 'green', 'black', 'magenta', 'gold', 'yellow','firebrick1','goldenrod',
                        'indigo','cyan','crimson','beige','aquamarine3', 'deepskyblue3')
        return(ListaKolorow[numer])

    def WyczyscMacierz():
        Macierz.delete(*Macierz.get_children())
        Graf.clear()

    def ZnajdowanieMinimum(Lista):
        idx=0
        i=0
        min = Lista[0]
        for w in Lista:
            if w<min:
                min=w
                idx=i
            i+=1
        return idx

    def DodajMiasto(e):
        if len(Miasta)<15:
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



    def Wyczysc():
        Plotno.delete(ALL)
        ListaMiast.delete(0,ListaMiast.size())
        Miasta.clear()
        WyczyscMacierz()

    def Koordynaty(numer):
        Nazwa = ListaMiast.get(numer)
        return(int(Nazwa[-10:-7]),int(Nazwa[-4:-1]))

    def Koordynaty2(numer):
        return(int(Miasta[numer].x),int(Miasta[numer].y))

    def Koordynaty2off(numer,odstep):
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

    def Srodek(m1,m2):
        (x1,y1) = Koordynaty2(m1)
        (x2,y2) = Koordynaty2(m2)
        return ((x2+x1)/2, (y2+y1)/2)

    def SrodekMiast(m1,m2):
        (x1,y1) = (m1.x,m1.y)
        (x2,y2) = (m2.x,m2.y)
        return ((x2+x1)/2, (y2+y1)/2)

    def SrodekMiastOffset(m1,m2,off):
        (x1,y1) = (m1.x,m1.y)
        (x2,y2) = (m2.x,m2.y)
        return ((x2+x1)/2, (y2+y1)/2-off)

    def PolaczMiastaNr(M1, M2):
        Plotno.create_text(Srodek(M1,M2),text=f'{(Odleglosc(M1,M2)):0.1f}',)
        Plotno.create_line(Koordynaty2(M1),Koordynaty2(M2),fill='grey')

    def PolaczMiastaNrKolorOffset(M1, M2, kolor, odstep):
        Plotno.create_text(Srodek(M1,M2),text=f'{(Odleglosc(M1,M2)):0.1f}',)
        Plotno.create_line(Koordynaty2off(M1,odstep),(Koordynaty2off(M2,odstep)),fill=kolor, width = 2 )

    def PolaczMiasta(M1, M2):
        Plotno.create_text(SrodekMiast(M1,M2), text=f'{(OdlegloscMiast(M1, M2)):0.1f}', )
        Plotno.create_line(KoordynatyMiasta(M1),KoordynatyMiasta(M2),fill='grey')

    def PolaczMiastaKolejnosc(M1, M2, Kolejnosc):
        #Plotno.create_text(SrodekMiast(M1, M2), text=f'{(OdlegloscMiast(M1, M2)):0.1f}', )
        #Plotno.create_text(SrodekMiastOffset(M1, M2,15), text=Kolejnosc)
        Plotno.create_line(KoordynatyMiasta(M1), KoordynatyMiasta(M2), fill='grey',arrow=LAST, arrowshape=(20,20,3))

    def WybranyZListy():
        Nr = ListaMiast.curselection()
        if Nr==():
            return 0
        else:
            return Nr[0]

    def Cw1(ls,M1):
        Lista = []
        for i in range(len(ls)):
            if Miasta[i].x>=Miasta[M1].x and i != M1 and Miasta[i].y<=Miasta[M1].y:
                Lista.append(i)
        return Lista
    def Cw2(ls,M1):
        Lista = []
        for i in range(len(ls)):
            if Miasta[i].x>=Miasta[M1].x and i != M1 and Miasta[i].y>=Miasta[M1].y:
                Lista.append(i)
        return Lista
    def Cw3(ls,M1):
        Lista = []
        for i in range(len(ls)):
            if Miasta[i].x<=Miasta[M1].x and i != M1 and Miasta[i].y>=Miasta[M1].y:
                Lista.append(i)
        return Lista
    def Cw4(ls,M1):
        Lista = []
        for i in range(len(ls)):
            if Miasta[i].x <= Miasta[M1].x and i != M1 and Miasta[i].y <= Miasta[M1].y:
                Lista.append(i)
        return Lista

    def JestPolaczenie(M1, M2):
        if M1 != M2:
            return True
        else:
            return False

    def UsunZGrafuKolumne(graf, kolumna):
        nowyGraf = []
        for wiersz in graf:
            del wiersz[kolumna]
            nowyGraf.append(wiersz)
        return nowyGraf



    def UsunStrzalki():
        Plotno.delete(ALL)
        for e in Miasta:
            Plotno.create_oval(e.x - 6, e.y - 6, e.x + 6, e.y + 6, fill=Kolory(e.nr))
            Plotno.create_text(e.x, e.y - 10, text='M' + f'{(e.nr):02d}')

###### ALGORYTMY #####################################################
    def Zachlanny():
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


        LISTA_ODLEGLOSCI_MIEDZY_MIASTAMI = Graf

        MIASTO_STARTOWE = WybranyZListy()
        FINALNA_KOLEJNOSC = []
        FINALNA_KOLEJNOSC.append(MIASTO_STARTOWE)
        FINALNA_ODLEGŁOSC = 0.0

        LISTA_MIAST_DO_PRZEJRZENIA = []
        for a in range(len(LISTA_ODLEGLOSCI_MIEDZY_MIASTAMI)):
            LISTA_MIAST_DO_PRZEJRZENIA.append(a)
        LISTA_MIAST_DO_PRZEJRZENIA.remove(MIASTO_STARTOWE)

        AKTUALNE_GDZIE_JESTESMY = MIASTO_STARTOWE
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
        def DrogaWspinaczkowy(BADANA_LISTA_ODLEGLOSCI, KOLEJNOSC):
            Suma = 0.0
            for i in range(len(KOLEJNOSC) - 1):
                Suma = Suma + BADANA_LISTA_ODLEGLOSCI[KOLEJNOSC[i]][KOLEJNOSC[i + 1]]
            return (Suma)

        def ZmianaMiejscWspiczkowy(LISTA_KOLEJNOSCI, PIERWSZY_ELEMENT, DRUGI_ELEMENT):
            LISTA_KOLEJNOSCI[DRUGI_ELEMENT], LISTA_KOLEJNOSCI[PIERWSZY_ELEMENT] = LISTA_KOLEJNOSCI[PIERWSZY_ELEMENT], \
                                                                                  LISTA_KOLEJNOSCI[DRUGI_ELEMENT]

        LISTA_ODLEGLOSCI_MIEDZY_MIASTAMI = Graf

        MIASTO_STARTOWE = WybranyZListy()
        OPTYMALNA_KOLEJNOSC = []
        #import random
        for a in range(len(LISTA_ODLEGLOSCI_MIEDZY_MIASTAMI)):
            OPTYMALNA_KOLEJNOSC.append(a)
        OPTYMALNA_KOLEJNOSC.index(MIASTO_STARTOWE)
        ZmianaMiejscWspiczkowy(OPTYMALNA_KOLEJNOSC, 0,OPTYMALNA_KOLEJNOSC.index(MIASTO_STARTOWE))
        # OPTYMALNA_KOLEJNOSC.reverse()
        #random.shuffle(OPTYMALNA_KOLEJNOSC)

        OPTYMALNA_DROGA = DrogaWspinaczkowy(LISTA_ODLEGLOSCI_MIEDZY_MIASTAMI, OPTYMALNA_KOLEJNOSC)
        print('Algorytm wspinaczkowy: ',OPTYMALNA_KOLEJNOSC,OPTYMALNA_DROGA)

        DLUGOSC_KOLEJNOSCI = len(OPTYMALNA_KOLEJNOSC)
        DLUGOSC_SWAPOWANIA = len(OPTYMALNA_KOLEJNOSC) - 1

        i = 1
        while i != DLUGOSC_SWAPOWANIA:
            for j in range(1, DLUGOSC_KOLEJNOSCI - i):
                TESTOWANA_KOLEJNOSC = list(OPTYMALNA_KOLEJNOSC)
                ZmianaMiejscWspiczkowy(TESTOWANA_KOLEJNOSC, i, i + j)
                TESTOWANA_DROGA = DrogaWspinaczkowy(LISTA_ODLEGLOSCI_MIEDZY_MIASTAMI, TESTOWANA_KOLEJNOSC)
                if TESTOWANA_DROGA < OPTYMALNA_DROGA:
                    OPTYMALNA_KOLEJNOSC = list(TESTOWANA_KOLEJNOSC)
                    OPTYMALNA_DROGA = TESTOWANA_DROGA
                    print('Algorytm wspinaczkowy: ', OPTYMALNA_KOLEJNOSC, OPTYMALNA_DROGA)
                    i = 0
                    j = 1
                    break
            i = i + 1
        for i in range(len(OPTYMALNA_KOLEJNOSC)-1):
            PolaczMiastaNrKolorOffset(OPTYMALNA_KOLEJNOSC[i], OPTYMALNA_KOLEJNOSC[i+1],'blue',0)
        txWsp.set('Algorytm wspinaczkowy      KOLEJNOŚĆ = ' + str(OPTYMALNA_KOLEJNOSC) + '      DROGA = ' + str(OPTYMALNA_DROGA))

    def Glab():
        import itertools

        def DrogaWglab(BADANA_LISTA_ODLEGLOSCI, KOLEJNOSC):
            Suma = 0.0
            for i in range(len(KOLEJNOSC) - 1):
                Suma = Suma + BADANA_LISTA_ODLEGLOSCI[KOLEJNOSC[i]][KOLEJNOSC[i + 1]]
            return (Suma)

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

        print(TESTOWANA_KOLEJNOSC)
        AKTUALNA_DROGA = DrogaWglab(LISTA_ODLEGLOSCI_MIEDZY_MIASTAMI, TESTOWANA_KOLEJNOSC)
        print('Algorytm wgłąb       : ', AKTUALNA_KOLEJNOSC, AKTUALNA_DROGA)

        A = itertools.permutations(AKTUALNA_KOLEJNOSC)
        for a in A:
            TESTOWANA_KOLEJNOSC = []
            TESTOWANA_KOLEJNOSC.append(MIASTO_STARTOWE)
            for b in a:
                TESTOWANA_KOLEJNOSC.append(b)
            TestowanaDroga = DrogaWglab(LISTA_ODLEGLOSCI_MIEDZY_MIASTAMI, TESTOWANA_KOLEJNOSC)

            if TestowanaDroga < AKTUALNA_DROGA:
                AKTUALNA_KOLEJNOSC = TESTOWANA_KOLEJNOSC
                AKTUALNA_DROGA = TestowanaDroga
                print('Algorytm wgłąb       : '+ str(AKTUALNA_KOLEJNOSC) +  str(AKTUALNA_DROGA))

        for i in range(len(TESTOWANA_KOLEJNOSC)-1):
            PolaczMiastaNrKolorOffset(TESTOWANA_KOLEJNOSC[i], TESTOWANA_KOLEJNOSC[i+1],'red',-5)
        txGlab.set('Algorytm wgłąb                     KOLEJNOŚĆ = '+ str(TESTOWANA_KOLEJNOSC) + '      DROGA = ' + str(AKTUALNA_DROGA))
#################################################################

    root = Tk()
    root.title('Mapa')
    #root.geometry("1010x810")
    Plotno = Canvas(root,width=400,height=400,bg="white")
    ListaMiast = Listbox(root, selectmode=SINGLE)
    Kasowanie = Button(root, width=15, height=2, text='Usuń \nmiasta',command=Wyczysc)
    UsStrz = Button(root, width=15, height=2, text='Usuń \nstrzałki',command=UsunStrzalki)
    Zach = Button(root, width=15, height=2, text='Algorytm \nZachłanny',bg='green', fg='white', command=Zachlanny)
    Wsp = Button(root, width=15, height=2, text='Algorytm \nWspinaczkowy',bg='blue', fg='white', command=Wspinaczkowy)
    Gla = Button(root, width=15, height=2, text='Algorytm \nWgłąb',bg='red', fg='white', command=Glab)
    txZach = StringVar()
    KonsolaZach = Entry(root,textvariable=txZach, xscrollcommand=True)
    txWsp = StringVar()
    KonsolaWsp = Entry(root, textvariable=txWsp, xscrollcommand=True)
    txGlab = StringVar()
    KonsolaGlab = Entry(root, textvariable=txGlab, xscrollcommand=True)

    Kolumny = ('Odl.',)
    for i in range(15):
        Kolumny = Kolumny + ("M" + f'{(i):02d}',)

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

    Plotno.bind('<Button-1>', DodajMiasto)
    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
