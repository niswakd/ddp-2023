#profil
def say(nama,alamat,gender,umur,hobi):
    print("Halo! Nama saya",nama)
    print("Tempat tinggal saya di",alamat)
    print("Saya adalah seorang",gender)
    print("Saat ini saya berumur",umur,"tahun")
    print("Saya sangat menyukai",hobi)

say("Niswatun Khasanah Dahtiar","Bogor","Perempuan","19","membaca dan bernyanyi")
print()

#mencari kelulusan
def mencariKelulusan(nilai):
    if nilai < 60:
        print("gagal")
    elif 61 <= nilai <= 70:
        print("baik")
    elif 71 <= nilai <= 80:
        print("sangat baik")
    elif 81 <= nilai <= 100:
        print("istimewa")
    else:
        print("tidak lulus")

mencariKelulusan(80)
print()

def angkaGanjil(ang):
    for i in range(61, ang + 1,2):
        print(i)

angkaGanjil(100)