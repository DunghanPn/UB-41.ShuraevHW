#task 1 var6
a = int(input())
z = 1
for i in range(a):
    z*=(i+1)
print(z)
#task 2 var8
n = int(input())
for i in range(n):
    for j in range(1, i + 2):
        print(j, end='')
    print()