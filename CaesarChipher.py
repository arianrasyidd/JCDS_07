#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Rabu, 30 Oktober 2019 ///////////////////////////////

#TODO membuat fungsi Chaesar Chipher
alfabet = 'abcdefghijklmnopqrstuvwxyz'

alfabet_2 = alfabet.split()
indexHuruf = alfabet.index('m')
hasil = alfabet[indexHuruf + 2]

x = input('Masukkan random kata : ')
y = int(input('Masukkan jumlah yg di geser : '))

def caesarChipher(kata):
    hasil = ''
    for huruf in kata.lower():
        if huruf in alfabet:
            indexHuruf = alfabet.index(huruf)
            indexHuruf = indexHuruf + (y%26)
            if indexHuruf >= 26:
                indexHuruf -= 26
                hasil = hasil + alfabet[indexHuruf]
            else:
                hasil = hasil + alfabet[indexHuruf]
        else:
            hasil = hasil + huruf
    return hasil

print(caesarChipher(x))