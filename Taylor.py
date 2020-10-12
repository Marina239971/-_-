from math import cos, factorial, radians
x = radians(float(input("Enter the angle value: ")))
cosinus = sum(pow(-1, i) * pow(x, 2 * i) / factorial(2 * i) for i in range(n))
print("cosinus:\t%s" % cosinus)
print("math.cos:\t%s" % cos(x))
