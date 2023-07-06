from tabulate import tabulate
import termcolor
import sys
from colorama import Fore, Back, Style
import tkinter as tk
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from tkinter import Toplevel
from tkinter import Label
from tkinter import Entry
from tkinter import PhotoImage
from tkinter import Image
from PIL import ImageTk, Image, ImageTk as PIL_imagetk
import winsound
import random
import time
import threading
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.widgets import TextBox
import numpy as np
import os
import sys, subprocess


"""Alles hier in eine Funktion und ein Button um diese Funktion 
abzurufen bis der Button nochmal gedrückt wird, um zu restarten.
TODO:
- Testen, ob man Funktionen in Funktionen aufrufen kann
- Alle 

"""


"""Variablen Definierung Start"""
#Images 
global Bild0
global Bild1
global Bild2
global Bild3
global Bild4
global Bild5
global Bild6
global Bild7
global Bild8
global BildMine
global BildSave

#Andere Variablen
global SaveMarkierteFelder
SaveMarkierteFelder = []
global Sicherheit
Sicherheit = False
global TimeRunning
TimeRunning = False
global t1
global startTime
global Array_Minenfelder
Array_Minenfelder = []
#Statistiken
global Hilfecounter
Hilfecounter = 0
global Aufdeck_Zeiten
Aufdeck_Zeiten = [0]
global Felder_x
Felder_x = [0]
global Hilfe_Timer
Hilfe_Timer = []



#a0 = [Mine/Nummer/Leer, X, Y]
A0= [0,0,9,0]
A1= [0,1,9,0]
A2= [0,2,9,0]
A3= [0,3,9,0]
A4= [0,4,9,0]
A5= [0,5,9,0]
A6= [0,6,9,0]
A7= [0,7,9,0]
A8= [0,8,9,0]
A9= [0,9,9,0]

B0= [0,0,8,0]
B1= [0,1,8,0]
B2= [0,2,8,0]
B3= [0,3,8,0]
B4= [0,4,8,0]
B5= [0,5,8,0]
B6= [0,6,8,0]
B7= [0,7,8,0]
B8= [0,8,8,0]
B9= [0,9,8,0]

C0= [0,0,7,0]
C1= [0,1,7,0]
C2= [0,2,7,0]
C3= [0,3,7,0]
C4= [0,4,7,0]
C5= [0,5,7,0]
C6= [0,6,7,0]
C7= [0,7,7,0]
C8= [0,8,7,0]
C9= [0,9,7,0]

D0= [0,0,6,0]
D1= [0,1,6,0]
D2= [0,2,6,0]
D3= [0,3,6,0]
D4= [0,4,6,0]
D5= [0,5,6,0]
D6= [0,6,6,0]
D7= [0,7,6,0]
D8= [0,8,6,0]
D9= [0,9,6,0]

E0= [0,0,5,0]
E1= [0,1,5,0]
E2= [0,2,5,0]
E3= [0,3,5,0]
E4= [0,4,5,0]
E5= [0,5,5,0]
E6= [0,6,5,0]
E7= [0,7,5,0]
E8= [0,8,5,0]
E9= [0,9,5,0]

F0= [0,0,4,0]
F1= [0,1,4,0]
F2= [0,2,4,0]
F3= [0,3,4,0]
F4= [0,4,4,0]
F5= [0,5,4,0]
F6= [0,6,4,0]
F7= [0,7,4,0]
F8= [0,8,4,0]
F9= [0,9,4,0]

G0= [0,0,3,0]
G1= [0,1,3,0]
G2= [0,2,3,0]
G3= [0,3,3,0]
G4= [0,4,3,0]
G5= [0,5,3,0]
G6= [0,6,3,0]
G7= [0,7,3,0]
G8= [0,8,3,0]
G9= [0,9,3,0]

H0= [0,0,2,0]
H1= [0,1,2,0]
H2= [0,2,2,0]
H3= [0,3,2,0]
H4= [0,4,2,0]
H5= [0,5,2,0]
H6= [0,6,2,0]
H7= [0,7,2,0]
H8= [0,8,2,0]
H9= [0,9,2,0]

I0= [0,0,1,0]
I1= [0,1,1,0]
I2= [0,2,1,0]
I3= [0,3,1,0]
I4= [0,4,1,0]
I5= [0,5,1,0]
I6= [0,6,1,0]
I7= [0,7,1,0]
I8= [0,8,1,0]
I9= [0,9,1,0]

J0= [0,0,0,0]
J1= [0,1,0,0]
J2= [0,2,0,0]
J3= [0,3,0,0]
J4= [0,4,0,0]
J5= [0,5,0,0]
J6= [0,6,0,0]
J7= [0,7,0,0]
J8= [0,8,0,0]
J9= [0,9,0,0]

global Felderarray
Felderarray = [A0,A1,A2,A3,A4,A5,A6,A7,A8,A9,
               B0,B1,B2,B3,B4,B5,B6,B7,B8,B9,
               C0,C1,C2,C3,C4,C5,C6,C7,C8,C9,
               D0,D1,D2,D3,D4,D5,D6,D7,D8,D9,
               E0,E1,E2,E3,E4,E5,E6,E7,E8,E9,
               F0,F1,F2,F3,F4,F5,F6,F7,F8,F9,
               G0,G1,G2,G3,G4,G5,G6,G7,G8,G9,
               H0,H1,H2,H3,H4,H5,H6,H7,H8,H9,
               I0,I1,I2,I3,I4,I5,I6,I7,I8,I9,
               J0,J1,J2,J3,J4,J5,J6,J7,J8,J9]
global Testarray
Testarray = [[A0,A1,A2,A3,A4,A5,A6,A7,A8,A9],
             [B0,B1,B2,B3,B4,B5,B6,B7,B8,B9],
             [C0,C1,C2,C3,C4,C5,C6,C7,C8,C9],
             [D0,D1,D2,D3,D4,D5,D6,D7,D8,D9],
             [E0,E1,E2,E3,E4,E5,E6,E7,E8,E9],
             [F0,F1,F2,F3,F4,F5,F6,F7,F8,F9],
             [G0,G1,G2,G3,G4,G5,G6,G7,G8,G9],
             [H0,H1,H2,H3,H4,H5,H6,H7,H8,H9],
             [I0,I1,I2,I3,I4,I5,I6,I7,I8,I9],
             [J0,J1,J2,J3,J4,J5,J6,J7,J8,J9]]
