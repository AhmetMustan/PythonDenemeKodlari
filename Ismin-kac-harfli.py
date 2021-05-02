isim=input("İsminizi giriniz:") #Dışarıdan isim allıyoruz fakat burada iki isimli olursa boşluğu karakter sayıyor.

x=int(input("isminizin Kaçıncı harfini görmek istersiniz:")) #İsmimizin kaçıncı harfini görmek istiyoruz?

print("İsminizin harf sayısı:",len(isim)) #İsmimizin kaç harfli olduğunu bastırıyor.

if x<=0: #Eğer 0'a eşit olursa veya negatif bir değer olursa ;
    print("Lutfen pozitif bir değer giriniz.") #Yazacak. Çünkü "[]"" negatif değerlerde sondan saymaya başlıyor.
    
elif x>len(isim): #Eğer ismin içindeki harf sayısından fazla bir değer girilirse;
    print("İsminizin içinde bu kadar fazla harf yoktur.") #Bu çıktıyı üret
    
else: #Normal bir istek olursa;
    print("İsminizin",x,".","harfi:",isim[x-1]) #Çıktıyı üret.
 