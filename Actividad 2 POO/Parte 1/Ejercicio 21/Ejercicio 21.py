
lado1 = float(input("Ingrese el valor del primer lado del triángulo: "))
lado2 = float(input("Ingrese el valor del segundo lado del triángulo: "))
lado3 = float(input("Ingrese el valor del tercer lado del triángulo: "))

perimetro = lado1 + lado2 + lado3
semiperimetro = perimetro / 2

s = semiperimetro
area = (s * (s - lado1) * (s - lado2) * (s - lado3)) ** 0.5

print("El perímetro del triángulo es:", perimetro)
print("El semiperímetro del triángulo es:", semiperimetro)
print("El área del triángulo es:", area)
