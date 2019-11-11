#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\  Jumat, 25 Oktober 2019  ////////////////////////////////////

#TODO Konversi nilai menggunakan if statement
#Case 1
nilai = 40

if nilai > 80:
    print(f'Nilai anda {nilai}, Anda Lulus!')
elif nilai < 40:
    print(f'nilai anda {nilai} tidak lulus!')
else:
    print(f'nilai anda {nilai}, anda remedial')
nilai = 30

#Case 2
nilai = 80

if nilai >= 82:
    print('A')
elif nilai > 72 and nilai  < 81:
    print('B')
elif nilai > 62 and nilai < 71:
    print('C')
elif nilai > 52  and nilai < 61:
    print('D')
else:
    print('E')
