"""
Nama: Kafka Ramadityo
Program Studi: Informatika
Mata Kuliah: DAA (INF-A)

1. Cari nilai KPK dari 3 dan 4
Tentukan Algoritma dan pseudocode nya
"""

# Algoritma
"""
1. Tentukan dua bilangan yang ingin dicari KPK-nya.
2. Tampilkan kelipatan dari 3 dan 4.
3. Hitung KPK dari kedua bilangan dengan cara mencari kelipatan dari bilangan yang lebih besar
   hingga ditemukan kelipatan yang juga merupakan kelipatan dari bilangan yang lebih kecil.
4. Tampilkan hasil KPK yang merupakan kelipatan pertama yang ditemukan dan juga merupakan
   kelipatan dari bilangan yang lebih kecil.
"""

# pseudocode
"""
Input bilangan1 = 3
Input bilangan2 = 4

FUNCTION kelipatan_3(i)
    FOR each i IN range(1, 40) DO
        IF i MOD 3 IS EQUAL TO 0 THEN
            PRINT i
    END FOR
END FUNCTION

FUNCTION kelipatan_4(i)
    FOR each i IN range(1, 40) DO
        IF i MOD 4 IS EQUAL TO 0 THEN
            PRINT i WITHOUT LINE-BREAK, SEPARATED BY SPACE
    END FOR
END FUNCTION


Output kelipatan_3(bilangan1)
Output kelipatan_4(bilangan2)

FUNCTION kpk(i, j)
    IF i > j THEN
        greater <- i
    ELSE
        greater <- j
    END IF

    WHILE True
        IF greater MOD i IS EQUAL TO 0 AND greater MOD j IS EQUAL TO 0 THEN
            kpk <- greater
            EXIT WHILE
        END IF
        greater <- greater + 1
    END WHILE

    RETURN kpk
END FUNCTION

KPK = pangkat1 * bilangan1
Output "KPK dari", bilangan1, "dan", bilangan2, "adalah", KPK
"""

bilangan1 = 3
bilangan2 = 4

def kelipatan_3(i):
  for i in range(1, 40):
    if i % 3 == 0:
        print(i, end=" ")

def kelipatan_4(i):
  for i in range(1, 40):
    if i % 4 == 0:
        print(i, end=" ")

kelipatan_1 = kelipatan_3(bilangan1)

print("\n")

kelipatan_2 = kelipatan_4(bilangan2)

print("\n")


def kpk(i, j):
    if i > j:
        greater = i
    else:
        greater = j

    while True:
        if greater % i == 0 and greater % j == 0:
            kpk = greater
            break
        greater += 1

    return kpk

kpk = kpk(bilangan1, bilangan2)
print("\nKPK dari", bilangan1, "dan", bilangan2, "adalah", kpk)



