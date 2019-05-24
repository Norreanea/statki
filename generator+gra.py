from random import randrange
class Statek():

    length = 1
    status_mapy = []
    mapa_wspolrzednych = []
    #punkty wokół statku
    wokol_mapy = []
    #statek nie wychodzi poza pole
    sprawdzanie = 1

    
    def __init__(self,length,pozycja,krata): #pozycja '0' = pozioma, '1' = pionowa
        self.status_mapy = []
        self.mapa_wspolrzednych = []
        self.wokol_mapy = []
        self.sprawdzanie = 1
        self.length = length
        wiersz = int(krata.split("_")[0])
        kolumna = int(krata.split("_")[1])
        for i in range(length):
            self.status_mapy.append(0)
            #0 - horyzont (zwiększenie kolumny), 1 - pion (zwiększenie wierszu)
            if kolumna + i > 9 or wiersz + i > 9:
                self.sprawdzanie = 0
            if pozycja == 0:
                #jeśli pozycja pozioma, na osi Y punkt wyjściowy ograniczamy do 11-liczba maszt 
                self.mapa_wspolrzednych.append(str(wiersz)+"_"+str(kolumna+i))
            else:
                self.mapa_wspolrzednych.append(str(wiersz+i)+"_"+str(kolumna))
   
def generator():
        statki = 0
        while statki < 10:
            global statki_kratki
            #lista zajmowanych przez statki kratek
            statki_kratki = []
            statki = 0
            statki_lista = []
            #generowanie statku (długość - liczba maszt)
            for length in reversed(range(1,5)):
                    #w taki sposób generujemy 4 jednomasztowca, 3 dwumasztowca i t.d
                    for i in range(5-length):
                        gen_statek = 0
                        while 1:
                            gen_statek += 1
                            
                            #generowanie punktów
                            kratka = str(randrange(9)+1)+"_"+str(randrange(9)+1)
                            #losowa pozycja statku
                            pozycja = randrange(2)
                            if pozycja == 0:
                                poz = "pozycja pozioma"
                            else:
                                poz = "pozycja pionowa"
                            #tworzymy przedstawiciela Statków
                            nowy_statek = Statek(length,pozycja,kratka)
                            #koordynaty się nie przecinają z już zajętymi
                            krzyzowanie = list(set(statki_kratki) & set(nowy_statek.wokol_mapy+nowy_statek.mapa_wspolrzednych))
                            if nowy_statek.sprawdzanie == 1 and len(krzyzowanie) == 0:
                                #dodajemy do listy wszystkie zajęte kratki wokół statku i koordynatę samego statku
                                statki_kratki += nowy_statek.wokol_mapy + nowy_statek.mapa_wspolrzednych
                                statki_lista.append(nowy_statek)
                                print(length, "- masztowiec", "kratka początkowa",kratka, poz)
                                statki += 1
                                break

generator()

punkty = [s.split(',') for s in statki_kratki]
print(punkty)


#####________________plansza
plansza = []

for x in range(1,11):
    plansza.append(["o"] * 10)

def print_board(plansza):
    for row in plansza:
        print (" ".join(row))

trafienia=0
tura=0

print("Oto plansza:\n")
print_board(plansza)
     
for tura in range(10):
    zgadn_wiersz = int(input("\nZgadnij wiersz [1-10]:  "))
    zgadn_kolumna = int(input("Zgadnij kolumnę [1-10]: "))
    strzał=("%d_%d" %(zgadn_wiersz,zgadn_kolumna))

    if (zgadn_wiersz < 1 or zgadn_wiersz > 10)  or (zgadn_kolumna < 1 or zgadn_kolumna > 10):
       print ("\nWykroczyłeś poza planszę")
       print_board(plansza)
    elif(plansza[zgadn_wiersz-1][zgadn_kolumna-1] == "."):
       print ("\nJuż tu próbowałeś. Zmarnowany ruch.")
       print_board(plansza)
    elif(plansza[zgadn_wiersz-1][zgadn_kolumna-1] == "X"):
       print ("\nJuż tu strzeliłeś statek. Zmarnowany ruch.")
       print_board(plansza)

    else:
        for i in range(0,len(punkty)):
         
            if strzał==punkty[i][0]:
                   trafienia=trafienia+1
                   plansza[zgadn_wiersz-1][zgadn_kolumna-1] = "X"
                   break                  
            else:
                   plansza[zgadn_wiersz-1][zgadn_kolumna-1] = "."
                    
        if plansza[zgadn_wiersz-1][zgadn_kolumna-1] == "X"   :
               print("\nTrafione!")
        elif plansza[zgadn_wiersz-1][zgadn_kolumna-1] == ".":
               print("\nPudło!")
        print_board(plansza)
