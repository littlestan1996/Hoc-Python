# Bai 1
import math
a, b, c = float(input()), float(input()), float(input())
delta = b**2 - 4*a*c
if delta < 0:
    print('Phuong trinh vo nghiem.')
elif delta == 0:
    x = -b / 2*a
    print('Phuong trinh co nghiem kep la: {}'.format(x))
else:
    x1 = (-b + math.sqrt(delta)) / 2*a
    x2 = (-b - math.sqrt(delta)) / 2*a
    print('Phuong trinh co hai nghiem la {} va {}.:'.format(x1, x2))

# Bai 2
import math
n = int(input('Nhap mot so nguyen duong: '))
x = float(input('Nhap mot so thuc bat ky: '))
s1, s2, s3 = 1, 1, 1
if n > 0:
    for i in range(1, n+1):
        s1 += x**i
    print('s1 = {}'.format(s1))
    for i in range(1, n + 1):
        s2 += (-x)**i
    print('s2 = {}'.format(s2))
    for i in range(1, n + 1):
        s3 += (x**i) / math.factorial(i)
    print('s3 = {}'.format(s3))
else:
    print('n phai la mot so nguyen duong.')

# Bai 3
tong_chu_so = 0
while True:
    n = int(input('Hay nhap mot so nguyen duong nho hon 1000: '))
    if 0 < n and n < 1000:
        print('Da dat yeu cau')
        break
    print('Da nhap so am. Hay nhap lai nao!')
while n > 0:
    tong_chu_so += n % 10
    n = int(n/10)
print('Tong cac chu so la: {}'.format(tong_chu_so))

# Bai 4
while True:
    a, b, c = float(input()), float(input()), float(input())
    if a+b > c and a+c > b and b+c > a:
        print('Ba so nay la do dai cua cac canh cua mot tam giac')
        break
    print('Ba so tren khong phai do dai cua cac canh cua mot tam giac')
if a**2+b**2 == c**2 or a**2+c**2 == b**2 or b**2+c**2 == a**2:
    print('Day la tam giac vuong')
else:
    print('Day khong phai tam giac vuong')















