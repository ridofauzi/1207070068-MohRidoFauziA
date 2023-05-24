# Highpass Filter
import cv2  # Mengimpor modul cv2 (OpenCV) untuk operasi pengolahan citra
import numpy as np  # Mengimpor modul numpy untuk operasi matematika pada citra
import matplotlib.pyplot as plt  # Mengimpor modul matplotlib untuk visualisasi

# Memanggil citra sebagai grayscale (argument 0)
img = cv2.imread('minion.jpg', 0)  # Membaca citra 'minion.jpg' dalam mode grayscale

# Menerapkan algoritma high-pass filtering:
# Laplacian
laplacian = cv2.Laplacian(img, cv2.CV_64F)  # Menggunakan operator Laplacian untuk high-pass filtering

# Sobel dengan ukuran kernel 5
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=7)  # Menggunakan operator Sobel pada sumbu X dengan kernel size 7
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=7)  # Menggunakan operator Sobel pada sumbu Y dengan kernel size 7

# Perbesar ukuran hasil plotting
plt.rcParams["figure.figsize"] = (20, 20)

# Menampilkan citra asli
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original')  # Judul plot
plt.xticks([])  # Menghilangkan sumbu x
plt.yticks([])  # Menghilangkan sumbu y

# Menampilkan hasil Laplacian
plt.subplot(2, 2, 2)
plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian')  # Judul plot
plt.xticks([])  # Menghilangkan sumbu x
plt.yticks([])  # Menghilangkan sumbu y

# Menampilkan hasil Sobel X
plt.subplot(2, 2, 3)
plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X')  # Judul plot
plt.xticks([])  # Menghilangkan sumbu x
plt.yticks([])  # Menghilangkan sumbu y

# Menampilkan hasil Sobel Y
plt.subplot(2, 2, 4)
plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y')  # Judul plot
plt.xticks([])  # Menghilangkan sumbu x
plt.yticks([])  # Menghilangkan sumbu y

# Menampilkan plot
plt.show()

# Membaca citra sebagai grayscale (argument 0)
img = cv2.imread('minion.jpg',0)

# Memanggil fungsi Canny Edges dengan argument (citra, nilai_min, nilai_max)
edges = cv2.Canny(img,100,200)

# Menampilkan citra asli
plt.subplot(121)
plt.imshow(img,cmap = 'gray')
plt.title('Original Image')  # Judul plot
plt.xticks([])  # Menghilangkan sumbu x
plt.yticks([])  # Menghilangkan sumbu y

# Menampilkan citra hasil Canny Edges
plt.subplot(122)
plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image')  # Judul plot
plt.xticks([])  # Menghilangkan sumbu x
plt.yticks([])  # Menghilangkan sumbu y

# Menampilkan plot
plt.show()

# Image Thresholding
img = cv2.imread('luffy.jpg',0)

# Hitungan threshold.
# Perhatikan nilai ambang batas bawah dan atas dari tiap fungsi yang diberikan
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

# Menampilkan hasil
titles = ['Gambar asli','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

# Menampilkan beberapa gambar sekaligus
for i in range(6):
    # 3 baris, 2 kolom
    plt.subplot(3,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])  # Judul plot
    plt.xticks([])  # Menghilangkan sumbu x
    plt.yticks([])  # Menghilangkan sumbu y
plt.show()

img = cv2.medianBlur(img,5)

# Melakukan Thresholding
# Binary Threshold
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# Adaptive Threshold dengan Mean
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)

# Adaptive Threshold dengan Gaussian
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

# Menampilkan hasil
titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

# Menampilkan hasil
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])  # Judul plot
    plt.xticks([])  # Menghilangkan sumbu x
    plt.yticks([])  # Menghilangkan sumbu y
plt.show()

plt.imshow(img)  # Tampilkan gambar asli