global Stringarray
Stringarray = [["A0","A1","A2","A3","A4","A5","A6","A7","A8","A9"],
                ["B0","B1","B2","B3","B4","B5","B6","B7","B8","B9"],
                ["C0","C1","C2","C3","C4","C5","C6","C7","C8","C9"],
                ["D0","D1","D2","D3","D4","D5","D6","D7","D8","D9"],
                ["E0","E1","E2","E3","E4","E5","E6","E7","E8","E9"],
                ["F0","F1","F2","F3","F4","F5","F6","F7","F8","F9"],
                ["G0","G1","G2","G3","G4","G5","G6","G7","G8","G9"],
                ["H0","H1","H2","H3","H4","H5","H6","H7","H8","H9"],
                ["I0","I1","I2","I3","I4","I5","I6","I7","I8","I9"],
                ["J0","J1","J2","J3","J4","J5","J6","J7","J8","J9"]]

"""Variablen Definition Ende"""


"""Erstellung der Minen- und Zahlenfelder"""
def Zuweisung_der_Minenfelder():
    global Array_Minenfelder

    Array_Minenfelder = [[],[],[],[],[],[],[],[],[],[]]
    i = 0
    while i<10:
        X = random.randint(0, 9)
        Y = random.randint(0, 9)
        Str = str(X) + str(Y)
        #Prüfen, ob das Feld schon ausgewählt wurde
        P=True
        if i >0:
            for j in range(i):
                if Str == Array_Minenfelder[j][0]:
                    P = False
                    j=i+1
                else:
                    if P != False:
                        P = True
        else:
            Array_Minenfelder[i].append(Str)
            i+=1
            P=False
        if P == True:
            Array_Minenfelder[i].append(Str)
            i+=1

    #Die Minen in das Felderarray schreiben
    for i in Array_Minenfelder:
        for j in Felderarray:
            Str = str(j[1])+str(j[2])
            if i[0] == Str:
                j[0] = "Mine"

    #Die Zahlen Felder schreiben
    for i in Array_Minenfelder:
        Str = i[0]
        X = int(Str[0:1])
        Y = int(Str[1:])
        
        #Oben
        Oben = [X, Y+1]
        #ObenRechts
        ObenRechts = [X+1,Y+1]
        #Rechts
        Rechts = [X+1,Y]
        #UntenRechts
        UntenRechts = [X+1,Y-1]
        #Unten
        Unten = [X,Y-1]
        #UntenLinks
        UntenLinks = [X-1,Y-1]
        #Links
        Links = [X-1,Y]
        #ObenLinks
        ObenLinks = [X-1,Y+1]

        Anschließende_Felder = [Oben, ObenRechts, Rechts,UntenRechts, Unten, UntenLinks, Links, ObenLinks]

        #Die Koordinaten Suchen in der Felderarray
        #Die [0] +1 machen, wenn keine Mine drinsteht

        for j in Anschließende_Felder:
            StrRichtung = str(j[0])+str(j[1])
            for x in Felderarray:
                StrFeld = str(x[1])+str(x[2])
                if StrRichtung == StrFeld:
                    if x[0]!="Mine":
                        x[0]+=1
    print(Array_Minenfelder)
Zuweisung_der_Minenfelder()


"""Wenn ein leeres Feld gedrückt wird"""
def Leere_Felder_aufdecken(Str):
    Leere_Felder = []
    Geprüfte_Felder = []
    ZahlenFelder = []
    Leere_Felder.append(Str)

    Stopp = False
    while Stopp == False:           #Irgendwann muss der Loop stoppen
        for Feld in Leere_Felder:      #Jeder Eintrag in den Leeren Feldern, muss nach allen Seiten geprüft werden, um zu erkennen, ob dort weitere Leere Felder angrnezen, die leer sind und wiederum geprüft werden müssen
            #Prüfen ob das Feld schon geprüft wurde:
            if Feld in Geprüfte_Felder:
                #print("Wurde schon geprüft")
                if Feld == Leere_Felder[-1]:    #Wenn das letzte Feld geprüft wurde, muss die Schleife enden
                    Stopp = True
                    #print(Stopp, "Stopp")
            else:
                Geprüfte_Felder.append(Feld)
                #print("Wurde noch nicht geprüft")
                #print(Geprüfte_Felder, "Geprüfte Felder")
                X = globals()[Feld][1]                        
                Y = globals()[Feld][2]   

                Oben = [X,Y+1]
                Unten = [X,Y-1]
                Rechts = [X+1,Y]
                Links = [X-1,Y]
                Angrenzende_Felder = [Oben,Unten,Rechts,Links]
                #Prüfen ob diese Felder leer sind: und wenn ja, schreiben in die Leeren Felder
                for j in Angrenzende_Felder:
                    Ko1 = j[0]
                    Ko2 = j[1]
                    if Ko1 >-1 and Ko2 >-1 and Ko1<10 and Ko2<10:
                        F = Stringarray[9-Ko2][Ko1]
                        #Prüfen ob das Angrnezende Feld leer ist
                        if globals()[F][0] == 0:
                            Leere_Felder.append(F)   #Wenn leer, dann anfügen an die Leeren Felder
                        else:
                            ZahlenFelder.append(F)

    Leere_Felder = list(set(Leere_Felder))

    #Für Statistik
    f=Felder_x[-1]
    Felder_x.append(f+len(ZahlenFelder)+len(Leere_Felder))

    #Alle Leeren Felder in Bilder0 umwandeln
    for k in Leere_Felder:
        k=str(k)
        k = k.lower()
        x=0
        for i in ButtonsystemStr:
            if i == k:
                Buttonsystem[x]["image"] = Bild0
                Buttonsystem[x]["width"] = "0"
                Buttonsystem[x]["height"] = "0"
            else:
                x+=1

    #Alle Angrenzenden Zahlen Felder umwandeln
    for k in ZahlenFelder:
        k=str(k)
        k = k.lower()
        x=0
        for i in ButtonsystemStr:
            if i == k:
                k = k.upper()
                Bild = "Bild"+str(globals()[k][0])
                Buttonsystem[x]["image"] = globals()[Bild]
                Buttonsystem[x]["width"] = "0"
                Buttonsystem[x]["height"] = "0"
            else:
                x+=1
                
    #Alle aufgedeckten FElder als aufgedeckt kennzeichnen:
    for x  in Leere_Felder:
        globals()[x][3] =1
    for x  in ZahlenFelder:
        globals()[x][3] =1


"""Hier wird der Timer als Thread gestaret und geupdatet"""
def TimerStarten():
    global TimeRunning
    global startTime
    while TimeRunning == True:
        elapsedTime = time.time() - startTime
        timerLabel["text"] = round(elapsedTime,3)
        if elapsedTime <20:
            timerLabel["bg"] = "medium spring green"
        elif elapsedTime <30:
            timerLabel["bg"] = "yellow"
        elif elapsedTime <40:
            timerLabel["bg"] = "orange"
        elif elapsedTime <50:
            timerLabel["bg"] = "medium violet red"
        elif elapsedTime <60:
            timerLabel["bg"] = "maroon"


