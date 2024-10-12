
#task 1 var 6


def euclid(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    print(a + b)


chislol = int(input())
chislo2 = int(input())


def nok(a, b):
    (a*b)/euclid(a, b)


print(euclid(chislol, chislo2))
print(nok(chislol, chislo2))
