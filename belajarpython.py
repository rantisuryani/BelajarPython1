print("===HELLO GENGS :)====")
print("Yuuuk, mari kita belajar fisika")
print("sebelumnya, aku kepo nih sama kamu, isi dulu yuk biodata kamu")

import datetime as dt
hari_ini = dt.date.today()
print(f"Sekarang {hari_ini} nih, fyi aja sih wkwk")
print("Isi yuk tanggal,bulan dan tahun lahir kamu")
nama = (input("Nama \t\t:"))
tanggal = int(input("Tanggal \t:"))
bulan = int(input("Bulan \t\t:"))
tahun = int(input("Tahun \t\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Oke{nama}, jadi kamu lahir pada tanggal {tanggal_lahir}")
print(f"aku jadi tau loh, hari lahir kamu adalah hari {tanggal_lahir:%A}")


umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365

print(f"sekarang kamu umur {umur_tahun} tahun kan, hehe")
print(f"okeeee cusss kita ngitung fisika wkwk")

#belajar fisika nih
# kalkulator Gerak Lurus Beraturan
print(20*"=")
print("KALKULATOR GERAK LURUS BERATURAN")
print(20*"=" + "\n")

#nyariiii kecepatan
print(18*"=")
print(" > Ngitung kecepatan <")
print(18*"=")
print("Definisi kecepatan = jarak yang ditempuh (meter) dalam satuan waktu (detik)" + "\n")

jarak = float(input("masukan besar jarak tempuh = "))
waktu = float(input("masukkan besar waktu tempuh : "))
operator = input("(masukan operator)------ :    ")
if operator == "/":
    hasil = jarak / waktu
    print(f"hasilnya adalah {hasil} m/s")
else:
    print("eitsss, kamu keliru loh") 

#nyariiii jarak
print(18*"=")
print(" > Ngitung Jarak <")
print(18*"=" + "\n")
kecepatan = float(input("masukan besar kecepatan = "))
waktu = float(input("masukkan besar waktu tempuh : "))
operator = input("(masukan operator)------ :    ")
if operator == "*" or operator == "x":
    hasil = kecepatan * waktu
    print(f"hasilnya adalah {hasil} meter")
else:
    print("eitsss, kamu keliru loh") 
    
#nyariiii waktu
print(18*"=")
print(" > Ngitung Waktu <")
print(18*"=" + "\n")
kecepatan = float(input("masukan besar kecepatan = "))
jarak = float(input("masukkan besar jarak tempuh : "))
operator = input("(masukan operator)------ :    ")
if operator == "/":
    hasil = kecepatan / jarak
    print(f"hasilnya adalah {hasil} detik")
else:
    print("eitsss, kamu keliru loh")    


print("\n" + 18*"=")
print("YEAY !! gampang banget yaa fisika wkwkw")
print(18*"=")
    
