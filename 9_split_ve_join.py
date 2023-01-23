################ SPLIT ###############
# Belirli bir bölme kriterine göre string' in alt parçalarını listenin elemanları olarak dönüştürebiliriz.

#Boşluğa göre ayırır
####-> Örnek 1
s ="Hello World !"
print(s.split(" "))

####-> Örnek 2 virgüle göre ayırır.
s= "limon,portakal,çilek"
print(s.split(","))

################   JOIN   ##############
#Listenin elemanları arasına belirtilen yapıyı koyup string' e dönüştürür.
# "patern".join("Elemanları kullanılacak liste")
####-> Örnek 3
l= ['limon','portakal','elma']
print(",".join(l))

####-> Örnek 4
l= ['limon','portakal','elma']
print("-".join(l))