"""Wenn Button gedrückt wird"""
def ButtonToFunction(eff, Button):
    global Sicherheit
    global t1
    global TimeRunning
    global startTime
    global Aufdeck_Zeiten
    global Felder_x

    #Hier wird der Timer Gestartet beim Ersten KLick
    if TimeRunning == False:
        #Thread starten
        startTime = time.time()
        TimeRunning = True
        t1 = threading.Thread(target = TimerStarten)
        t1.start()
        print("t1 started")
        timerLabel["bg"] = "spring green"

    Str = str(Button)
    Str = Str.replace(".","")
    Str = Str.upper()
    Button = Str.lower()

    if globals()[Str][3] == 0:

        "Hier die Funktion zur Erhebung von statistischen Daten:"
        if timerLabel["text"] != "Timer":
            f = float(timerLabel["text"])
            f = round(f, 2)
            Aufdeck_Zeiten.append(f)
        else: 
            Aufdeck_Zeiten.append(0)

        #Spiel beenden, wenn MinenFeld
        if globals()[Str][0] == "Mine":
            x=0
            for i in ButtonsystemStr:
                if i == Button:
                    Buttonsystem[x]["image"] = BildMine
                    Buttonsystem[x]["width"] = "0"
                    Buttonsystem[x]["height"] = "0"
                    if Sicherheit == False:
                        Spiel_beenden("GameOver") #Wenn auf eine Mine getreten wurde = Game Over
                    else:
                        hilfeButton["bg"] = "white"
                        Sicherheit = False
                else:
                    x+=1

        elif globals()[Str][0] == 0:
            """Wenn 0 gewählt wird, müssen alle Felder daneben, die 0 sind aufgedeckt werden"""
            Leere_Felder_aufdecken(Str)

        elif globals()[Str][0] != 0:
            x=0
            for i in ButtonsystemStr:
                if i == Button:
                    Bild = "Bild"+str(globals()[Str][0])
                    Buttonsystem[x]["image"] = globals()[Bild]
                    Buttonsystem[x]["width"] = "0"
                    Buttonsystem[x]["height"] = "0"
                else:
                    x+=1

            #Statistik Daten
            f=Felder_x[-1]
            Felder_x.append(f+1)

        Sicherheit = False
        hilfeButton["bg"] = "white"

        "Hier die Funktion zum Testen, ob alle Felder aufgedeckt wurden:"
        Aufgedeckt_Gewinn_Test(Str)


"""Testet, ob alle Buttons aufgedeckt wurden"""
def Aufgedeckt_Gewinn_Test(Str):
    globals()[Str][3] = 1
    
    #Testen ob alle Felder schon aufgedeckt wurden
    for x in Felderarray:
        if x[0] != "Mine":
            if x[3]==1:
                if x == Felderarray[-1]:
                    print("Spiel_beenden")
                    Gewonnen = "Gewonnen"
                    Spiel_beenden(Gewonnen)
            else:
                break
        else:
            if x == Felderarray[-1]:
                print("Spiel_beenden")
                Gewonnen = "Gewonnen"
                Spiel_beenden(Gewonnen)


"""Minenfelder Markieren Rechtsklick"""
def right_click(eff, Button):
    #Abfrage, ob schon ein Bild da ist, wenn ja, wieder zurück zu nichts
    Str = str(Button)
    Str = Str.replace(".","")
    Str = Str.upper()
    Button = Str.lower()

    x=0
    for i in ButtonsystemStr:
        if i == Button:

            if Button in SaveMarkierteFelder:
                Buttonsystem[x]["image"] = ""
                Buttonsystem[x]["bg"] = "white"
                Buttonsystem[x]["width"] = 10
                Buttonsystem[x]["height"] = 4
                SaveMarkierteFelder.remove(Button)

            else:
                Buttonsystem[x]["image"] = BildSave
                Buttonsystem[x]["width"] = "0"
                Buttonsystem[x]["height"] = "0"
                SaveMarkierteFelder.append(Button)
        else:
            x+=1


"""Hier wird das Spiel beendet"""
def Spiel_beenden(Wert):
    #Den Timer Thread beenden
    global TimeRunning
    TimeRunning = False
    #Wenn auf Mine getreten wurde
    if Wert == "GameOver":
        print("ende")
        #Alle Minen aufdecken
        x=0
        while x<100:
            if Felderarray[x][0] == "Mine":
                Buttonsystem[x]["image"] = BildMine
                Buttonsystem[x]["width"] = "0"
                Buttonsystem[x]["height"] = "0"
            x+=1
    if Wert == "Gewonnen":
        print("Gewonnen")
    SiegesStatisik_Erstellen(Wert)


"""Hier kann ein Feld sicher aufgedeckt werden"""
def HilfeFeld(eff):
    global Sicherheit
    global Hilfecounter
    Sicherheit = True
    hilfeButton["bg"] = "green"
    Hilfecounter += 1
    if timerLabel["text"] != "Timer":
        f = float(timerLabel["text"])
        f = round(f, 2)
        Hilfe_Timer.append(f)


"""Hier wird die Statistik erstellt fürs Ende"""
def SiegesStatisik_Erstellen(Wert):
    global Hilfecounter
    t = timerLabel["text"]
    f = int(timerLabel["text"])

    if Wert != "Gewonnen":
        Aufdeck_Zeiten.pop(0)

    #Bewertung der Schwierigkeit des Spiels:
    Schwierigkeit =0
    for x in Felderarray:
        if x[0]!=0 and x[0]!="Mine":
            Schwierigkeit+=1
    Schwierigkeit = Schwierigkeit-8 # Weil 8 Die kleinste Schwierigkeit ist


    #Hier wird die Statistik erstellt:
    plt.plot(Aufdeck_Zeiten, Felder_x,marker = "o", color = "blue")
    for xc in Hilfe_Timer:
        plt.axvline(x=xc, color = "green", label= "Hilfe benutzt")

    z = Felder_x[-1]
    u = (z/100)*80
    r = (z/100)*60

    plt.text(0, z, "Gebrauchte Zeit:  " + str(t), ha='left', rotation=0, wrap=True)
    plt.text(0, u, "Gebrauchte Hilfe: " + str(Hilfecounter), ha='left', rotation=0, wrap=True)
    plt.text(0, r, "Schwierigkeit: " + str(Schwierigkeit)+" von 58", ha='left', rotation=0, wrap=True)
        
    """Beschriftung  des Graphen"""
    plt.xlabel("Zeit") #Gibt X Achsen Beschriftung
    plt.ylabel("Aufgedeckte Felder") #Gibt Y Achsen Beschriftung
    plt.title("Zeitstatistik") #Gibt den Titel an
    plt.legend() #Zeigt an, was als Label bei plt.plot angegeben  wurde
    plt.grid(True) #Zeigt ein Hintergrundgitter an

    plt.show()  #Zeigt das Diagramm an


