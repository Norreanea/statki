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
                            kratka = str(randrange(10))+"_"+str(randrange(10))
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

