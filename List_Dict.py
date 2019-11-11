#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\  Jumat, 25 Oktober 2019  ////////////////////////////////////

#TODO Menghitung hari yang akan datang dari hari sekarang
#100 hari kedepan
hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
now = 'rabu'; brpHari = 100

iNow = hari.index(now)
sisaHari = brpHari % len(hari)
hariYgDicari = hari[(iNow + sisaHari) % 7]

print(hariYgDicari)

# 100 hari kebelakang
hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
now = 'rabu'; brpHari = -100

iNow = hari.index(now)
sisaHari = brpHari % len(hari)
hariYgDicari = hari[(iNow + sisaHari) % 7]

print(hariYgDicari)


#TODO Membuat translator hari Ing => Ind atau Ing <= Ind
days = {
    'senin': 'monday',
    'selasa': 'tuesday',
    'rabu': 'wednesday',
    'kamis': 'thursday',
    'jumat': 'friday',
    'sabtu': 'saturday',
    'minggu': 'sunday'
}

hari = list(days)
day  = list(days.values())

x = input('Ketik nama hari (ENG/IND) : ')

if x.lower() in hari:
    engHari = day[hari.index(x.lower())]
    print(f'Bhs Inggris {x.upper()} adalah {engHari.upper()}')
elif x.lower() in day:
    idDay = hari[day.index(x.lower())]
    print(f'Bhs Indonesia {x.upper()} adalah {idDay.upper()}')
else:
    print(f'Input \"{x}\" tidak VALID')