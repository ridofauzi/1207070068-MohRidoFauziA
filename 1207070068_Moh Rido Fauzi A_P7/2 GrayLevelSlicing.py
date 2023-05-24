import cv2  # Mengimport library cv2 (OpenCV) untuk operasi pada gambar.
import numpy as np  # Mengimport library numpy untuk operasi pada array dan matriks.
import matplotlib.pyplot as plt# Mengimport library matplotlib.pyplot sebagai plt untuk visualisasi data.

# Membaca gambar dalam mode grayscale
img = cv2.imread('marrio.jpg', cv2.IMREAD_GRAYSCALE)

# Mendapatkan dimensi gambar
row, column = img.shape

# Membuat array kosong dengan ukuran yang sama dengan gambar
img1 = np.zeros((row, column), dtype='uint8')

# Rentang nilai minimum dan maksimum
min_range = 10
max_range = 60

# Melakukan iterasi pada setiap piksel gambar
for i in range(row):
    for j in range(column):
        # Jika nilai piksel berada dalam rentang yang ditentukan, set nilai piksel pada img1 menjadi 255 (putih)
        if min_range <= img[i, j] <= max_range:
            img1[i, j] = 255
        # Jika tidak, set nilai piksel pada img1 menjadi 0 (hitam)
        else:
            img1[i, j] = 0

# Membuat subplot dan menampilkan gambar serta histogram
fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(img, cmap='gray')
ax[0].set_title("Citra Input")
ax[1].hist(img.ravel(), bins=256)
ax[1].set_title('Histogram Input')

ax[2].imshow(img1, cmap='gray')
ax[2].set_title("Citra Output")
ax[3].hist(img1.ravel(), bins=256)
ax[3].set_title('Histogram Output')

# Menampilkan subplot
plt.tight_layout()
plt.show()
