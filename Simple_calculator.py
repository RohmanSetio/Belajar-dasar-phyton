print ("Kalkulator sederhana")
print ("....................")

print ("1.Penambahan")
print ("2.Pengurangan")
print ("3.Perkalian")
print ("4.Pembagian")

print ("....................")

def Penjumlahan(x,y):
    return x+y
    
def Pengurangan(a,z):
    return a-z

def Perkalian(k,l):
    return k*l
    
def Pembagian(m,n):
    return m/n
    
angka1 = int(input("masukan angka"))
angka2 = int(input("masukan angka"))

print("Jawaban Penjumlahannya adalah:", Penjumlahan (angka1,angka2))
print("Jawaban Pengurangannya adalah:", Pengurangan (angka1,angka2))
print("Jawaban Perkaliannya adalah:", Perkalian (angka1,angka2))
print("Jawaban Pembagiannya adalah:", Pembagian (angka1,angka2))