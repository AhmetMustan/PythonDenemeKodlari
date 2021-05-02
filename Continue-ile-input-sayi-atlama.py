i=int(input("Değer giriniz:")) #Sayi kaça kadar sıralanacak.
x=0
y=int(input("Atlanacak sayi")) #Hangi sayi atlansın.
for x in range(i): #Döngü x i'ye gelene kadar dönsün.
    x+=1 # X her defasında 1 arttırılsın.
    if x==y: #Eğer x y'ye denk gelirse;
        continue #Bu sayıyı atla ve döngüye devam et.
    print(x) # x i'ye eşit olduğu zaman x in değerini bastır.