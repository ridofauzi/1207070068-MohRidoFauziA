import matplotlib.pyplot as plt  # Mengimpor modul matplotlib untuk membuat plot
from skimage import data  # Mengimpor modul data dari skimage untuk mengakses contoh citra
from skimage.io import imread  # Mengimpor fungsi imread dari modul skimage.io untuk membaca citra
from skimage.color import rgb2gray  # Mengimpor fungsi rgb2gray dari modul skimage.color untuk mengubah citra menjadi citra grayscale
import numpy as np  # Mengimpor modul numpy untuk operasi array

citra1 = imread(fname="mobil.tif")  # Membaca citra "mobil.tif" menggunakan fungsi imread dan menyimpannya ke dalam variabel citra1
citra2 = imread(fname="boneka2.tif")  # Membaca citra "boneka2.tif" menggunakan fungsi imread dan menyimpannya ke dalam variabel citra2

print('Shape citra 1 : ', citra1.shape)  # Mencetak bentuk (shape) citra1
print('Shape citra 1 : ', citra2.shape)  # Mencetak bentuk (shape) citra2

fig, axes = plt.subplots(1, 2, figsize=(10, 10))  # Membuat gambar (figure) dan sumbu (axes) dengan 1 baris dan 2 kolom, serta ukuran 10x10
ax = axes.ravel()  # Membentuk sumbu menjadi array 1 dimensi

ax[0].imshow(citra1, cmap='gray')  # Menampilkan citra1 di sumbu pertama dengan colormap gray
ax[0].set_title("Citra 1")  # Memberikan judul pada sumbu pertama
ax[1].imshow(citra2, cmap='gray')  # Menampilkan citra2 di sumbu kedua dengan colormap gray
ax[1].set_title("Citra 2")  # Memberikan judul pada sumbu kedua

copyCitra1 = citra1.copy()  # Membuat salinan dari citra1 dan menyimpannya ke dalam variabel copyCitra1
copyCitra2 = citra2.copy()  # Membuat salinan dari citra2 dan menyimpannya ke dalam variabel copyCitra2

m1, n1 = copyCitra1.shape  # Mendapatkan ukuran citra1 dalam variabel m1 (jumlah baris) dan n1 (jumlah kolom)
output1 = np.empty([m1, n1])  # Membuat array kosong dengan ukuran m1 x n1 dan menyimpannya ke dalam variabel output1

m2, n2 = copyCitra2.shape  # Mendapatkan ukuran citra2 dalam variabel m2 (jumlah baris) dan n2 (jumlah kolom)
output2 = np.empty([m2, n2])  # Membuat array kosong dengan ukuran m2 x n2 dan menyimpannya ke dalam variabel output2

print('Shape copy citra 1 : ', copyCitra1.shape)  # Mencetak bentuk (shape) copyCitra1
print('Shape output citra 1 : ', output1.shape)  # Mencetak bentuk (shape) output1

print('m1 : ', m1)  # Mencetak nilai m1
print('n1 : ', n1)  # Mencetak nilai n1

print()

print('Shape copy citra 2 : ', copyCitra2.shape)  # Mencetak bentuk (shape) copyCitra2
print('Shape output citra 3 : ', output2.shape)  # Mencetak bentuk (shape) output2

print('m2 : ', m2)  # Mencetak nilai m2
print('n2 : ', n2)  # Mencetak nilai n2

print()

for baris in range(0, m1-1):  # Melakukan iterasi untuk setiap baris dalam rentang 0 hingga m1-1 pada citra1
    for kolom in range(0, n1-1):  # Melakukan iterasi untuk setiap kolom dalam rentang 0 hingga n1-1 pada citra1
        a1 = baris  # Mengatur nilai a1 menjadi nilai baris
        b1 = kolom  # Mengatur nilai b1 menjadi nilai kolom
        dataA = [copyCitra1[a1-1, b1-1], copyCitra1[a1-1, b1], copyCitra1[a1-1, b1+1],
                 copyCitra1[a1, b1-1], copyCitra1[a1, b1], copyCitra1[a1, b1+1],
                 copyCitra1[a1+1, b1-1], copyCitra1[a1+1, b1], copyCitra1[a1+1, b1+1]]  # Mendapatkan nilai piksel di sekitar piksel (a1, b1) dalam citra1

        # Urutkan
        for i in range(1, 8):  # Melakukan iterasi untuk i dalam rentang 1 hingga 7
            for j in range(i, 9):  # Melakukan iterasi untuk j dalam rentang i hingga 8
                if dataA[i] > dataA[j]:  # Jika nilai dataA[i] lebih besar dari dataA[j]
                    tmpA = dataA[i]  # Tukar nilai dataA[i] dengan dataA[j]
                    dataA[i] = dataA[j]
                    dataA[j] = tmpA

        output1[a1, b1] = dataA[5]  # Mengisi nilai piksel (a1, b1) pada output1 dengan nilai median dari dataA

for baris in range(0, m2-1):  # Melakukan iterasi untuk setiap baris dalam rentang 0 hingga m2-1 pada citra2
    for kolom in range(0, n2-1):  # Melakukan iterasi untuk setiap kolom dalam rentang 0 hingga n2-1 pada citra2
        a1 = baris  # Mengatur nilai a1 menjadi nilai baris
        b1 = kolom  # Mengatur nilai b1 menjadi nilai kolom
        dataA = [copyCitra2[a1-1, b1-1], copyCitra2[a1-1, b1], copyCitra2[a1-1, b1+1],
                 copyCitra2[a1, b1-1], copyCitra2[a1, b1], copyCitra2[a1, b1+1],
                 copyCitra2[a1+1, b1-1], copyCitra2[a1+1, b1], copyCitra2[a1+1, b1+1]]  # Mendapatkan nilai piksel di sekitar piksel (a1, b1) dalam citra2

        # Urutkan
        for i in range(1, 8):  # Melakukan iterasi untuk i dalam rentang 1 hingga 7
            for j in range(i, 9):  # Melakukan iterasi untuk j dalam rentang i hingga 8
                if dataA[i] > dataA[j]:  # Jika nilai dataA[i] lebih besar dari dataA[j]
                    tmpA = dataA[i]  # Tukar nilai dataA[i] dengan dataA[j]
                    dataA[i] = dataA[j]
                    dataA[j] = tmpA

        output2[a1, b1] = dataA[5]  # Mengisi nilai piksel (a1, b1) pada output2 dengan nilai median dari dataA

fig, axes = plt.subplots(2, 2, figsize=(10, 10))  # Membuat gambar (figure) dan sumbu (axes) dengan 2 baris dan 2 kolom, serta ukuran 10x10
ax = axes.ravel()  # Membentuk sumbu menjadi array 1 dimensi

ax[0].imshow(citra1, cmap='gray')  # Menampilkan citra1 di sumbu pertama dengan colormap gray
ax[0].set_title("Input Citra 1")  # Memberikan judul pada sumbu pertama

ax[1].imshow(citra2, cmap='gray')  # Menampilkan citra2 di sumbu kedua dengan colormap gray
ax[1].set_title("Input Citra 2")  # Memberikan judul pada sumbu kedua

ax[2].imshow(output1, cmap='gray')  # Menampilkan output1 di sumbu ketiga dengan colormap gray
ax[2].set_title("Output Citra 1")  # Memberikan judul pada sumbu ketiga

ax[3].imshow(output2, cmap='gray')  # Menampilkan output2 di sumbu keempat dengan colormap gray
ax[3].set_title("Output Citra 2")  # Memberikan judul pada sumbu keempat

plt.show()  # Menampilkan plot keseluruhan
