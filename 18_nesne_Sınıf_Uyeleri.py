"""
- Bir sınıf içerisinde bulunan nitelikler (özellikler), değişkenler, metotlar, fonksiyonlar ve buna benzer başka veri tipleri o sınıfın
üyelerini meydana getirir. 
1) Aleni Üyeler ( Public Members)
2) Gizli Üyeler ( Private Members)
3) Yarı-gizli Üyerler ( Semi-Private Members)

1) Public Members

Eğer bir sınıf üyesi dışarıya açıksa, yani bu üyeye sınıf dışından normal yöntemlerle erişilebiliyorsa bu tür üyelere ‘aleni üyeler’ adı verilir.

2) Private memebers __gizli, __degisken

Dışarıya kapalı olan bu gizli üyelere, normal yöntemleri kullanarak sınıf dışından erişemezsiniz.
Başında çift alt çizgi olan, ancak ucunda herhangi bir çizgi bulunmayan (veya tek bir alt çizgi bulunan) bu gizli öğelere normal yollardan erişemeyiz.
Bir üyenin gizli olabilmesi için başında en az iki adet, ucunda da en fazla bir adet alt çizgi bulunmalıdır. Yani şunlar birer gizli üyedir:

__gizli = 'gizli'
__gizli_ = 'gizli'
__gizli_üye = 'gizli'
__gizli_üye_ = 'gizli'

Gizli üyeler yalnızca sınıf dışına kapalıdır. Bu üyelere sınıf içinden rahatlıkla erişebiliriz

"""