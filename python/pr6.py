#var 6 task 1
n = int(input('длина массива '))
x = []
s = str('')
f = 0
g = 0
for i in range(n):
    print('Введите ', i + 1, ' элемент')
    x.append(int(input()))
a = max(x)
for z in range(n):
    if x[z] != a:
        f+=1
    elif x[z] == a:
        g+=1
print(f, ' меньше максимального, ', g, ' равных максимальному' )
#var 6 task 2
n = int(input('длина массива '))
x = []
s = str('')
g = 0
for i in range(n):
    print('Введите ', i + 1, ' элемент')
    x.append(int(input()))
for z in range(n):
    if x[z] > 5:
        g += x[z]
print(g)