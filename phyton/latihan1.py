# Input kecepatan rata-rata robot (dalam cm/detik)
kecepatan_robot = int(input("Masukkan kecepatan robot (cm/detik) [M]: "))

# Input koordinat titik awal dan titik akhir
x1 = int(input("Masukkan koordinat x1 titik awal: "))
y1 = int(input("Masukkan koordinat y1 titik awal: "))
x2 = int(input("Masukkan koordinat x2 titik akhir: "))
y2 = int(input("Masukkan koordinat y2 titik akhir: "))

# Menghitung jarak Manhattan
jarak_manhattan = (x2 - x1) + (y2 - y1)
jarak_total = jarak_manhattan * 1.5

# Menghitung waktu yang diperlukan
waktu_tujuan = abs(jarak_total / kecepatan_robot)

# Menampilkan hasil
print(f"Robot tiba di tujuannya dalam waktu {waktu_tujuan} detik.")
