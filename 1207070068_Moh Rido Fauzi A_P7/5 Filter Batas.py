import matplotlib.pyplot as plt  # Mengimpor library matplotlib untuk membuat plot
import cv2  # Mengimpor library OpenCV untuk membaca dan memanipulasi citra
# Mengimpor fungsi untuk mengubah citra menjadi skala keabuan
from skimage.color import rgb2gray
import numpy as np  # Mengimpor library NumPy untuk operasi matriks dan array

# Membaca citra 'istana.jpg' dalam skala keabuan
citra1 = cv2.imread('istana.jpg', cv2.IMREAD_GRAYSCALE)
# Membaca citra 'marrio.jpg' dalam skala keabuan
citra2 = cv2.imread('marrio.jpg', cv2.IMREAD_GRAYSCALE)
print('Shape citra 1 : ', citra1.shape)  # Menampilkan dimensi citra pertama
print('Shape citra 1 : ', citra2.shape)  # Menampilkan dimensi citra kedua

# Membuat subplots dengan 1 baris dan 2 kolom
fig, axes = plt.subplots(1, 2, figsize=(10, 10))
ax = axes.ravel()  # Melakukan ravel (flatten) pada array axes

ax[0].imshow(citra1, cmap='gray')  # Menampilkan citra pertama pada axes[0]
ax[0].set_title("Citra 1")  # Memberikan judul pada subplot citra pertama
ax[1].imshow(citra2, cmap='gray')  # Menampilkan citra kedua pada axes[1]
ax[1].set_title("Citra 2")  # Memberikan judul pada subplot citra kedua

copyCitra1 = citra1.copy()  # Mengcopy citra pertama ke variabel copyCitra1
copyCitra2 = citra2.copy()  # Mengcopy citra kedua ke variabel copyCitra2

# Mendapatkan dimensi citra pertama (jumlah baris dan kolom)
m1, n1 = copyCitra1.shape
# Membuat matriks kosong dengan dimensi yang sama dengan citra pertama
output1 = np.empty([m1, n1])

# Mendapatkan dimensi citra kedua (jumlah baris dan kolom)
m2, n2 = copyCitra2.shape
# Membuat matriks kosong dengan dimensi yang sama dengan citra kedua
output2 = np.empty([m2, n2])

# Menampilkan dimensi copyCitra1
print('Shape copy citra 1:', copyCitra1.shape)
print('Shape output citra 1:', output1.shape)  # Menampilkan dimensi output1
print('m1:', m1)  # Menampilkan jumlah baris citra pertama
print('n1:', n1)  # Menampilkan jumlah kolom citra pertama
print()

# Menampilkan dimensi copyCitra2
print('Shape copy citra 2:', copyCitra2.shape)
print('Shape output citra 2:', output2.shape)  # Menampilkan dimensi output2
print('m2:', m2)  # Menampilkan jumlah baris citra kedua
print('n2:', n2)  # Menampilkan jumlah kolom citra kedua
print()

for baris in range(0, m1-1):  # Melakukan iterasi pada setiap baris citra pertama
    for kolom in range(0, n1-1):  # Melakukan iterasi pada setiap kolom citra pertama
        a1 = baris  # Menginisialisasi variabel a1 dengan nilai baris saat ini
        b1 = kolom  # Menginisialisasi variabel b1 dengan nilai kolom saat ini
        arr = np.array([
            copyCitra1[a1-1, b1-1],
            copyCitra1[a1-1, b1],
            copyCitra1[a1, b1+1],
            copyCitra1[a1, b1-1],
            copyCitra1[a1, b1+1],
            copyCitra1[a1+1, b1-1],
            copyCitra1[a1+1, b1],
            copyCitra1[a1+1, b1+1]
        ])  # Membentuk array dengan nilai piksel di sekitar piksel saat ini
        # Mendapatkan nilai piksel minimum dari array tersebut
        minPiksel = np.amin(arr)
        # Mendapatkan nilai piksel maksimum dari array tersebut
        maksPiksel = np.amax(arr)
        # Jika piksel saat ini kurang dari nilai piksel minimum
        if copyCitra1[baris, kolom] < minPiksel:
            # Assign nilai piksel minimum ke matriks output1
            output1[baris, kolom] = minPiksel
        else:
            # Jika piksel saat ini lebih dari nilai piksel maksimum
            if copyCitra1[baris, kolom] > maksPiksel:
                # Assign nilai piksel maksimum ke matriks output1
                output1[baris, kolom] = maksPiksel
            else:
                # Assign nilai piksel saat ini ke matriks output1
                output1[baris, kolom] = copyCitra1[baris, kolom]

for baris1 in range(0, m2-1):  # Melakukan iterasi pada setiap baris citra kedua
    for kolom1 in range(0, n2-1):  # Melakukan iterasi pada setiap kolom citra kedua
        a1 = baris1  # Menginisialisasi variabel a1 dengan nilai baris saat ini
        b1 = kolom1  # Menginisialisasi variabel b1 dengan nilai kolom saat ini
        arr = np.array([
            copyCitra2[a1-1, b1-1],
            copyCitra2[a1-1, b1],
            copyCitra2[a1, b1+1],
            copyCitra2[a1, b1-1],
            copyCitra2[a1, b1+1],
            copyCitra2[a1+1, b1-1],
            copyCitra2[a1+1, b1],
            copyCitra2[a1+1, b1+1]
        ])  # Membentuk array dengan nilai piksel di sekitar piksel saat ini
        # Mendapatkan nilai piksel minimum dari array tersebut
        minPiksel = np.amin(arr)
        # Mendapatkan nilai piksel maksimum dari array tersebut
        maksPiksel = np.amax(arr)
        # Jika piksel saat ini kurang dari nilai piksel minimum
        if copyCitra2[baris1, kolom1] < minPiksel:
            # Assign nilai piksel minimum ke matriks output2
            output2[baris1, kolom1] = minPiksel
        else:
            # Jika piksel saat ini lebih dari nilai piksel maksimum
            if copyCitra2[baris1, kolom1] > maksPiksel:
                # Assign nilai piksel maksimum ke matriks output2
                output2[baris1, kolom1] = maksPiksel
            else:
                # Assign nilai piksel saat ini ke matriks output2
                output2[baris1, kolom1] = copyCitra2[baris1, kolom1]
# Membuat subplots dengan 2 baris dan 2 kolom
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
ax = axes.ravel()  # Melakukan ravel (flatten) pada array axes

ax[0].imshow(citra1, cmap='gray')  # Menampilkan citra pertama pada axes[0]
ax[0].set_title("Input Citra 1")  # Memberikan judul pada subplot citra pertama

ax[1].imshow(citra2, cmap='gray')  # Menampilkan citra kedua pada axes[1]
ax[1].set_title("Input Citra 2")  # Memberikan judul pada subplot citra kedua

# Menampilkan hasil citra pertama pada axes[2]
ax[2].imshow(output1, cmap='gray')
# Memberikan judul pada subplot hasil citra pertama
ax[2].set_title("Output Citra 1")

# Menampilkan hasil citra kedua pada axes[3]
ax[3].imshow(output2, cmap='gray')
# Memberikan judul pada subplot hasil citra kedua
ax[3].set_title("Output Citra 2")

plt.show()  # Menampilkan plot