"""Hier werden Fehler- ausgerpintet"""
def Print_All(eff):
    global Array_Minenfelder
    print(tabulate(Felderarray,"    Felderarray\n"))
    print(Array_Minenfelder,"   Minenfelder\n")
    # Schauen, welche Felder noch nicht aufgedeckt wurden:
    for x in Felderarray:
        if x[3] ==0:
            print(x , "     x")
    Aufgedeckt_Gewinn_Test("A1")


"""Hier kann alles neu gestartet werden"""
def Restart(eff):
    root.destroy()
    subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])


"""Alles für die GUI Start"""
root = tk.Tk()
root.geometry("1170x700")
root.title("Minesweeper")


#Bilder
BildSave = Image.open("Save.png")
BildSave = BildSave.resize((75,75))
BildSave = PIL_imagetk.PhotoImage(BildSave)

Bild0 = Image.open("0.png")
Bild0 = Bild0.resize((75,75))
Bild0 = PIL_imagetk.PhotoImage(Bild0)

Bild1 = Image.open("1.png")
Bild1 = Bild1.resize((75,75))
Bild1 = PIL_imagetk.PhotoImage(Bild1)

Bild2 = Image.open("2.png")
Bild2 = Bild2.resize((75,75))
Bild2 = PIL_imagetk.PhotoImage(Bild2)

Bild3 = Image.open("3.png")
Bild3 = Bild3.resize((75,75))
Bild3 = PIL_imagetk.PhotoImage(Bild3)

Bild4 = Image.open("4.png")
Bild4 = Bild4.resize((75,75))
Bild4 = PIL_imagetk.PhotoImage(Bild4)

Bild5 = Image.open("5.png")
Bild5 = Bild5.resize((75,75))
Bild5 = PIL_imagetk.PhotoImage(Bild5)

Bild6 = Image.open("6.png")
Bild6 = Bild6.resize((75,75))
Bild6 = PIL_imagetk.PhotoImage(Bild6)

Bild7 = Image.open("7.png")
Bild7 = Bild7.resize((75,75))
Bild7 = PIL_imagetk.PhotoImage(Bild7)

Bild8 = Image.open("8.png")
Bild8 = Bild8.resize((75,75))
Bild8 = PIL_imagetk.PhotoImage(Bild8)

BildMine = Image.open("Mine.png")
BildMine = BildMine.resize((75,75))
BildMine = PIL_imagetk.PhotoImage(BildMine)


a0=tk.Button(root, name="a0", width=10,height=4,bg='white')
a0.bind("<Button-1>", lambda eff: ButtonToFunction(eff, a0))
a0.bind("<Button-3>", lambda eff: right_click(eff, a0))
a0.place(x=0,y=0)
a1=tk.Button(root, name="a1", width=10,height=4,bg='white')
a1.bind("<Button-1>", lambda eff: ButtonToFunction(eff, a1))
a1.bind("<Button-3>", lambda eff: right_click(eff, a1))
a1.place(x=80,y=0)
a2=tk.Button(root, name="a2", width=10,height=4,bg='white')
a2.bind("<Button-1>", lambda eff: ButtonToFunction(eff, a2))
a2.bind("<Button-3>", lambda eff: right_click(eff, a2))
a2.place(x=160,y=0)
a3=tk.Button(root, name="a3", width=10,height=4,bg='white')
a3.bind("<Button-1>", lambda eff: ButtonToFunction(eff, a3))
a3.bind("<Button-3>", lambda eff: right_click(eff, a3))
a3.place(x=240,y=0)
a4=tk.Button(root, name="a4", width=10,height=4,bg='white')
a4.bind("<Button-1>", lambda eff: ButtonToFunction(eff, a4))
a4.bind("<Button-3>", lambda eff: right_click(eff, a4))
a4.place(x=320,y=0)
a5=tk.Button(root, name="a5", width=10,height=4,bg='white')
a5.bind("<Button-1>", lambda eff: ButtonToFunction(eff, a5))
a5.bind("<Button-3>", lambda eff: right_click(eff, a5))
a5.place(x=400,y=0)
a6=tk.Button(root, name="a6", width=10,height=4,bg='white')
a6.bind("<Button-1>", lambda eff: ButtonToFunction(eff, a6))
a6.bind("<Button-3>", lambda eff: right_click(eff, a6))
a6.place(x=480,y=0)
a7=tk.Button(root, name="a7", width=10,height=4,bg='white')
a7.bind("<Button-1>", lambda eff: ButtonToFunction(eff, a7))
a7.bind("<Button-3>", lambda eff: right_click(eff, a7))
a7.place(x=560,y=0)
a8=tk.Button(root, name="a8", width=10,height=4,bg='white')
a8.bind("<Button-1>", lambda eff: ButtonToFunction(eff, a8))
a8.bind("<Button-3>", lambda eff: right_click(eff, a8))
a8.place(x=640,y=0)
a9=tk.Button(root, name="a9", width=10,height=4,bg='white')
a9.bind("<Button-1>", lambda eff: ButtonToFunction(eff, a9))
a9.bind("<Button-3>", lambda eff: right_click(eff, a9))
a9.place(x=720,y=0)

