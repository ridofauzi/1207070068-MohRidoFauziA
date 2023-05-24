import matplotlib.pyplot as plt  # Mengimpor modul matplotlib untuk visualisasi
from skimage import data  # Mengimpor modul skimage untuk memanipulasi citra
from skimage.io import imread  # Mengimpor fungsi imread dari modul skimage.io untuk membaca citra
from skimage.color import rgb2gray  # Mengimpor fungsi rgb2gray dari modul skimage.color untuk mengubah citra menjadi skala keabuan
import numpy as np  # Mengimpor modul numpy untuk operasi matematika pada citra
import cv2  # Mengimpor modul cv2 (OpenCV) untuk operasi pengolahan citra

citra1 = cv2.imread("istana.jpg", cv2.IMREAD_GRAYSCALE)  # Membaca citra "istana.jpg" dalam skala keabuan menggunakan OpenCV
print(citra1.shape)  # Menampilkan dimensi citra1

plt.imshow(citra1, cmap='gray')  # Menampilkan citra1 dalam skala keabuan

kernel = np.array([[-1, 0, -1],  # Membuat kernel untuk filter sharpening
                   [0, 4, 0], 
                   [-1, 0, -1]])

citraOutput = cv2.filter2D(citra1, -1, kernel)  # Melakukan operasi filter sharpening pada citra1 dengan kernel yang telah dibuat

fig, axes = plt.subplots(1, 2, figsize=(12, 12))  # Membuat subplot dengan 1 baris dan 2 kolom untuk menampilkan citra input dan output
ax = axes.ravel()

ax[0].imshow(citra1, cmap='gray')  # Menampilkan citra1 dalam skala keabuan pada sumbu x[0]
ax[0].set_title("Citra Input")
ax[1].imshow(citraOutput, cmap='gray')  # Menampilkan citraOutput dalam skala keabuan pada sumbu x[1]
ax[1].set_title("Citra Output")
plt.show()  # Menampilkan plot citra input dan output secara bersamaan
