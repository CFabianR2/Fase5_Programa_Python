# ==========================================
# FASE 5 - EVALUACIÓN FINAL POA
# FUNDAMENTOS DE PROGRAMACIÓN
# Solucion problema 5: Control de horas semanales
# Codigo fuente: Autoria propia
# ==========================================

# Matriz con los recursos y horas trabajadas
recursos = [
    ["Felipe", 8, 8, 9, 8, 8],
    ["Fabian", 6, 9, 12, 9, 8],
    ["Andrea", 7, 8, 8, 7, 8],
    ["Milena", 9, 9, 9, 8, 9]
]

# Función para calcular el total de horas
# y clasificar la jornada laboral
def calcular_horas(recurso):

    nombre = recurso[0]

    total_horas = sum(recurso[1:])

    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return nombre, total_horas, clasificacion


# Título del programa
print("===================================")
print("CONTROL DE HORAS SEMANALES")
print("===================================\n")


# Recorrer la matriz
for recurso in recursos:

    nombre, total, clasificacion = calcular_horas(recurso)

    print("Nombre del recurso:", nombre)
    print("Total de horas trabajadas:", total)
    print("Clasificación:", clasificacion)
    print("-----------------------------------")