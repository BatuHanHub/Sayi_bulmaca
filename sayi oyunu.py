import random 

print ( """Sayı Bulmaca, sürüm 2.0 -sürüm (x86_x64)
Lisans GPLv3+ : GNU GPL sürüm 3 <https://www.gnu.org/licenses/gpl-3.0.html>
telif hakkı (C) 2022 BatuHanHub 
Bu ücretsiz bir yazılımdır; değiştirmekte ve yeniden dağıtmakta özgürsünüz.
Yasaların izin verdiği ölçüde HİÇBİR GARANTİ YOKTUR.""" )

print('''SAYI BULMACA OYUNUNA HOSGELINIZ!
      
      Zorluk seviyeleri;
      
      #############################
      *Kolay mod için "k" yazınız.
      **Normal mod için "n" yazınız.
      ***Zor mod için "z" yazınız.
      #############################
      
      ''')

while True:
        
    koz=str(input(">"))
    
    if koz == "k" or "K":
        koz=random.randint(1,4)
        pass
    
    elif koz == "n" or "N":
        koz=random.randint(1,7)
        pass
        
    elif koz == "z" or "Z":
        koz=random.randint(1,10)
        pass
    
    elif koz != "k" or "K" and "n" or "N" and "z" or "Z":
        print('''HATA: lütfen zorluk seviyenizi yazınız
              
      Zorluk seviyeleri;
      
      #############################
      *Kolay mod için "k" yazınız.
      **Normal mod için "n" yazınız.
      ***Zor mod için "z" yazınız.
      #############################
      
              ''') 
        continue

    break

can = 3

while True: 
    
    tahmin=int(input("bence:"))
    
    if koz == tahmin:
        print("\nTebrikler kazandınız!\n")
        break
        
    elif koz != tahmin:
        can = can - 1
        print("can:", can)
        
        if can == 0:
            print("Kaybettiniz!")
            break
        
        else:
            continue
            
input("oyun bitti.")
