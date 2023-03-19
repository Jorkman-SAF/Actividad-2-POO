nombre = input("Ingrese el nombre del empleado: ")
salario_hora = float(input("Ingrese el salario básico por hora del empleado: "))
horas_trabajadas = float(input("Ingrese el número de horas trabajadas en el mes: "))

salario_mensual = salario_hora * horas_trabajadas

if salario_mensual > 450000:
    print("El salario mensual de", nombre, "es de $", salario_mensual)
else:
    print(nombre)
