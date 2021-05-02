x=int(input("Lutfen Vize notunuzu giriniz ve Enter tuşuna basınız:"))
y=int(input("Lutfen Final Notunuzu giriniz ve Enter tuşuna basınız:"))
x= x*0.4
y=y*0.6
ort=x+y
print("ortalamanız:",ort)
if ort>=90:
    print('Harf Notunuz "AA"')
elif (ort>=85) and (ort<90):
    print('Harf Notunuz"BA"')
elif (ort<85) and (ort>=75):
    print('Harf Notunuz "BB"')
elif (ort<75) and (ort>=60):
    print('Harf Notunuz "CB"')
elif (ort<60) and (ort>=50):
    print('Harf Notunuz "CC"')
elif (ort<50) and (ort>=45):
    print('Harf Notunuz "DC"')
elif (ort<45) and (ort>=40):
    print('Harf Notunuz "DD"')
else:
    print('Harf Notunuz "FF"')
print("Programınız sona ulaştı.")
