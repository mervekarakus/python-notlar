### BREAK - CONTINUE ###
###                  ###
###                  ###
########################  

#Bir şart sağlandığında, durum gerçekleştiğinde döngüden aniden çıkmak isteniyorsa BREAK kullanılır.
#Örnek 1 - break komutunu gördüğü anda döngüden çıkar yani 4 e kadar yazdırır.
for i in range(10):
    if i ==5:
        break
    print(i)

#Örnek 2 
x = 0
while x< 10:
    x += 1
    if x == 5:
        break
    print(x)

# Bazen döngülerde bir şart sağlandığında bir sonraki iterasyonda devam etmek isteyebilirim. Bunu CONTINUE ile sağlayabiliriz.
# CONTINUE ile karşılaşıldığı zaman, döngünün bir sonraki iterasyonuna geçilir.
# Örnek -3 3 ü bastırmaz, 4 ü bastırarak devamm eder.
for i in range(10):
    if i ==3:
        print("hey")
        continue
    print(i)

#Örnek 4 -- 0 1 2 yazdırdıktan sonra soznsuz döngüye girer
i=0
while(i<10):
    if(i==3 or i==5):
      continue
    print("i: ",i)
    i=i+1