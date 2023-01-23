
#Try - Axcept Komutları
"""try:
    hata verebileceğini bildiğimiz kodlar
except HataAdı:
    hata durumunda yapılacak işlem

ilk_sayı    = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")

try:
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
except ZeroDivisionError:
    print("Bir sayıyı 0'a bölemezsiniz!")

try:
    ...bir takım işler...
except birHata:
    ...hata alınınca yapılacak işlemler...
finally:
    ...hata olsa da olmasa da yapılması gerekenler...
    
"""
# ilk_sayı    = input("ilk sayı: ")
# ikinci_sayı = input("ikinci sayı: ")

# try:
#     sayı1 = int(ilk_sayı)
#     sayı2 = int(ikinci_sayı)
#     print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
# except (ValueError, ZeroDivisionError):
#     print("Bir hata oluştu!")
    
def tamsayiya_cevir():
  girdi = input("Bir ondalik sayi giriniz:")
  #print("Yuvarlama işleminin sonucu : {} ".format(round(float(girdi))))
  try: #Bunu dene olmazsa excepte geç
    girdi = float(girdi)
    print("Yuvarlama işleminin sonucu : {} ".format(round(float(girdi))))
  except:
    print("{} girdisi tamsayiya çevrilemiyor".format(girdi))
tamsayiya_cevir()