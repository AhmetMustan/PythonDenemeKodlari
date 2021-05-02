i=int(input("Değer giriniz:")) #Aslında çok önemi olmasa bile döngünün kaç kez döneceğini belirliyor.
x=int(input("Geldiği anda durdurulacak sayı:")) #Döngü hangi sayıya geldiğinde dursun istiyorsak o değeri veriyoruz.
y=0 #Döngü devam etsin
for y in range(i): # y i'ye gelene kadar döngü dönecek.
    y+=1 # y değeri her seferinde 1 artacak.
    if x==y: # Eğer y değeri x e eşit olursa;
        break #Döngüyü durdur.
    print(y) # y değerini yazdır.