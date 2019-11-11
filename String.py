#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\  Senin, 21 Oktober 2019  /////////////////////////////////////////

#TODO mencari jumlah huruf tertentu tanpa menggunakan fungsi count
kalimat = 'Hari ini Hari tidak masuk sekolah'
cari = 'a'
x = kalimat.upper().replace(cari.upper(), '')
print(x)
JmlCari = len(kalimat) - len(x)
print(f"Jumlah huruf '{cari}' ada = {JmlCari}")


#TODO mencari Jumlah kata 'hari' tanpa menggunakan fungsi 
kalimat = 'Hari ini Hari tidak masuk sekolah'
cari = 'tidak'
x = kalimat.lower(). replace(cari.lower(), '')
jmlCari = int((len(kalimat) - len(x)) / len(cari))
print(len(kalimat))
print(len(x))
print(f'Jumlah kata \'{cari}\' ada = {jmlCari}')