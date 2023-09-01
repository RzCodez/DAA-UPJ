"""
Nama: Kafka Ramadityo
Program Studi: Informatika
MatKul: DAA (INF-A)


6. Tentukan algoritma dan pseudocode volume kerucut
(diameter = 5, tinggi = 4) 

#Algoritma 

1. Input nilai diameter sebagai panjang diameter kerucut. 
2. Hitung jari-jari dengan membagi diameter oleh 2. 
3. Input nilai tinggi kerucut. 
4. Tetapkan nilai pi menjadi 3.14. 
5. Hitung volume kerucut menggunakan rumus: 1/3 * pi * (jari-jari ** 2) * tinggi. 
6. Tampilkan hasil volume kerucut. 

#Pseudocode 

SET diameter TO 5 
SET jariJari TO diameter / 2 
SET tinggi TO 4 
SET pi TO 3.14 
SET volumeKerucut TO 1/3 * pi * (jariJari ^ 2) * tinggi 

DISPLAY "Volume kerucut: " + volumeKerucut 
"""

diameter = 5
jariJari = diameter / 2
tinggi = 4
pi = 3.14

volumeKerucut = 1/3 * pi * (jariJari ** 2) * tinggi

print("Volume kerucut: ", volumeKerucut)
