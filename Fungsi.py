#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\    Senin, 28 Oktober 2019    /////////////////////////////////////////

#TODO Membuat fungsi membedakan angka ganjil genap
# Menggunakan Print
def gangenPrint(x):
    if x % 2 == 0:
        print(x, 'tergolong GENAP')
    else:
        print(x, 'tergolong GANJIL')


gangenPrint(4)

# Menggunakan Return
def gangenReturn(angka):
    if angka % 2 == 0:
        return 'GENAP'
    else:
        return 'GANJIL'


print(gangenReturn(9))


#TODO Membuat fungsi calculator sederhana
a = int(input('masukan angka 1 : '))
x = input('masukan operator aritmatika (+-*/) : ')
b = int(input('masukan angka 2 : '))

def iCalculator(a, b):
    if x == '+':
        print(f'hasil dari {a} {x} {b} adalah {a + b}')
    elif x == '*':
        print(f'hasil dari {a} {x} {b} adalah {a * b}')
    elif x == '/':
        print(f'hasil dari {a} {x} {b} adalah {a / b}')
    elif x == '-':
        print(f'hasil dari {a} {x} {b} adalah {a - b}')
    else:
        print('maaf operator tidak dikenali')


iCalculator(a, b)


#TODO Membuat Fungsi Kuadrat
def kuadrat(angka):
    return angka ** 2

print(kuadrat(7))


#TODO Membuat Fungsi pangkat
def pangkat(a, b):
    z = 1
    for i in range(b):
        z *= a
    return z


print(pangkat(3, 2))


#TODO Latihan logika FizzBuzz
def FizzBuzz(x):
    for i in range(1, x+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
    
FizzBuzz(150)


#TODO Membuat fungsi mengubah semua kata vokal menjadi "O"
# Cara 1
def vocal(kalimat):
    kalimat = kalimat.lower()
    kalimat = kalimat.replace('a', 'o')
    kalimat = kalimat.replace('i', 'o')
    kalimat = kalimat.replace('u', 'o')
    kalimat = kalimat.replace('e', 'o')
    print(kalimat)

vocal('muhammad arian rasyid')

# Cara 2
def ubahVokal(kata):
    output = ''
    for huruf in kata:
        if huruf in 'aiueo':
            output = output + 'o'
        else:
            output += huruf
    return output

print(ubahVokal('Arian'))
print(ubahVokal('kambing'))

#TODO Membuat fungsi untuk membalik kata dalam kalimat
def reversing(kata): 
  emptyString = "" 
  for i in kata: 
    emptyString = i + emptyString
  return emptyString

#TODO Membuat fungsi faktorial
def faktorial(x):
    angka = 1
    for i in range(1, x+1):
        angka *= i
    print(angka)

faktorial(7)


