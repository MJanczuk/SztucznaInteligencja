# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *
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
    Kreski = []
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

    def DodajMiasto(e):
        if len(Miasta)<15:Miasta.append(miasto(e.x,e.y))

        LiczbaMiast = ListaMiast.size()
        if LiczbaMiast<15:
            Plotno.create_oval(e.x-6,e.y-6,e.x+6,e.y+6,fill=Kolory(LiczbaMiast))
            ListaMiast.insert(END,'Miasto '+ f'{(LiczbaMiast):02d}' + ' [X:' + f'{(e.x):03d}'+',Y:'+f'{(e.y):03d}'+']')

    def Wyczysc():
        Plotno.delete(ALL)
        ListaMiast.delete(0,ListaMiast.size())
        Miasta.clear()

    def Koordynaty(numer):
        Nazwa = ListaMiast.get(numer)
        return(int(Nazwa[-10:-7]),int(Nazwa[-4:-1]))

    def Koordynaty2(numer):
        return(int(Miasta[numer].x),int(Miasta[numer].y))

    def Odleglosc(m1,m2):
        (x1,y1) = Koordynaty2(m1)
        (x2,y2) = Koordynaty2(m2)
        return math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))

    def Srodek(m1,m2):
        (x1,y1) = Koordynaty2(m1)
        (x2,y2) = Koordynaty2(m2)
        return ((x2+x1)/2, (y2+y1)/2)

    def Zachlanny():
        Kreski.clear()
    def Wspinaczkowy():
        Kreski.append(1)
    def Glab():
        ps = ListaMiast.curselection()
        if ps == ():
            ps = (0,)
        M1 = ps[0]
        M2 = M1 + 1
        Plotno.create_text(Srodek(M1,M2),text=f'{(Odleglosc(M1,M2)):0.1f}',)
        Plotno.create_line(Koordynaty2(M1),Koordynaty2(M2),fill='grey')

    root = Tk()
    root.title('Mapa')
    #root.geometry("1010x810")
    Plotno = Canvas(root,width=400,height=400,bg="white")
    ListaMiast = Listbox(root, selectmode=SINGLE)
    Kasowanie = Button(root, width=15, height=2, text='Wyczysc',command=Wyczysc)
    Zach = Button(root, width=15, height=2, text='Algorytm \nZachłanny', command=Zachlanny)
    Wsp = Button(root, width=15, height=2, text='Algorytm \nWspinaczkowy', command=Wspinaczkowy)
    Gla = Button(root, width=15, height=2, text='Algorytm \nWgłąb', command=Glab)

    Plotno.grid(row=0, columnspan=3, column=0,pady=2)
    ListaMiast.grid(row=0,column=3,pady=2,sticky=NSEW)
    Kasowanie.grid(row=1,column=3,pady=2)
    Zach.grid(row=1, column=0, pady=2)
    Wsp.grid(row=1, column=1, pady=2)
    Gla.grid(row=1, column=2, pady=2)

    Plotno.bind('<Button-1>', DodajMiasto)
    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
