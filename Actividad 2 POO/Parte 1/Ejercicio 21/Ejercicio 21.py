
lado1 = float(input("Ingrese el valor del primer lado del tri�ngulo: "))
lado2 = float(input("Ingrese el valor del segundo lado del tri�ngulo: "))
lado3 = float(input("Ingrese el valor del tercer lado del tri�ngulo: "))

perimetro = lado1 + lado2 + lado3
semiperimetro = perimetro / 2

s = semiperimetro
area = (s * (s - lado1) * (s - lado2) * (s - lado3)) ** 0.5

print("El per�metro del tri�ngulo es:", perimetro)
print("El semiper�metro del tri�ngulo es:", semiperimetro)
print("El �rea del tri�ngulo es:", area)
