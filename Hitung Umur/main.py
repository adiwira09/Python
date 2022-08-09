# Aplikasi Sederhana Menghitung Umur
import datetime as dt

# Memasukkan Tanggal Lahir
print("Masukkan Tanggal Lahir Anda")
tanggal = int(input("Tanggal : "))
bulan = int(input("Bulan : "))
tahun = int(input("Tahun : "))
tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal Lahir Anda: {tanggal_lahir}")

# Hari ini
hari_ini = dt.date.today()

#Menghitung Umur dan Format nya
umur = hari_ini - tanggal_lahir
umur_tahun = umur.days // 365
umur_bulan = (umur.days % 365) // 30
umur_hari = ((umur.days % 365) % 30)
print(f"Umur Anda: {umur_tahun} tahun {umur_bulan} bulan {umur_hari} hari")
