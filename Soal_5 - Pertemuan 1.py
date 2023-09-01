"""
Nama: Kafka Ramadityo
Program Studi: Informatika
MatKul: DAA (INF-A)

5. Tentukan algoritma dan pseudocode volume tabung (jari-jari = 3, tinggi = 5)

#Algoritma 

1. Simpan nilai 3.14 dalam variabel pi. 
2. Simpan nilai 3 dalam variabel jari. 
3. Simpan nilai 5 dalam variabel tinggi. 
4. Hitung volume tabung dengan rumus pi * jari^2 * tinggi dan simpan hasilnya dalam variabel volumeTabung. 
5. Tampilkan hasil volume tabung. 

#Pseudocode 

SET pi TO 3.14 
SET jari TO 3 
SET tinggi TO 5 

SET volumeTabung TO pi * (jari^2) * tinggi
DISPLAY "Volume tabung: " + volumeTabung 
"""

pi = 3.14
jari = 3
tinggi = 5

volumeTabung = pi * (jari**2) * tinggi

print("Volume tabung: ", volumeTabung)
