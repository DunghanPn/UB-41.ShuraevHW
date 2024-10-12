# task 1.1
a = int(input())
b = int(input())
c = int(input())
if a <= 3 and a >= 1:
    print(a, 'входит')
if b <= 3 and b >= 1:
    print(b, 'входит')
if c <= 3 and c >= 1:
    print(c, 'входит')
# task 1.2
a = int(input())
if a%11 == 0 and a < 100:
    print('да')
else:
    print('нет')
# task 2.1 var6
a = int(input('a'))
b = int(input('b'))
x = 0
if a < b and b > 4:
    x = a + b
elif a > b:
    x = a - b
else:
    x = a**2
print(x)
#task 2.2 var8
x = int(input('x'))
y = int(input('y'))
B = 0
if x < 2 and y == 2:
    B = x * y + 1
elif x > y:
    B = y**2 + x**2
else:
    B = (x**2) + 2
print(B)
#task 3.1 var6
a = int(input())
if a%7 == 0:
    print('да')
else:
    print('нет')
#task 3.2 var8
a = int(input('Номер месяца '))
if a == 2:
    print('28')
if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
    print('31')
if a == 4 or a == 6 or a == 9 or a == 11:
    print('30')
