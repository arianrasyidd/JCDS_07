#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Rabu, 30 Oktober 2019 ///////////////////////////////

#TODO Membuat fungsi palindrome
#Fungsi Palindrome
def palindrome(kalimat):
    x = ''
    kata = kalimat.split()
    for i in kata:
        z = i[::-1] + ' '
        x += z
    return x


print(palindrome("Hai aku Arian"))

#Fungsi untuk ngecek palindrome
def palindromeChecker(param):
    paramReversed = param[::-1]
    paramLength = len(param)
    count = 0

    for i in range(0, paramLength):
        if param[i] == paramReversed[i]:
            count += 1
        
    if count == paramLength:
        return 'Palindrome'
    else:
        return 'Not Palindrome'


print(palindromeChecker("Hai aku Arian"))
