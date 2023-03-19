import math

A = float(input("Ingrese el valor de A: "))
B = float(input("Ingrese el valor de B: "))
C = float(input("Ingrese el valor de C: "))

discriminante = B**2 - 4*A*C

if discriminante >= 0:
    x1 = (-B + math.sqrt(discriminante)) / (2*A)
    x2 = (-B - math.sqrt(discriminante)) / (2*A)
    
    print("Las soluciones son:")
    print("x1 =", x1)
    print("x2 =", x2)
else:
    print("La ecuación no tiene solución real.")