b0=tk.Button(root, name="b0", width=10,height=4,bg='white')
b0.bind("<Button-1>", lambda eff: ButtonToFunction(eff, b0))
b0.bind("<Button-3>", lambda eff: right_click(eff, b0))
b0.place(x=0,y=70)
b1=tk.Button(root, name="b1", width=10,height=4,bg='white')
b1.bind("<Button-1>", lambda eff: ButtonToFunction(eff, b1))
b1.bind("<Button-3>", lambda eff: right_click(eff, b1))
b1.place(x=80,y=70)
b2=tk.Button(root, name="b2", width=10,height=4,bg='white')
b2.bind("<Button-1>", lambda eff: ButtonToFunction(eff, b2))
b2.bind("<Button-3>", lambda eff: right_click(eff, b2))
b2.place(x=160,y=70)
b3=tk.Button(root, name="b3", width=10,height=4,bg='white')
b3.bind("<Button-1>", lambda eff: ButtonToFunction(eff, b3))
b3.bind("<Button-3>", lambda eff: right_click(eff, b3))
b3.place(x=240,y=70)
b4=tk.Button(root, name="b4", width=10,height=4,bg='white')
b4.bind("<Button-1>", lambda eff: ButtonToFunction(eff, b4))
b4.bind("<Button-3>", lambda eff: right_click(eff, b4))
b4.place(x=320,y=70)
b5=tk.Button(root, name="b5", width=10,height=4,bg='white')
b5.bind("<Button-1>", lambda eff: ButtonToFunction(eff, b5))
b5.bind("<Button-3>", lambda eff: right_click(eff, b5))
b5.place(x=400,y=70)
b6=tk.Button(root, name="b6", width=10,height=4,bg='white')
b6.bind("<Button-1>", lambda eff: ButtonToFunction(eff, b6))
b6.bind("<Button-3>", lambda eff: right_click(eff, b6))
b6.place(x=480,y=70)
b7=tk.Button(root, name="b7", width=10,height=4,bg='white')
b7.bind("<Button-1>", lambda eff: ButtonToFunction(eff, b7))
b7.bind("<Button-3>", lambda eff: right_click(eff, b7))
b7.place(x=560,y=70)
b8=tk.Button(root, name="b8", width=10,height=4,bg='white')
b8.bind("<Button-1>", lambda eff: ButtonToFunction(eff, b8))
b8.bind("<Button-3>", lambda eff: right_click(eff, b8))
b8.place(x=640,y=70)
b9=tk.Button(root, name="b9", width=10,height=4,bg='white')
b9.bind("<Button-1>", lambda eff: ButtonToFunction(eff, b9))
b9.bind("<Button-3>", lambda eff: right_click(eff, b9))
b9.place(x=720,y=70)

c0=tk.Button(root, name="c0", width=10,height=4,bg='white')
c0.bind("<Button-1>", lambda eff: ButtonToFunction(eff, c0))
c0.bind("<Button-3>", lambda eff: right_click(eff, c0))
c0.place(x=0,y=140)
c1=tk.Button(root, name="c1", width=10,height=4,bg='white')
c1.bind("<Button-1>", lambda eff: ButtonToFunction(eff, c1))
c1.bind("<Button-3>", lambda eff: right_click(eff, c1))
c1.place(x=80,y=140)
c2=tk.Button(root, name="c2", width=10,height=4,bg='white')
c2.bind("<Button-1>", lambda eff: ButtonToFunction(eff, c2))
c2.bind("<Button-3>", lambda eff: right_click(eff, c2))
c2.place(x=160,y=140)
c3=tk.Button(root, name="c3", width=10,height=4,bg='white')
c3.bind("<Button-1>", lambda eff: ButtonToFunction(eff, c3))
c3.bind("<Button-3>", lambda eff: right_click(eff, c3))
c3.place(x=240,y=140)
c4=tk.Button(root, name="c4", width=10,height=4,bg='white')
c4.bind("<Button-1>", lambda eff: ButtonToFunction(eff, c4))
c4.bind("<Button-3>", lambda eff: right_click(eff, c4))
c4.place(x=320,y=140)
c5=tk.Button(root, name="c5", width=10,height=4,bg='white')
c5.bind("<Button-1>", lambda eff: ButtonToFunction(eff, c5))
c5.bind("<Button-3>", lambda eff: right_click(eff, c5))
c5.place(x=400,y=140)
c6=tk.Button(root, name="c6", width=10,height=4,bg='white')
c6.bind("<Button-1>", lambda eff: ButtonToFunction(eff, c6))
c6.bind("<Button-3>", lambda eff: right_click(eff, c6))
c6.place(x=480,y=140)
c7=tk.Button(root, name="c7", width=10,height=4,bg='white')
c7.bind("<Button-1>", lambda eff: ButtonToFunction(eff, c7))
c7.bind("<Button-3>", lambda eff: right_click(eff, c7))
c7.place(x=560,y=140)
c8=tk.Button(root, name="c8", width=10,height=4,bg='white')
c8.bind("<Button-1>", lambda eff: ButtonToFunction(eff, c8))
c8.bind("<Button-3>", lambda eff: right_click(eff, c8))
c8.place(x=640,y=140)
c9=tk.Button(root, name="c9", width=10,height=4,bg='white')
c9.bind("<Button-1>", lambda eff: ButtonToFunction(eff, c9))
c9.bind("<Button-3>", lambda eff: right_click(eff, c9))
c9.place(x=720,y=140)

d0=tk.Button(root, name="d0", width=10,height=4,bg='white')
d0.bind("<Button-1>", lambda eff: ButtonToFunction(eff, d0))
d0.bind("<Button-3>", lambda eff: right_click(eff, d0))
d0.place(x=0,y=210)
d1=tk.Button(root, name="d1", width=10,height=4,bg='white')
d1.bind("<Button-1>", lambda eff: ButtonToFunction(eff, d1))
d1.bind("<Button-3>", lambda eff: right_click(eff, d1))
d1.place(x=80,y=210)
d2=tk.Button(root, name="d2", width=10,height=4,bg='white')
d2.bind("<Button-1>", lambda eff: ButtonToFunction(eff, d2))
d2.bind("<Button-3>", lambda eff: right_click(eff, d2))
d2.place(x=160,y=210)
d3=tk.Button(root, name="d3", width=10,height=4,bg='white')
d3.bind("<Button-1>", lambda eff: ButtonToFunction(eff, d3))
d3.bind("<Button-3>", lambda eff: right_click(eff, d3))
d3.place(x=240,y=210)
d4=tk.Button(root, name="d4", width=10,height=4,bg='white')
d4.bind("<Button-1>", lambda eff: ButtonToFunction(eff, d4))
d4.bind("<Button-3>", lambda eff: right_click(eff, d4))
d4.place(x=320,y=210)
d5=tk.Button(root, name="d5", width=10,height=4,bg='white')
d5.bind("<Button-1>", lambda eff: ButtonToFunction(eff, d5))
d5.bind("<Button-3>", lambda eff: right_click(eff, d5))
d5.place(x=400,y=210)
d6=tk.Button(root, name="d6", width=10,height=4,bg='white')
d6.bind("<Button-1>", lambda eff: ButtonToFunction(eff, d6))
d6.bind("<Button-3>", lambda eff: right_click(eff, d6))
d6.place(x=480,y=210)
d7=tk.Button(root, name="d7", width=10,height=4,bg='white')
d7.bind("<Button-1>", lambda eff: ButtonToFunction(eff, d7))
d7.bind("<Button-3>", lambda eff: right_click(eff, d7))
d7.place(x=560,y=210)
d8=tk.Button(root, name="d8", width=10,height=4,bg='white')
d8.bind("<Button-1>", lambda eff: ButtonToFunction(eff, d8))
d8.bind("<Button-3>", lambda eff: right_click(eff, d8))
d8.place(x=640,y=210)
d9=tk.Button(root, name="d9", width=10,height=4,bg='white')
d9.bind("<Button-1>", lambda eff: ButtonToFunction(eff, d9))
d9.bind("<Button-3>", lambda eff: right_click(eff, d9))
d9.place(x=720,y=210)

