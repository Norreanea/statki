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
