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

statek_rzad = random_rzad(plansza)
statek_kol = random_kol(plansza)
print ("Jeśli MUSISZ trafić:")
print (statek_rzad, statek_kol)

z_rzad = input("Wybierz rząd: ")
z_kol = input("Wybierz kolumnę: ")
z_rzad=int(z_rzad)
z_kol=int(z_kol)

while z_rzad!=statek_rzad or z_kol!=statek_kol:
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

print("Gratulacje, zatopiłeś statek!")

