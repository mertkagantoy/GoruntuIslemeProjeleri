import cv2
import numpy as np

# Kamera başlatma
cap = cv2.VideoCapture(0)

while True:
    # Kameradan bir çerçeve al
    _, frame = cap.read()

    # RGB'den HSV'ye dönüştürme
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kırmızı renk aralığını belirleme
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # HSV görüntüsündeki kırmızı renk aralığını maskeleme
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Görüntü ve maskeyi birleştirme
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Sonuçları gösterme
    cv2.imshow('Original', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', result)

    # Çıkış için 'q' tuşuna basma kontrolü
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı kapatma
cap.release()
cv2.destroyAllWindows()
