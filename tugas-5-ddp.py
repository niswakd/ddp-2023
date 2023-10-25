spesifikasi = ["namaKendaraan","jenisKendaraan","ccKendaraan","warnaKendaraan","rodaKendaraan"]
spesifikasi.append("hargaKendaraan")
spesifikasi.append("tipeKendaraan")
spesifikasi.insert(2, "merkKendaraan")
print(spesifikasi)

ket = '''Menghitung luas bangun datar.
Berikut merupakan pilihan bangun datar yang bisa dihitung:
1. persegi
2. lingkaran
3. segitiga'''

print(ket)

pilih = input("bangun datar mana yang ingin kamu hitung?")
match pilih:
 case "1":
  sisi = int(input("masukkan sisi"))
  persegi = sisi*sisi
  print("luas persegi", persegi)
 
 case "2":
  jari = int(input("masukkan jari"))
  lingkaran = 3.14*jari*jari
  print("luas lingkaran", lingkaran)

 case "3":
  alas = int(input("masukkan alas"))
  tinggi = int(input("masukkan tinggi"))
  segitiga = 0.5*alas*tinggi
  print("luas segitiga", segitiga)

 case  _:
  print("tidak ada")