#Ternary Conditionals 
#Cevap olarak "y" veya "n vereceğiz"
# Ternary Conditionals aslında daha önce yapamadığımız bir şeyi yapabilmemize olanak sağlamayacak. if-else mantığını tek satırda kullanıp döndürülecek,
# sonucu ona göre belirlememizi sağlayacak.


# Diyelim ki belirli bir durumu test edip, x değişkeninin değerini bu testin sonucuna göre belirlemek istiyorum. Soruya cevabım "y" olursa değeri 2'ye, yoksa 0'a eşitleyeceğim.

cevap = input("X in değeri 2 olsun mu? y/n:")
if cevap =="y":
    x=2
else:
    x=0
print(x)

#Ternary Conditionals ile tek satırda bunu yazabiliriz

cevap =input("X in değeri 2 olsun mu? y/n:")
x = 2 if cevap == "y" else 0
print(x)