e0=tk.Button(root, name="e0", width=10,height=4,bg='white')
e0.bind("<Button-1>", lambda eff: ButtonToFunction(eff, e0))
e0.bind("<Button-3>", lambda eff: right_click(eff, e0))
e0.place(x=0,y=280)
e1=tk.Button(root, name="e1", width=10,height=4,bg='white')
e1.bind("<Button-1>", lambda eff: ButtonToFunction(eff, e1))
e1.bind("<Button-3>", lambda eff: right_click(eff, e1))
e1.place(x=80,y=280)
e2=tk.Button(root, name="e2", width=10,height=4,bg='white')
e2.bind("<Button-1>", lambda eff: ButtonToFunction(eff, e2))
e2.bind("<Button-3>", lambda eff: right_click(eff, e2))
e2.place(x=160,y=280)
e3=tk.Button(root, name="e3", width=10,height=4,bg='white')
e3.bind("<Button-1>", lambda eff: ButtonToFunction(eff, e3))
e3.bind("<Button-3>", lambda eff: right_click(eff, e3))
e3.place(x=240,y=280)
e4=tk.Button(root, name="e4", width=10,height=4,bg='white')
e4.bind("<Button-1>", lambda eff: ButtonToFunction(eff, e4))
e4.bind("<Button-3>", lambda eff: right_click(eff, e4))
e4.place(x=320,y=280)
e5=tk.Button(root, name="e5", width=10,height=4,bg='white')
e5.bind("<Button-1>", lambda eff: ButtonToFunction(eff, e5))
e5.bind("<Button-3>", lambda eff: right_click(eff, e5))
e5.place(x=400,y=280)
e6=tk.Button(root, name="e6", width=10,height=4,bg='white')
e6.bind("<Button-1>", lambda eff: ButtonToFunction(eff, e6))
e6.bind("<Button-3>", lambda eff: right_click(eff, e6))
e6.place(x=480,y=280)
e7=tk.Button(root, name="e7", width=10,height=4,bg='white')
e7.bind("<Button-1>", lambda eff: ButtonToFunction(eff, e7))
e7.bind("<Button-3>", lambda eff: right_click(eff, e7))
e7.place(x=560,y=280)
e8=tk.Button(root, name="e8", width=10,height=4,bg='white')
e8.bind("<Button-1>", lambda eff: ButtonToFunction(eff, e8))
e8.bind("<Button-3>", lambda eff: right_click(eff, e8))
e8.place(x=640,y=280)
e9=tk.Button(root, name="e9", width=10,height=4,bg='white')
e9.bind("<Button-1>", lambda eff: ButtonToFunction(eff, e9))
e9.bind("<Button-3>", lambda eff: right_click(eff, e9))
e9.place(x=720,y=280)

f0=tk.Button(root, name="f0", width=10,height=4,bg='white')
f0.bind("<Button-1>", lambda eff: ButtonToFunction(eff, f0))
f0.bind("<Button-3>", lambda eff: right_click(eff, f0))
f0.place(x=0,y=350)
f1=tk.Button(root, name="f1", width=10,height=4,bg='white')
f1.bind("<Button-1>", lambda eff: ButtonToFunction(eff, f1))
f1.bind("<Button-3>", lambda eff: right_click(eff, f1))
f1.place(x=80,y=350)
f2=tk.Button(root, name="f2", width=10,height=4,bg='white')
f2.bind("<Button-1>", lambda eff: ButtonToFunction(eff, f2))
f2.bind("<Button-3>", lambda eff: right_click(eff, f2))
f2.place(x=160,y=350)
f3=tk.Button(root, name="f3", width=10,height=4,bg='white')
f3.bind("<Button-1>", lambda eff: ButtonToFunction(eff, f3))
f3.bind("<Button-3>", lambda eff: right_click(eff, f3))
f3.place(x=240,y=350)
f4=tk.Button(root, name="f4", width=10,height=4,bg='white')
f4.bind("<Button-1>", lambda eff: ButtonToFunction(eff, f4))
f4.bind("<Button-3>", lambda eff: right_click(eff, f4))
f4.place(x=320,y=350)
f5=tk.Button(root, name="f5", width=10,height=4,bg='white')
f5.bind("<Button-1>", lambda eff: ButtonToFunction(eff, f5))
f5.bind("<Button-3>", lambda eff: right_click(eff, f5))
f5.place(x=400,y=350)
f6=tk.Button(root, name="f6", width=10,height=4,bg='white')
f6.bind("<Button-1>", lambda eff: ButtonToFunction(eff, f6))
f6.bind("<Button-3>", lambda eff: right_click(eff, f6))
f6.place(x=480,y=350)
f7=tk.Button(root, name="f7", width=10,height=4,bg='white')
f7.bind("<Button-1>", lambda eff: ButtonToFunction(eff, f7))
f7.bind("<Button-3>", lambda eff: right_click(eff, f7))
f7.place(x=560,y=350)
f8=tk.Button(root, name="f8", width=10,height=4,bg='white')
f8.bind("<Button-1>", lambda eff: ButtonToFunction(eff, f8))
f8.bind("<Button-3>", lambda eff: right_click(eff, f8))
f8.place(x=640,y=350)
f9=tk.Button(root, name="f9", width=10,height=4,bg='white')
f9.bind("<Button-1>", lambda eff: ButtonToFunction(eff, f9))
f9.bind("<Button-3>", lambda eff: right_click(eff, f9))
f9.place(x=720,y=350)

