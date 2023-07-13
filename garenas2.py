import datetime


pisos = 10
departamentos_por_piso = 4
precios = {'A': 3800, 'B': 3000, 'C': 2800, 'D': 3500}
departamentos_disponibles = [[True] * departamentos_por_piso for _ in range(pisos)]
compradores = {}


def mostrar_departamentos_disponibles():
    print("Estado actual de los departamentos:")
    for piso in range(pisos):
        for depto in range(departamentos_por_piso):
            estado = 'Disponible' if departamentos_disponibles[piso][depto] else 'Vendido'
            print(f"Piso {piso + 1} - Departamento {chr(65 + depto)}: {estado}")


def comprar_departamento():
    mostrar_departamentos_disponibles()
    piso = int(input("Ingrese el número de piso: "))
    tipo = input("Ingrese el tipo de departamento (A, B, C o D): ").upper()

    if not (1 <= piso <= pisos) or tipo not in precios:
        print("Selección inválida. Por favor, inténtelo nuevamente.")
        return

    departamento = tipo + str(piso)
    if not departamentos_disponibles[piso - 1][ord(tipo) - ord('A')]:
        print("El departamento seleccionado no está disponible. Por favor, seleccione otro.")
        return

    run = input("Ingrese el RUN del comprador (sin guiones ni puntos): ")
    compradores[run] = departamento
    departamentos_disponibles[piso - 1][ord(tipo) - ord('A')] = False

    print("La operación se ha realizado correctamente.")


def mostrar_listado_compradores():
    print("Listado de compradores (ordenado por RUN):")
    for run in sorted(compradores.keys()):
        print(f"RUN: {run} - Departamento: {compradores[run]}")


def mostrar_ventas_totales():
    totales = {tipo: 0 for tipo in precios.keys()}
    total_general = 0

    for run, depto in compradores.items():
        tipo = depto[0]
        totales[tipo] += precios[tipo]
        total_general += precios[tipo]

    print("Ventas totales:")
    print("Tipo de departamento\tCantidad\tTotal")
    for tipo in precios.keys():
        cantidad = sum(1 for depto in compradores.values() if depto[0] == tipo)
        total = totales[tipo]
        print(f"{tipo}\t\t\t{cantidad}\t\t{total}")
    print(f"\nTotal general:\t\t\t\t{total_general}")


def mostrar_menu():
    print("\n---- Inmobiliaria Casa Feliz ----")
    print("1. Comprar departamento")
    print("2. Mostrar departamentos disponibles")
    print("3. Ver listado de compradores")
    print("4. Mostrar ganancias totales")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("\nIngrese una opción: ")

        if opcion == "1":
            comprar_departamento()
        elif opcion == "2":
            mostrar_departamentos_disponibles()
        elif opcion == "3":
            mostrar_listado_compradores()
        elif opcion == "4":
            mostrar_ventas_totales()
        elif opcion == "5":
            fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y")
            nombre = "Tu nombre"  # Reemplaza "Tu nombre" por tu nombre real
            apellido = "Tu apellido"  # Reemplaza "Tu apellido" por tu apellido real
            print(f"\nGracias por utilizar el sistema. {nombre} {apellido}. Fecha: {fecha_actual}")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


main()
