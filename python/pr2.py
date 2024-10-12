import math
# первое задание
x = 16.55*(10**(-3))
y = (-2.75)
z = 0.15
s = math.sqrt(10*((x**(1/3))+x**(y+2)))*((math.asin(z)**2)-abs(x-y))
print(s)
# второе задание
x = -2.235*(10**(-2))
y = 2.23
z = 15.221
s = ((math.exp(abs(x-y))*(abs(x-y)**(x+y)))/(math.atan(x)+math.atan(z)))+((x**6)+(math.log(y)**2))
print(s)
