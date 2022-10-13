#yazarlar : BatuHanHub
#yardımın için teşekkürler gizli kahraman O7

import random 

kolay_mod = 4
normal_mod = 7
zor_mod = 10

print('''SAYI BULMACA OYUNUNA HOSGELINIZ!
      
      Zorluk seviyeleri;
      
      #############################
      *Kolay mod için "k" yazınız.
      **Normal mod için "n" yazınız.
      ***Zor mod için "z" yazınız.
      #############################
      
      ''')

while True:
        
    koz=str(input(">>>"))
    
    if koz == ("k" or "K"):
        koz = kolay_mod
        break
    
    elif koz == ("n" or "N"):
        koz = normal_mod
        pass
        
    elif koz == ("z" or "Z"):
        koz = zor_mod
        pass
    
    elif koz != ("k" , "K" , "n" , "N" , "z" , "Z") :
        print('''HATA: lütfen zorluk seviyenizi yazınız
              
      Zorluk seviyeleri;
      
      #############################
      *Kolay mod için "k" yazınız.
      **Orta mod için "o" yazınız.
      ***Zor mod için "z" yazınız.
      #############################
      
              ''') 
        continue
    
    break
    
while True:
    
    sayı = random.randint(1,koz)
    
    tahmin=int(input("bence:"))
    
    if sayı == tahmin:
        print("\nTebrikler kazandınız!\n")
        pass
        
    elif sayı != tahmin:
        print("\nbulamadın\n")
        continue
    
    break
    


input("çıkmak için bir tuşa basınız...")
     