import cv2# Mengimpor modul cv2 (OpenCV) untuk operasi pengolahan citra
import numpy as np# Mengimpor modul numpy untuk operasi matematika pada citra
import matplotlib.pyplot as plt# Mengimpor modul matplotlib untuk visualisasi
# Load the image in grayscale
# Memuat citra dalam skala keabuan
img = cv2.imread('bmw.jpg', 0)

# Low pass filtering (Gaussian Blur)
# Operasi low pass filtering menggunakan Gaussian Blur
blur = cv2.GaussianBlur(img, (5, 5), 0)

# High pass filtering (Laplacian)
# Operasi high pass filtering menggunakan Laplacian
laplacian = cv2.Laplacian(img, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))  # Konversi ke tipe data uint8

# Image thresholding
# Operasi thresholding pada citra
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Calculate histogram for each filtered image
# Menghitung histogram untuk setiap citra hasil filtering
hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_blur = cv2.calcHist([blur], [0], None, [256], [0, 256])
hist_laplacian = cv2.calcHist([laplacian], [0], None, [256], [0, 256])
hist_thresh = cv2.calcHist([thresh], [0], None, [256], [0, 256])

# Plotting
# Menampilkan citra-citra hasil filtering dan histogramnya

# Menampilkan citra asli
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.xticks([])
plt.yticks([])

# Menampilkan citra hasil low pass filtering
plt.subplot(2, 2, 2)
plt.imshow(blur, cmap='gray')
plt.title('Low Pass Filtering')
plt.xticks([])
plt.yticks([])

# Menampilkan citra hasil high pass filtering
plt.subplot(2, 2, 3)
plt.imshow(laplacian, cmap='gray')
plt.title('High Pass Filtering')
plt.xticks([])
plt.yticks([])

# Menampilkan citra hasil image thresholding
plt.subplot(2, 2, 4)
plt.imshow(thresh, cmap='gray')
plt.title('Image Thresholding')
plt.xticks([])
plt.yticks([])

# Membuat subplot baru untuk menampilkan histogram

# Menampilkan histogram citra asli
plt.figure()
plt.subplot(2, 2, 1)
plt.bar(range(256), hist_img[:, 0], color='blue')
plt.title('Histogram - Original Image')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# Menampilkan histogram citra hasil low pass filtering
plt.subplot(2, 2, 2)
plt.bar(range(256), hist_blur[:, 0], color='blue')
plt.title('Histogram - Low Pass Filtering')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# Menampilkan histogram citra hasil high pass filtering
plt.subplot(2, 2, 3)
plt.bar(range(256), hist_laplacian[:, 0], color='blue')
plt.title('Histogram - High Pass Filtering')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# Menampilkan histogram citra hasil image thresholding
plt.subplot(2, 2, 4)
plt.bar(range(256), hist_thresh[:, 0], color='blue')
plt.title('Histogram - Image Thresholding')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# Menampilkan plot
plt.tight_layout()
plt.show()
