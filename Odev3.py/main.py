import cv2
import numpy as np

# Resmi yükle
resim = cv2.imread("rices.jpg")

# Resmi istenen boyuta yeniden boyutlandır
yeni_genislik = 800
yeni_yukseklik = 600
resim = cv2.resize(resim, (yeni_genislik, yeni_yukseklik))

# Gri tonlamaya dönüştür
gritonlama = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

# Gauss filtresi uygula
bulaniklastirilmis = cv2.GaussianBlur(gritonlama, (5, 5), 0)

# Kenarları algıla
kenarlar = cv2.Canny(bulaniklastirilmis, 50, 150)

# Gürültüyü azalt
kernel = np.ones((5, 5), np.uint8)
genisletilmis_kenarlar = cv2.dilate(kenarlar, kernel, iterations=1)

# Konturları bul
konturlar, _ = cv2.findContours(genisletilmis_kenarlar, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Belirli bir alanın altındaki konturları filtrele
min_kontur_alani = 100  # Belirli bir alanı aşan konturları filtrele
filtrelenmis_konturlar = [kontur for kontur in konturlar if cv2.contourArea(kontur) > min_kontur_alani]
#bu ifade, konturlar listesindeki konturları filtreleyerek, yalnızca belirli bir alanın üzerindeki konturları
# içeren yeni bir liste oluşturur

# Siyah arka plana yüklenen görüntüyü ekleyin
sonuc = np.zeros_like(resim)
#NumPy kütüphanesindeki zeros_like fonksiyonunu kullanarak, resim adlı bir NumPy dizisi ile aynı boyutta ve türde,
# sadece sıfırlardan oluşan bir dizi oluşturur.

# Tespit edilen pirinçleri beyaz olarak, siyah arka plana ekle
cv2.drawContours(sonuc, filtrelenmis_konturlar, -1, (255, 255, 255), thickness=cv2.FILLED)

# Pirinç sayısı
pirinc_sayisi = len(filtrelenmis_konturlar)

print("Pirinç sayısı: {}".format(pirinc_sayisi))

# Sonucu göster
cv2.imshow('Sadece Pirinç', sonuc)
cv2.waitKey(0)
cv2.destroyAllWindows()
