import cv2
import matplotlib.pyplot as plt
import numpy as np


def calculate_histogram(image):
    # Görüntünün genişliği ve yüksekliği alınıyor
    w, h = image.shape

    # Histogramı tutmak için 256 elemanlı bir dizi oluşturuluyor
    hist = [0] * 256

    # Her pikselin değerine göre histogram hesaplanıyor
    for v in range(h):
        for u in range(w):
            pixel_value = image[u, v]
            hist[pixel_value] += 1

    return hist


# Görüntüyü dosyadan okuma
image_path = "image.png"  # Gerçek dosya yoluyla değiştirin
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#IMREAD_GRAYSCALE :Bu, görüntünün gri tonlu olarak okunmasını sağlar. Eğer bu parametre verilmezse, görüntü renkli olarak okunur.

# Görüntü okunamazsa, uygun bir hata mesajı gösterilebilir
if image is None:
    print("Görüntü okunamadı. Lütfen dosya yolunu kontrol edin.")
else:
    # Histogramı hesapla
    histogram = calculate_histogram(image)
    print("Histogram:", histogram)

    # Histogram grafiğini çiz
    plt.bar(range(256), histogram, color='gray')
    plt.title('Histogram')
    plt.xlabel('Piksel Değeri')
    plt.ylabel('Frekans')
    plt.show()
