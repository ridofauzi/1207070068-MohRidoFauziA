import numpy as np  # Mengimport library numpy untuk operasi pada array dan matriks.
import matplotlib.pyplot as plt  # Mengimport library matplotlib.pyplot sebagai plt untuk visualisasi data.
import cv2  # Mengimport library cv2 (OpenCV) untuk operasi pada gambar.

istana = cv2.imread('istana.jpg', cv2.IMREAD_GRAYSCALE)  # Membaca gambar 'istana.jpg' dalam mode grayscale.

image_equalized = cv2.equalizeHist(istana)  # Mengaplikasikan Histogram Equalization (HE) pada citra grayscale.

clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(8, 8))  # Membuat objek CLAHE dengan batasan klip 2 dan ukuran grid 8x8.

image_clahe = clahe.apply(istana)  # Mengaplikasikan CLAHE pada citra grayscale.

min_val = np.min(istana)  # Menghitung nilai minimum dalam citra grayscale.
max_val = np.max(istana)  # Menghitung nilai maksimum dalam citra grayscale.
image_cs = 255 * (istana - min_val) / (max_val - min_val)  # Mengaplikasikan kontras stretching (CS) pada citra grayscale.

copyCamera = istana.copy().astype(float)  # Membuat salinan citra grayscale dan mengubah tipe datanya menjadi float.
output1 = copyCamera * 1.9  # Mengalikan setiap piksel citra dengan konstanta 1.9.

fig, axes = plt.subplots(5, 2, figsize=(20, 20))  # Membuat layout subplot dengan ukuran 5 baris dan 2 kolom.
ax = axes.ravel()  # Meratakan array dari objek subplot.

ax[0].imshow(istana, cmap='gray')  # Menampilkan citra input pada subplot pertama.
ax[0].set_title("Citra Input")  # Memberikan judul pada subplot pertama.
ax[1].hist(istana.ravel(), bins=256)  # Menampilkan histogram citra input pada subplot kedua.
ax[1].set_title('Histogram Input')  # Memberikan judul pada subplot kedua.

ax[2].imshow(image_equalized, cmap='gray')  # Menampilkan citra hasil HE pada subplot ketiga.
ax[2].set_title("Citra Output HE")  # Memberikan judul pada subplot ketiga.
ax[3].hist(image_equalized.ravel(), bins=256)  # Menampilkan histogram citra hasil HE pada subplot keempat.
ax[3].set_title('Histogram Output HE Method')  # Memberikan judul pada subplot keempat.

ax[4].imshow(image_cs, cmap='gray')  # Menampilkan citra hasil CS pada subplot kelima.
ax[4].set_title("Citra Output CS")  # Memberikan judul pada subplot kelima.
ax[5].hist(image_cs.ravel(), bins=256)  # Menampilkan histogram citra hasil CS pada subplot keenam.
ax[5].set_title('Histogram Output CS Method')  # Memberikan judul pada subplot keenam.

ax[6].imshow(image_clahe, cmap='gray')  # Menampilkan citra hasil CLAHE pada subplot ketujuh.
ax[6].set_title("Citra Grayscale CLAHE")  # Memberikan judul pada subplot ketujuh.
ax[7].hist(image_clahe.ravel(), bins=256)  # Menampilkan histogram citra hasil CLAHE pada subplot kedelapan.
ax[7].set_title('Histogram Output CLAHE Method')  # Memberikan judul pada subplot kedelapan.

ax[8].imshow(output1, cmap='gray')  # Menampilkan citra hasil perkalian konstanta pada subplot kesembilan.
ax[8].set_title("Citra Grayscale Perkalian Konstanta")  # Memberikan judul pada subplot kesembilan.
ax[9].hist(output1.ravel(), bins=256)  # Menampilkan histogram citra hasil perkalian konstanta pada subplot kesepuluh.
ax[9].set_title('Histogram Output Perkalian Konstanta Method')  # Memberikan judul pada subplot kesepuluh.

fig.tight_layout()  # Mengatur tata letak subplot agar rapi.

plt.show()  # Menampilkan plot ke layar.
