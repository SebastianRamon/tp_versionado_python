gastos = []


def registrar_gasto():
    concepto = input("Ingrese el concepto del gasto: ")

    try:
        monto = float(input("Ingrese el monto: "))
    except ValueError:
        print("El monto ingresado no es válido.")
        return

    if monto <= 0:
        print("El monto debe ser mayor que cero.")
        return

    gastos.append({
        "concepto": concepto,
        "monto": monto
    })

    print("Gasto registrado correctamente.")


def listar_gastos():
    if not gastos:
        print("No hay gastos registrados.")
        return

    print("\n--- GASTOS REGISTRADOS ---")

    for i, gasto in enumerate(gastos, start=1):
        print(f"{i}. {gasto['concepto']} - ${gasto['monto']:.2f}")


def iniciar():
    print("=== CONTROL DE GASTOS - VERSION ESTABLE ===")

    while True:
        print("\n1. Registrar gasto")
        print("2. Listar gastos")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_gasto()

        elif opcion == "2":
            listar_gastos()

        elif opcion == "0":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    iniciar()