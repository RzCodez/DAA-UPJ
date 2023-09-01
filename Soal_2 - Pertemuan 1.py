"""
Nama: Kafka Ramadityo
Program Studi: Informatika
Mata Kuliah: DAA (INF-A)

2. Fungsi untuk menukar posisi dua variabel x dan y, dengan kasus : 
Ada 2 buah: manggis dan pisang. Manggis di piring 1, Pisang di piring 2. Piring 3 kosong.

#Algortima 

1. Inisialisasi variabel piring_1 dengan nilai "Manggis". 
2. Inisialisasi variabel piring_2 dengan nilai "Pisang". 
3. Inisialisasi variabel piring_3 dengan None. 
4. Ubah nilai variabel piring_3 menjadi nilai dari piring_1. 
5. Ubah nilai variabel piring_1 menjadi nilai dari piring_2. 
6. Ubah nilai variabel piring_2 menjadi nilai dari piring_3. 
7. Cetak piring_1. 
8. Cetak piring_2. 

#Pseudocode 

DECLARE piring_1 AS String 
DECLARE piring_2 AS String 
DECLARE piring_3 AS String 

SET piring_1 TO "Manggis" 
SET piring_2 TO "Pisang" 
SET piring_3 TO None 

SET piring_3 TO piring_1 
SET piring_1 TO piring_2 
SET piring_2 TO piring_3 

DISPLAY "piring 1 berisikan: " + piring_1 
DISPLAY "piring 2 berisikan: " + piring_2 
"""

piring_1 = "Manggis"
piring_2 = "Pisang"
piring_3 = None

temp = piring_1
piring_1 = piring_2
piring_2 = temp

print("piring 1 berisikan: ", piring_1)
print("piring 2 berisikan: ", piring_2)
print("piring 3 berisikan: ", piring_3)

