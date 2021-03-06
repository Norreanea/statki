#!/usr/bin/python3

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
                self.wokol_mapy.append(str(wiersz)+"_"+str(kolumna+i))
            else:
                self.wokol_mapy.append(str(wiersz+i)+"_"+str(kolumna))
        for j in self.wokol_mapy:
            ti = int(j.split("_")[0])
            tj = int(j.split("_")[1])
            for ri in range(ti,ti+1):
                for rj in range(tj,tj+1):
                    if ri>=0 and ri<=9 and rj>=0 and rj<=9:
                        if not(str(ri)+"_"+str(rj) in self.mapa_wspolrzednych) and not(str(ri)+"_"+str(rj) in self.wokol_mapy):
                            self.mapa_wspolrzednych.append(str(ri)+"_"+str(rj))
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
