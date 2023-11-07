# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *
from tkinter import ttk
import random
import math


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
        def __init__(self,wsp_x,wsp_y):
            self.x = wsp_x
            self.y = wsp_y
        def f(self):
            print(self.x,self.y)
        def x(self):
            return self.x
        def y(self):
            return self.y

    def Kolory(numer):
        ListaKolorow = ('red', 'blue', 'green', 'black', 'magenta', 'gold', 'yellow','firebrick1','goldenrod',
                        'indigo','cyan','crimson','beige','aquamarine3', 'deepskyblue3')
        return(ListaKolorow[numer])

    def WyczyscMacierz():
        Macierz.delete(*Macierz.get_children())
        Graf.clear()


    def DodajMiasto(e):
        if len(Miasta)<15:
            Miasta.append(miasto(e.x,e.y))

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
                Graf.append(Wiersz)


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

    def Koordynaty3(Miasta,numer):
        return(int(Miasta[numer].x),int(Miasta[numer].y))

    def Odleglosc(m1,m2):
        (x1,y1) = Koordynaty2(m1)
        (x2,y2) = Koordynaty2(m2)
        return round(math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2)),1)

    def Odleglosc2(ls,m1,m2):
        (x1,y1) = Koordynaty3(ls,m1)
        (x2,y2) = Koordynaty3(ls,m2)
        return round(math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2)),1)

    def Srodek(m1,m2):
        (x1,y1) = Koordynaty2(m1)
        (x2,y2) = Koordynaty2(m2)
        return ((x2+x1)/2, (y2+y1)/2)

    def PolaczMiasta(M1,M2):
        Plotno.create_text(Srodek(M1,M2),text=f'{(Odleglosc(M1,M2)):0.1f}',)
        Plotno.create_line(Koordynaty2(M1),Koordynaty2(M2),fill='grey')

    def Zachlanny():
        pass
    def Wspinaczkowy():
        pass
    def Glab():
        pass

    root = Tk()
    root.title('Mapa')
    #root.geometry("1010x810")
    Plotno = Canvas(root,width=400,height=400,bg="white")
    ListaMiast = Listbox(root, selectmode=SINGLE)
    Kasowanie = Button(root, width=15, height=2, text='Wyczysc',command=Wyczysc)
    Zach = Button(root, width=15, height=2, text='Algorytm \nZachłanny', command=Zachlanny)
    Wsp = Button(root, width=15, height=2, text='Algorytm \nWspinaczkowy', command=Wspinaczkowy)
    Gla = Button(root, width=15, height=2, text='Algorytm \nWgłąb', command=Glab)

    Kolumny = ('Odl.',)
    for i in range(15):
        Kolumny = Kolumny + ("M" + str(i),)

    Macierz = ttk.Treeview(root,columns=Kolumny,show='headings')

    Macierz.heading('1', text="Odl.")
    Macierz.column('1', minwidth=0, width=37, stretch=NO)

    for i in range(16):
        Macierz.heading(Kolumny[i],text=Kolumny[i])
        Macierz.column(Kolumny[i], minwidth=0, width=37, stretch=NO)
    Plotno.grid(row=0, columnspan=3, column=0,pady=2)
    ListaMiast.grid(row=0,column=3,pady=2,sticky=NSEW)
    Kasowanie.grid(row=1,column=3,pady=2)
    Zach.grid(row=1, column=0, pady=2)
    Wsp.grid(row=1, column=1, pady=2)
    Gla.grid(row=1, column=2, pady=2)
    Macierz.grid(row=0,column=4,pady=2,sticky=NS)

    Plotno.bind('<Button-1>', DodajMiasto)
    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
