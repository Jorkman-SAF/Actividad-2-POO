codigo = input("Ingrese el código del empleado: ")
nombres = input("Ingrese los nombres del empleado: ")
horas_trabajadas = float(input("Ingrese el número de horas trabajadas al mes: "))
valor_hora = float(input("Ingrese el valor por hora trabajada: "))
porcentaje_retencion = float(input("Ingrese el porcentaje de retención en la fuente: "))

salario_bruto = horas_trabajadas * valor_hora
retencion = salario_bruto * (porcentaje_retencion / 100)
salario_neto = salario_bruto - retencion

print("Código del empleado:", codigo)
print("Nombres del empleado:", nombres)
print("Salario bruto:", salario_bruto)
print("Salario neto:", salario_neto)
