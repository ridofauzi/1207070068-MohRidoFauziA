import cv2# Mengimpor modul cv2 (OpenCV) untuk operasi pengolahan citra
import numpy as np# Mengimpor modul numpy untuk operasi matematika pada citra
import matplotlib.pyplot as plt # Mengimpor modul matplotlib untuk visualisasi

# Baca gambar dalam format BGR
img = cv2.imread('dog.jpg')

# Ubah format gambar dari BGR menjadi RGB
dog = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)  # Tampilkan gambar asli dalam format BGR
# Membuat filter: matriks berukuran 5 x 5 dengan nilai semua elemen 1/25
kernel = np.ones((5,5), np.float32) / 25
print(kernel)

# Lakukan proses filtering dengan filter awal
dog_filter = cv2.filter2D(img, -1, kernel)

# Perbesar ukuran hasil plotting jika diperlukan
plt.rcParams["figure.figsize"] = (15,15)

# Plot pertama, gambar asli
plt.subplot(121)
plt.imshow(dog)
plt.title('Original')
plt.xticks([]), plt.yticks([])

# Plot kedua, hasil filter dengan kernel awal
plt.subplot(122)
plt.imshow(dog_filter)
plt.title('Averaging')
plt.xticks([]), plt.yticks([])

# Tampilkan plot
plt.show()

# Blur menggunakan fungsi cv2.blur pada gambar asli
dog_blur = cv2.blur(dog, (5, 5))

# Membuat kernel dengan np.matrix
kernel_new = np.matrix([[1, 1, 1],
                    [1, 2, 1],
                    [1, 1, 1]]) / 25

# Lakukan proses filtering dengan kernel baru pada gambar asli
dog_filter_new = cv2.filter2D(dog, -1, kernel_new)

# Tampilkan gambar awal, hasil filter, hasil blur, dan hasil filter baru secara bersamaan
plt.figure(figsize=(15, 10))

# Gambar awal
plt.subplot(221)
plt.imshow(dog)
plt.title("Original")

# Hasil filter
plt.subplot(222)
plt.imshow(dog_filter)
plt.title("Averaging")

# Hasil blur
plt.subplot(223)
plt.imshow(dog_blur)
plt.title("Gambar Blur")

# Hasil filter baru
plt.subplot(224)
plt.imshow(dog_filter_new)
plt.title("Gambar Filtering Kernel Baru")

plt.tight_layout()
plt.show()