g0=tk.Button(root, name="g0", width=10,height=4,bg='white')
g0.bind("<Button-1>", lambda eff: ButtonToFunction(eff, g0))
g0.bind("<Button-3>", lambda eff: right_click(eff, g0))
g0.place(x=0,y=420)
g1=tk.Button(root, name="g1", width=10,height=4,bg='white')
g1.bind("<Button-1>", lambda eff: ButtonToFunction(eff, g1))
g1.bind("<Button-3>", lambda eff: right_click(eff, g1))
g1.place(x=80,y=420)
g2=tk.Button(root, name="g2", width=10,height=4,bg='white')
g2.bind("<Button-1>", lambda eff: ButtonToFunction(eff, g2))
g2.bind("<Button-3>", lambda eff: right_click(eff, g2))
g2.place(x=160,y=420)
g3=tk.Button(root, name="g3", width=10,height=4,bg='white')
g3.bind("<Button-1>", lambda eff: ButtonToFunction(eff, g3))
g3.bind("<Button-3>", lambda eff: right_click(eff, g3))
g3.place(x=240,y=420)
g4=tk.Button(root, name="g4", width=10,height=4,bg='white')
g4.bind("<Button-1>", lambda eff: ButtonToFunction(eff, g4))
g4.bind("<Button-3>", lambda eff: right_click(eff, g4))
g4.place(x=320,y=420)
g5=tk.Button(root, name="g5", width=10,height=4,bg='white')
g5.bind("<Button-1>", lambda eff: ButtonToFunction(eff, g5))
g5.bind("<Button-3>", lambda eff: right_click(eff, g5))
g5.place(x=400,y=420)
g6=tk.Button(root, name="g6", width=10,height=4,bg='white')
g6.bind("<Button-1>", lambda eff: ButtonToFunction(eff, g6))
g6.bind("<Button-3>", lambda eff: right_click(eff, g6))
g6.place(x=480,y=420)
g7=tk.Button(root, name="g7", width=10,height=4,bg='white')
g7.bind("<Button-1>", lambda eff: ButtonToFunction(eff, g7))
g7.bind("<Button-3>", lambda eff: right_click(eff, g7))
g7.place(x=560,y=420)
g8=tk.Button(root, name="g8", width=10,height=4,bg='white')
g8.bind("<Button-1>", lambda eff: ButtonToFunction(eff, g8))
g8.bind("<Button-3>", lambda eff: right_click(eff, g8))
g8.place(x=640,y=420)
g9=tk.Button(root, name="g9", width=10,height=4,bg='white')
g9.bind("<Button-1>", lambda eff: ButtonToFunction(eff, g9))
g9.bind("<Button-3>", lambda eff: right_click(eff, g9))
g9.place(x=720,y=420)

h0=tk.Button(root, name="h0", width=10,height=4,bg='white')
h0.bind("<Button-1>", lambda eff: ButtonToFunction(eff, h0))
h0.bind("<Button-3>", lambda eff: right_click(eff, h0))
h0.place(x=0,y=490)
h1=tk.Button(root, name="h1", width=10,height=4,bg='white')
h1.bind("<Button-1>", lambda eff: ButtonToFunction(eff, h1))
h1.bind("<Button-3>", lambda eff: right_click(eff, h1))
h1.place(x=80,y=490)
h2=tk.Button(root, name="h2", width=10,height=4,bg='white')
h2.bind("<Button-1>", lambda eff: ButtonToFunction(eff, h2))
h2.bind("<Button-3>", lambda eff: right_click(eff, h2))
h2.place(x=160,y=490)
h3=tk.Button(root, name="h3", width=10,height=4,bg='white')
h3.bind("<Button-1>", lambda eff: ButtonToFunction(eff, h3))
h3.bind("<Button-3>", lambda eff: right_click(eff, h3))
h3.place(x=240,y=490)
h4=tk.Button(root, name="h4", width=10,height=4,bg='white')
h4.bind("<Button-1>", lambda eff: ButtonToFunction(eff, h4))
h4.bind("<Button-3>", lambda eff: right_click(eff, h4))
h4.place(x=320,y=490)
h5=tk.Button(root, name="h5", width=10,height=4,bg='white')
h5.bind("<Button-1>", lambda eff: ButtonToFunction(eff, h5))
h5.bind("<Button-3>", lambda eff: right_click(eff, h5))
h5.place(x=400,y=490)
h6=tk.Button(root, name="h6", width=10,height=4,bg='white')
h6.bind("<Button-1>", lambda eff: ButtonToFunction(eff, h6))
h6.bind("<Button-3>", lambda eff: right_click(eff, h6))
h6.place(x=480,y=490)
h7=tk.Button(root, name="h7", width=10,height=4,bg='white')
h7.bind("<Button-1>", lambda eff: ButtonToFunction(eff, h7))
h7.bind("<Button-3>", lambda eff: right_click(eff, h7))
h7.place(x=560,y=490)
h8=tk.Button(root, name="h8", width=10,height=4,bg='white')
h8.bind("<Button-1>", lambda eff: ButtonToFunction(eff, h8))
h8.bind("<Button-3>", lambda eff: right_click(eff, h8))
h8.place(x=640,y=490)
h9=tk.Button(root, name="h9", width=10,height=4,bg='white')
h9.bind("<Button-1>", lambda eff: ButtonToFunction(eff, h9))
h9.bind("<Button-3>", lambda eff: right_click(eff, h9))
h9.place(x=720,y=490)

i0=tk.Button(root, name="i0", width=10,height=4,bg='white')
i0.bind("<Button-1>", lambda eff: ButtonToFunction(eff, i0))
i0.bind("<Button-3>", lambda eff: right_click(eff, i0))
i0.place(x=0,y=560)
i1=tk.Button(root, name="i1", width=10,height=4,bg='white')
i1.bind("<Button-1>", lambda eff: ButtonToFunction(eff, i1))
i1.bind("<Button-3>", lambda eff: right_click(eff, i1))
i1.place(x=80,y=560)
i2=tk.Button(root, name="i2", width=10,height=4,bg='white')
i2.bind("<Button-1>", lambda eff: ButtonToFunction(eff, i2))
i2.bind("<Button-3>", lambda eff: right_click(eff, i2))
i2.place(x=160,y=560)
i3=tk.Button(root, name="i3", width=10,height=4,bg='white')
i3.bind("<Button-1>", lambda eff: ButtonToFunction(eff, i3))
i3.bind("<Button-3>", lambda eff: right_click(eff, i3))
i3.place(x=240,y=560)
i4=tk.Button(root, name="i4", width=10,height=4,bg='white')
i4.bind("<Button-1>", lambda eff: ButtonToFunction(eff, i4))
i4.bind("<Button-3>", lambda eff: right_click(eff, i4))
i4.place(x=320,y=560)
i5=tk.Button(root, name="i5", width=10,height=4,bg='white')
i5.bind("<Button-1>", lambda eff: ButtonToFunction(eff, i5))
i5.bind("<Button-3>", lambda eff: right_click(eff, i5))
i5.place(x=400,y=560)
i6=tk.Button(root, name="i6", width=10,height=4,bg='white')
i6.bind("<Button-1>", lambda eff: ButtonToFunction(eff, i6))
i6.bind("<Button-3>", lambda eff: right_click(eff, i6))
i6.place(x=480,y=560)
i7=tk.Button(root, name="i7", width=10,height=4,bg='white')
i7.bind("<Button-1>", lambda eff: ButtonToFunction(eff, i7))
i7.bind("<Button-3>", lambda eff: right_click(eff, i7))
i7.place(x=560,y=560)
i8=tk.Button(root, name="i8", width=10,height=4,bg='white')
i8.bind("<Button-1>", lambda eff: ButtonToFunction(eff, i8))
i8.bind("<Button-3>", lambda eff: right_click(eff, i8))
i8.place(x=640,y=560)
i9=tk.Button(root, name="i9", width=10,height=4,bg='white')
i9.bind("<Button-1>", lambda eff: ButtonToFunction(eff, i9))
i9.bind("<Button-3>", lambda eff: right_click(eff, i9))
i9.place(x=720,y=560)

