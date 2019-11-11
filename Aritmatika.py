#\\\\\\\\\\\\\\\\\\\\\\\\\\\   Selasa, 22 Oktober 2019   /////////////////////////////////////////

#TODO mencari jawaban dari soal persamaan linear
# Cara 1 
Jmlhewan = 13
Jmlkaki = 32
kakikambing = 4
kakiayam = 2

ayam = int((((Jmlhewan*kakikambing) - Jmlkaki) / kakiayam))
kambing = Jmlhewan - ayam

print(f'Jadi, jumlah ayam ada {ayam} dan jumlah kambing ada {kambing}')

# Menggunakan input
totalHewan  = int(input('Ketik total hewan : '))
totalKaki   = int(input('Ketik total kaki hewan : '))
kakiAyam    = int(input('Ketik jumlah kaki hewan A : '))
kakiKambing = int(input('Ketik jumlah kaki hewan B : '))

divisor = abs(kakiAyam - kakiKambing)

Kambing = abs((totalKaki - totalHewan*kakiAyam) / divisor)
#print("Kambing:", Kambing)

Ayam = abs((totalKaki - totalHewan*kakiKambing) / divisor)
#print("Ayam:", Ayam)

print(f'hewan A = {int(Ayam)}, hewan B = {int(Kambing)}')


#TODO Mencari jawaban dari soal perbandingan
bedaUmur_anak   = 1/4
beda_anak       = 1/2
bedaUmur_ibu    = 1/7
beda_ibu        = 19

equation_1 = (beda_ibu * bedaUmur_anak) + beda_anak
equation_2 = (bedaUmur_anak - bedaUmur_ibu)
age_ibu    = round(equation_1 / equation_2)

equation_3 = (((bedaUmur_anak / bedaUmur_ibu) * beda_ibu) + ((beda_ibu * bedaUmur_anak) + beda_anak) - beda_ibu)
equation_4 = (bedaUmur_anak / bedaUmur_ibu) - 1
age_anak   = int(equation_3 / equation_4)

melahirkan = age_ibu - age_anak

print(f'Umur ibu {age_ibu}, Umur anak {age_anak}')
print(f'Maka umur ibu saat melahirkan anak adalah {melahirkan}')