#Pilihan
print("Pilih :")
print("1. Celcius")
print("2. Reamour")
print("3. Fahrenheit")
print("4. Kelvin")
pilihan = input("Masukkan Pilihan : ")

#CELCIUS TO R/F/K
if pilihan == "1":
 print("1. C to R")
 print("2. C to F")
 print("3. C to K")
 pilihan_c = input("Masukkan Pilihan : ")
 
 if pilihan_c == '1':
  suhu_c = float(input("Masukkan Suhu dalam Celcius : "))
  c_r = 4/5*suhu_c
  print("Suhu Dalam Reamour :", c_r, "R")
 elif pilihan_c == '2':
  suhu_c = float(input("Masukkan Suhu dalam Celcius : "))
  c_k = suhu_c+273
  print("Suhu Dalam Kelvin :", c_k, "K")
 elif pilihan_c == '3':
  suhu_c = float(input("Masukkan Suhu dalam Celcius : "))
  c_f = 9/5*suhu_c + 32
  print("Suhu Dalam Fahrenheit :", c_f, "F")
  
#REAMOUR TO C/F/K
elif pilihan == "2":
 print("1. R to C")
 print("2. R to F")
 print("3. R to K")
 pilihan_r = input("Masukkan Pilihan : ")
 
 if pilihan_r == '1':
  suhu_r = float(input("Masukkan Suhu dalam Reamour : "))
  r_c = 5/4*suhu_r
  print("Suhu Dalam Celcius :", r_c, "C")
  
 elif pilihan_r == '2':
  suhu_r = float(input("Masukkan Suhu dalam Reamour : "))
  r_f = 9/4*suhu_r+32
  print("Suhu Dalam Kelvin :", r_f, "K")
  
 elif pilihan_r == '3':
  suhu_r = float(input("Masukkan Suhu dalam Reamour : "))
  r_k = 5/4*suhu_r+273
  print("Suhu Dalam Fahrenheit :", r_k, "F")

#FAHRENHEIT TO R/C/K
elif pilihan == "3":
 print("1. F to C")
 print("2. F to R")
 print("3. F to K")
 pilihan_f = input("Masukkan Pilihan : ")
 
 if pilihan_f == '1':
  suhu_f = float(input("Masukkan Suhu dalam Fahrenheit : "))
  f_r = 4/9*(suhu_f-32)
  print("Suhu Dalam Reamour :", f_r, "R")
  
 elif pilihan_f == '2':
  suhu_f = float(input("Masukkan Suhu dalam Fahrenheit : "))
  f_c = 5/9*(suhu_f-32)
  print("Suhu Dalam Celcius :", f_c, "C")
  
 elif pilihan_f == '3':
  suhu_f = float(input("Masukkan Suhu dalam Fahrenheit : "))
  f_c = 5/9*(suhu_f-32)
  c_k = f_c + 273
  print("Suhu Dalam Kelvin :", c_k, "K")
  
#KELVIN TO R/F/C
elif pilihan == "4":
 print("1. K to C")
 print("2. K to F")
 print("3. K to R")
 pilihan_k = input("Masukkan Pilihan : ")
 
 if pilihan_k == '1':
  suhu_k = float(input("Masukkan Suhu dalam Kelvin : "))
  k_c = suhu_k-273
  print("Suhu Dalam Celcius :", k_c, "C")
  
 elif pilihan_k == '2':
  suhu_k = float(input("Masukkan Suhu dalam Kelvin : "))
  k_r = 4/5*(suhu_k-273)
  print("Suhu Dalam Reamour :", k_r, "R")
  
 elif pilihan_k == '3':
  suhu_k = float(input("Masukkan Suhu dalam Kelvin : "))
  k_c = suhu_k-273
  k_f = (9/5*k_c) + 32
  print("Suhu Dalam Fahrenheit :", k_f, "F")
