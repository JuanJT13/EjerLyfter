quantity = int(input("¿Cuántas notas vas a ingresar? "))

approved_count = 0
failed_count = 0
total_sum = 0
approved_sum = 0
failed_sum = 0

for i in range(quantity):
    grade = float(input(f"Ingresa la nota {i+1}: "))
    
    # Validación
    while grade < 0 or grade > 100:
        print("Nota inválida. Debe estar entre 0 y 100.")
        grade = float(input(f"Ingresa nuevamente la nota {i+1}: "))
    
    total_sum += grade
    
    if grade > 70:
        approved_count += 1
        approved_sum += grade
    else:
        failed_count += 1
        failed_sum += grade

# Promedios
average_total = total_sum / quantity

if approved_count > 0:
    average_approved = approved_sum / approved_count
else:
    average_approved = 0

if failed_count > 0:
    average_failed = failed_sum / failed_count
else:
    average_failed = 0

# Resultados
print("Cantidad de aprobadas:", approved_count)
print("Cantidad de desaprobadas:", failed_count)
print("Promedio total:", average_total)
print("Promedio de aprobadas:", average_approved)
print("Promedio de desaprobadas:", average_failed)