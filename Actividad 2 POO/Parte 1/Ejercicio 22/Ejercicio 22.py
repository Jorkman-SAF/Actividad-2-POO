nombre = input("Ingrese el nombre del empleado: ")
salario_hora = float(input("Ingrese el salario b�sico por hora del empleado: "))
horas_trabajadas = float(input("Ingrese el n�mero de horas trabajadas en el mes: "))

salario_mensual = salario_hora * horas_trabajadas

if salario_mensual > 450000:
    print("El salario mensual de", nombre, "es de $", salario_mensual)
else:
    print(nombre)
