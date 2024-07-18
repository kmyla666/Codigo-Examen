import random
trabajadores = {}

def ingresar_trabajadores():
    global trabajadores
    nombres = ["Juan Perez", 
        "Maria Garcia", 
        "Carlos Lopez",
        "Ana Martinez",
        "Pedro Rodrigez",
        "Laura Hernandez", 
        "Miguel Sanchez",
        "Isabel Gomez", 
        "Francisco Diaz",
        "Elena Fernandez",
    ] 
    for nombre in nombres:
        sueldo = random.randint(300000, 2500000)  
        trabajadores[nombre] = (sueldo,0, 0, 0) 
    print("Se han ingresado 10 trabajadores con sus sueldos aleatorios.")

def mostrar_trabajadores_por_rango(minimo, maximo):
    global trabajadores
    print(f"\nTrabajadores con sueldos entre ${minimo} y ${maximo}:")
    print("-----------------------------------------")
    for nombre, (sueldo, _, _, _) in trabajadores.items():
        if minimo <= sueldo <= maximo:
            print(f"{nombre}: ${sueldo}")

def sueldo_mas_alto_bajo_promedio():
    global trabajadores
    sueldos = [sueldo for sueldo, _, _, _ in trabajadores.values()]
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    sueldo_promedio = sum(sueldos) / len(sueldos)
    
    nombre_sueldo_max = [nombre for nombre, (sueldo, _, _, _) in trabajadores.items() if sueldo == sueldo_max][0]
    nombre_sueldo_min = [nombre for nombre, (sueldo, _, _, _) in trabajadores.items() if sueldo == sueldo_min][0]
    
    print("\nInformación de sueldos:")
    print("----------------------")
    print(f"Sueldo más alto: {nombre_sueldo_max} - ${sueldo_max}")
    print(f"Sueldo más bajo: {nombre_sueldo_min} - ${sueldo_min}")
    print(f"Sueldo promedio: ${sueldo_promedio:.2f}")
 
def calcular_descuentos():
    global trabajadores
    for nombre, (sueldo, _, _, _) in trabajadores.items():
        descuento_afp = round(sueldo * 0.7 ,2)
        descuento_salud = round (sueldo * 0.07 ,7)
        sueldo_liquido =sueldo - descuento_afp - descuento_salud
        trabajadores[nombre] = (sueldo, descuento_afp, descuento_salud, sueldo_liquido)

def mostrar_reporte_sueldos(nombre):
    global trabajadores
    if nombre in trabajadores:
        sueldo_base,descuento_afp, descuento_salud, sueldo_liquido = trabajadores[nombre]
        print(f"\nNombre del empleado : \n{nombre}:")
        print(f"Sueldo base: ${sueldo_base}")
        print(f"Descuento AFP: ${descuento_afp:.2f}")
        print(f"Descuento Fonasa: ${descuento_salud:.2f}")
        print(f"Sueldo líquido: ${sueldo_liquido:.2f}")
    else:
        print("Trabajador no encontrado.")
def menu():
    opcion = 0
    while opcion != 5:
        print("\n----------Menu----------")
        print("1. Asignar Sueldos Aleatorios")
        print("2. Clasificar Sueldos")
        print("3. Ver estadisticas")
        print("4. Reporte de Sueldos ")
        print("5. Salir")
        opcion = int(input("Ingrese una opción: "))
        
        if opcion == 1:
            ingresar_trabajadores()
        elif opcion == 2:
            minimo = int(input("Ingrese el sueldo mínimo del rango: "))
            maximo = int(input("Ingrese el sueldo máximo del rango: "))
            mostrar_trabajadores_por_rango(minimo, maximo)
        elif opcion == 3:
            sueldo_mas_alto_bajo_promedio()
        elif opcion == 4:
            nombre = input("Ingrese el nombre del trabajador para mostrar el reporte de sueldo liquido: ")
            mostrar_reporte_sueldos(nombre)
        elif opcion == 5:
            print("Finalizando Programa....\nDesarrollado por Camila Reyes\nRut 20.144.890-5")
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
        menu()