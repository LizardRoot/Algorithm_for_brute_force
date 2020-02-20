a = 3
b = 0
c = 0
d = 0

a1 = 3
b1 = 3
c1 = 3
d1 = 3

# 3.0.0.0
# 3.3.3.3

# a.b.c.d
# a1.b1.c1.d1

if b < b1:
    for oktet_2 in range(b,b1+1):
        for oktet_3 in range(c,c1+1):
            for oktet_4 in range(d,d1+1):
            	print(str(a) + '.' + str(oktet_2) + '.' + str(oktet_3) + '.' + str(oktet_4))

elif c < c1:
    for oktet_3 in range(c,c1+1):
        for oktet_4 in range(d,d1+1):
            print(str(a) + '.' + str(b) + '.' + str(oktet_3) + '.' + str(oktet_4))

elif d < d1:
	for oktet_4 in range(d,d1+1):
		print(str(a) + '.' + str(b) + '.' + str(c) + '.' + str(oktet_4))

else:
	print('Error')

