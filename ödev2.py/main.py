import cv2
import numpy as np

# Kamera başlatma
kamera = cv2.VideoCapture(0)

while True:
    # Kameradan bir çerçeve al
    _, kare = kamera.read()

    # RGB'den HSV'ye dönüştürme
    hsv = cv2.cvtColor(kare, cv2.COLOR_BGR2HSV)

    # Kırmızı renk aralığını belirleme (Alt ve üst sınırlar)
    alt_kirmizi = np.array([0, 100, 100])
    ust_kirmizi = np.array([10, 255, 255])

    # HSV görüntüsündeki kırmızı renk aralığını maskeleme
    maske = cv2.inRange(hsv, alt_kirmizi, ust_kirmizi)

    # Görüntü ve maskeyi birleştirme (Kırmızı renge odaklanma)
    sonuc = cv2.bitwise_and(kare, kare, mask=maske)

    # Orijinal görüntüyü gösterme
    cv2.imshow('Orijinal', kare)

    # Kırmızı renge odaklanmış sonuç görüntüsünü gösterme
    cv2.imshow('Sonuç', sonuc)

    # Çıkış için 'q' tuşuna basma kontrolü
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı kapatma
kamera.release()
cv2.destroyAllWindows()
