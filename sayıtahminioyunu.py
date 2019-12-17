import random
import time
print("Sayı Tahmin Oyununa HoşGeldiniz 1-100 Arasında Bir Sayı Tahmin Ediniz ")
sayi = random.randint(1,100)
tahmin_hakki = 5
while True:
    tahmin = int(input("Tahmininiz: "))
    
    if tahmin == sayi:
        print("Sayı Sorgulanıyor... ")
        time.sleep(1)
        print("Tebrikler! Doğru Bildiniz")
        break
    elif tahmin > sayi:
        print("Sayı Sorgulanıyor... ")
        time.sleep(1)
        tahmin_hakki-=1
        print("Daha Küçük Bir Sayı Giriniz")
        print("Kalan Tahmin Hakkı: ",tahmin_hakki)
    else:
        print("Sayı Sorgulanıyor... ")
        time.sleep(1)
        tahmin_hakki -= 1
        print("Daha Büyük Bir Sayı Giriniz")
        print("Kalan Tahmin Hakkı: ", tahmin_hakki)
    if tahmin_hakki == 0:
        print("Tahmin Hakkınız Bitmiştir")
        print("Bilgisayarın Tahmini: ",sayi)