j0=tk.Button(root, name="j0", width=10,height=4,bg='white')
j0.bind("<Button-1>", lambda eff: ButtonToFunction(eff, j0))
j0.bind("<Button-3>", lambda eff: right_click(eff, j0))
j0.place(x=0,y=630)
j1=tk.Button(root, name="j1", width=10,height=4,bg='white')
j1.bind("<Button-1>", lambda eff: ButtonToFunction(eff, j1))
j1.bind("<Button-3>", lambda eff: right_click(eff, j1))
j1.place(x=80,y=630)
j2=tk.Button(root, name="j2", width=10,height=4,bg='white')
j2.bind("<Button-1>", lambda eff: ButtonToFunction(eff, j2))
j2.bind("<Button-3>", lambda eff: right_click(eff, j2))
j2.place(x=160,y=630)
j3=tk.Button(root, name="j3", width=10,height=4,bg='white')
j3.bind("<Button-1>", lambda eff: ButtonToFunction(eff, j3))
j3.bind("<Button-3>", lambda eff: right_click(eff, j3))
j3.place(x=240,y=630)
j4=tk.Button(root, name="j4", width=10,height=4,bg='white')
j4.bind("<Button-1>", lambda eff: ButtonToFunction(eff, j4))
j4.bind("<Button-3>", lambda eff: right_click(eff, j4))
j4.place(x=320,y=630)
j5=tk.Button(root, name="j5", width=10,height=4,bg='white')
j5.bind("<Button-1>", lambda eff: ButtonToFunction(eff, j5))
j5.bind("<Button-3>", lambda eff: right_click(eff, j5))
j5.place(x=400,y=630)
j6=tk.Button(root, name="j6", width=10,height=4,bg='white')
j6.bind("<Button-1>", lambda eff: ButtonToFunction(eff, j6))
j6.bind("<Button-3>", lambda eff: right_click(eff, j6))
j6.place(x=480,y=630)
j7=tk.Button(root, name="j7", width=10,height=4,bg='white')
j7.bind("<Button-1>", lambda eff: ButtonToFunction(eff, j7))
j7.bind("<Button-3>", lambda eff: right_click(eff, j7))
j7.place(x=560,y=630)
j8=tk.Button(root, name="j8", width=10,height=4,bg='white')
j8.bind("<Button-1>", lambda eff: ButtonToFunction(eff, j8))
j8.bind("<Button-3>", lambda eff: right_click(eff, j8))
j8.place(x=640,y=630)
j9=tk.Button(root, name="j9", width=10,height=4,bg='white')
j9.bind("<Button-1>", lambda eff: ButtonToFunction(eff, j9))
j9.bind("<Button-3>", lambda eff: right_click(eff, j9))
j9.place(x=720,y=630)


hilfeButton=tk.Button(root, text = "Hilfe",name="hilfeButton", width=30,height=10,bg='white')
hilfeButton.bind("<Button-1>", lambda eff: HilfeFeld(eff))
hilfeButton.place(x=900,y=315)

timerLabel=tk.Label(root, text = "Timer",name="timerLabel", width=30,height=10,bg='white')
timerLabel.place(x=900,y=0)

printall=tk.Button(root, text = "Print All",name="printall", width=30,height=10,bg='white')
printall.bind("<Button-1>", lambda eff: Print_All(eff))
printall.place(x=900,y=500)

restart=tk.Button(root, text = "restart",name="restart", width=30,height=8,bg='white')
restart.bind("<Button-1>", lambda eff: Restart(eff))
restart.place(x=900,y=170)

global Buttonsystem
Buttonsystem = [a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,
               b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,
               c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,
               d0,d1,d2,d3,d4,d5,d6,d7,d8,d9,
               e0,e1,e2,e3,e4,e5,e6,e7,e8,e9,
               f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,
               g0,g1,g2,g3,g4,g5,g6,g7,g8,g9,
               h0,h1,h2,h3,h4,h5,h6,h7,h8,h9,
               i0,i1,i2,i3,i4,i5,i6,i7,i8,i9,
               j0,j1,j2,j3,j4,j5,j6,j7,j8,j9, 
               hilfeButton, timerLabel, printall, restart]

global ButtonsystemStr
ButtonsystemStr = ["a0","a1","a2","a3","a4","a5","a6","a7","a8","a9",
               "b0","b1","b2","b3","b4","b5","b6","b7","b8","b9",
               "c0","c1","c2","c3","c4","c5","c6","c7","c8","c9",
               "d0","d1","d2","d3","d4","d5","d6","d7","d8","d9",
               "e0","e1","e2","e3","e4","e5","e6","e7","e8","e9",
               "f0","f1","f2","f3","f4","f5","f6","f7","f8","f9",
               "g0","g1","g2","g3","g4","g5","g6","g7","g8","g9",
               "h0","h1","h2","h3","h4","h5","h6","h7","h8","h9",
               "i0","i1","i2","i3","i4","i5","i6","i7","i8","i9",
               "j0","j1","j2","j3","j4","j5","j6","j7","j8","j9"]


"""Das erste Feld wird aufgedeckt"""
def ErstesFeldaufdecken():
    #Von oben durchprobieren, bis zum ersten leeren Feld
    x=0
    t=True
    while t == True and x<100:
        if Felderarray[x][0] == 0:
            Buttonsystem[x]["image"] = Bild0
            Buttonsystem[x]["width"] = "0"
            Buttonsystem[x]["height"] = "0"
            t=False
        else:
            x+=1

    #Minenfelder Rot färben
    f=0
    for i in Felderarray:
        f+=1
        if i[0] == "Mine":
            Buttonsystem[f-1]["bg"] = "red"

ErstesFeldaufdecken()

root.mainloop()
"""Alles "für die GUI Ende"""






"""Todos:
Highscore Save
"""