import matplotlib.pyplot as plt # Mengimpor modul pyplot dari library matplotlib
import cv2 # Mengimpor library opencv
import numpy as np # Mengimpor library numpy

# Membaca citra 'istana.jpg' dalam skala keabuan
citra1 = cv2.imread("istana.jpg", cv2.IMREAD_GRAYSCALE)

# Membaca citra 'marrio.jpg' dalam skala keabuan
citra2 = cv2.imread("marrio.jpg", cv2.IMREAD_GRAYSCALE)

# Menampilkan dimensi citra 1 dan citra 2
print('Shape citra 1:', citra1.shape)
print('Shape citra 2:', citra2.shape)

# Menampilkan kedua citra dalam satu figure menggunakan subplots
fig, axes = plt.subplots(1, 2, figsize=(10, 10))
ax = axes.ravel()

ax[0].imshow(citra1, cmap='gray') # Menampilkan citra pertama
ax[0].set_title("Citra 1") # Judul citra pertama
ax[1].imshow(citra2, cmap='gray') # Menampilkan citra kedua
ax[1].set_title("Citra 2") # Judul citra kedua

copyCitra1 = citra1.copy().astype(float) # Membuat salinan citra pertama dan mengonversinya menjadi tipe float
copyCitra2 = citra2.copy().astype(float) # Membuat salinan citra kedua dan mengonversinya menjadi tipe float

# Mendapatkan dimensi citra salinan pertama dan kedua
m1, n1 = copyCitra1.shape
output1 = np.empty((m1, n1), dtype=float)

m2, n2 = copyCitra2.shape
output2 = np.empty((m2, n2), dtype=float)

# Menampilkan dimensi copy citra 1 dan output citra 1
print('Shape copy citra 1:', copyCitra1.shape)
print('Shape output citra 1:', output1.shape)
print('m1:', m1)
print('n1:', n1)
print()

# Menampilkan dimensi copy citra 2 dan output citra 2
print('Shape copy citra 2:', copyCitra2.shape)
print('Shape output citra 2:', output2.shape)
print('m2:', m2)
print('n2:', n2)
print()

# Menggunakan filter rata-rata pada citra salinan pertama
for baris in range(0, m1-1):
    for kolom in range(0, n1-1):
        a1 = baris
        b1 = kolom
        jumlah = copyCitra1[a1-1, b1-1] + copyCitra1[a1-1, b1] + copyCitra1[a1-1, b1-1] + \
                 copyCitra1[a1, b1-1] + copyCitra1[a1, b1] + copyCitra1[a1, b1+1] + \
                 copyCitra1[a1+1, b1-1] + copyCitra1[a1+1, b1] + copyCitra1[a1+1, b1+1]
        output1[a1, b1] = (1/9 * jumlah)

# Menggunakan filter rata-rata pada citra salinan kedua
for baris1 in range(0, m2-1):
    for kolom1 in range(0, n2-1):
        a1 = baris1
        b1 = kolom1
        jumlah = copyCitra2[a1-1, b1-1] + copyCitra2[a1-1, b1] + copyCitra2[a1-1, b1-1] + \
                 copyCitra2[a1, b1-1] + copyCitra2[a1, b1] + copyCitra2[a1, b1+1] + \
                 copyCitra2[a1+1, b1-1] + copyCitra2[a1+1, b1] + copyCitra2[a1+1, b1+1]
        output2[a1, b1] = (1/9 * jumlah)

# Menampilkan citra input pertama, citra input kedua, citra output pertama, dan citra output kedua
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
ax = axes.ravel()

ax[0].imshow(citra1, cmap='gray')
ax[0].set_title("Input Citra 1")

ax[1].imshow(citra2, cmap='gray')
ax[1].set_title("Input Citra 2")

ax[2].imshow(output1, cmap='gray')
ax[2].set_title("Output Citra 1")

ax[3].imshow(output2, cmap='gray')
ax[3].set_title("Output Citra 2")

plt.show()