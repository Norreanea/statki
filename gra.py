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


import random

plansza = []

for x in range(0,10):
  plansza.append(["O"] * 10)

def print_plansza(plansza):
  for rzad in plansza:
    print (" ".join(rzad))

print ("Statki - komunikacja z graczem")
print ("Program przedstawia reakcje na strzały oddawane przez gracza. W tym celu tworzona jest przykładowa plansza z 1 statkiem. Gra toczy się do momentu zatopienia statku.")
print ("Rzędy ponumerowane są od 0 do 9")
print_plansza(plansza)

def random_rzad(plansza):
  return random.randint(0,len(plansza)-1)

def random_kol(plansza):
  return random.randint(0,len(plansza[0])-1)

#statek_rzad = random_rzad(plansza)
#statek_kol = random_kol(plansza)
#print ("Jeśli MUSISZ trafić:")
#print (statek_rzad, statek_kol)

z_rzad = input("Wybierz rząd: ")
z_kol = input("Wybierz kolumnę: ")
z_rzad=int(z_rzad)
z_kol=int(z_kol)
kordy=str(z_rzad)+"_"+str(z_kol)
#print (kordy)
trafione=[]
while len(trafione)+1<20:
  print(len(trafione))
  while kordy not in statki_kratki:
    if (z_rzad < 0 or z_rzad > 9) or (z_kol < 0 or z_kol > 9):
        print ("Wybrałeś miejsce spoza zakresu")
    elif(plansza[z_rzad][z_kol] == "X"):
        print ("Tu już próbowałeś")
    else:
        print ("Nie trafiłeś")
        plansza[z_rzad][z_kol] = "X"
    print_plansza(plansza)
    z_rzad = input("Wybierz rząd: ")
    z_kol = input("Wybierz kolumnę: ")
    z_rzad=int(z_rzad)
    z_kol=int(z_kol)
    kordy=str(z_rzad)+"_"+str(z_kol)
  if kordy in statki_kratki:
    if kordy in trafione:
      print ("Tu już zatopiłeś!")
      print_plansza(plansza)
      z_rzad = input("Wybierz rząd: ")
      z_kol = input("Wybierz kolumnę: ")
      z_rzad=int(z_rzad)
      z_kol=int(z_kol)
      kordy=str(z_rzad)+"_"+str(z_kol)
    else:
      print("Trafiony-zatopiony!")
      trafione.append(kordy)
      print (trafione)
      plansza[z_rzad][z_kol]="X"
      print_plansza(plansza)
      z_rzad = input("Wybierz rząd: ")
      z_kol = input("Wybierz kolumnę: ")
      z_rzad=int(z_rzad)
      z_kol=int(z_kol)
      kordy=str(z_rzad)+"_"+str(z_kol)    

print("Gratulacje, wygrałeś")

