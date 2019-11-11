#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\    Kamis, 24 Oktober 2019    ////////////////////////////////////////////

#TODO Mencari gabungan dan irisan serta operator lainnya dari himpunan set
a = {1, 2, 4, 7, 9, 19}
b = {7, 9, 8, 19, 6, 5, 12, 16, 17}
c = {3, 8, 6, 19}

print(a & b)
print(a & b & c)
print(a & b | c )
print(a - b | c)
print(a ^ b & c)

p = set(range(-4, 5))
q = set(range(-7, 2))
r = set(range(-1, 8))
s = set(range(-9, 11))
print(p|q, p|r, q|r)