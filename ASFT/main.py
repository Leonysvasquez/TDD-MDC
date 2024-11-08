# main.py

from maquina_cafe import MaquinaCafe, VasoInvalidoError, AzucarInvalidaError, SinRecursosError

def mostrar_menu():
    print("\n--- Máquina Dispensadora de Café ---")
    print("1. Seleccionar tamaño de vaso")
    print("2. Seleccionar cantidad de azúcar")
    print("3. Recoger vaso de café")
    print("4. Recargar recursos")
    print("5. Mostrar estado de la máquina")
    print("6. Salir")

def seleccionar_tamano(maquina):
    print("\nSelecciona el tamaño del vaso:")
    print("1. Pequeño (3 Oz)")
    print("2. Mediano (5 Oz)")
    print("3. Grande (7 Oz)")
    opcion = input("Ingresa el número correspondiente: ")
    tamano_map = {'1': 'Pequeño', '2': 'Mediano', '3': 'Grande'}
    tamano = tamano_map.get(opcion)
    if tamano:
        try:
            maquina.seleccionar_vaso(tamano)
        except VasoInvalidoError as e:
            print(f"Error: {e}")
    else:
        print("Opción inválida. Por favor, intenta nuevamente.")

def seleccionar_azucar(maquina):
    print("\nSelecciona la cantidad de azúcar (cucharadas):")
    try:
        cucharadas = int(input("Ingresa el número de cucharadas: "))
        maquina.seleccionar_azucar(cucharadas)
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")
    except AzucarInvalidaError as e:
        print(f"Error: {e}")

def recoger_vaso(maquina):
    print("\nRecogiendo vaso de café...")
    try:
        maquina.recoger_vaso()
    except SinRecursosError as e:
        print(f"Error: {e}")

def recargar_recursos(maquina):
    print("\nRecargar recursos:")
    print("1. Café")
    print("2. Azúcar")
    print("3. Vasos")
    opcion = input("Ingresa el número correspondiente al recurso a recargar: ")
    if opcion == '1':
        try:
            cantidad = int(input("Ingresa la cantidad de café a recargar (Oz): "))
            maquina.recargar_cafe(cantidad)
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")
    elif opcion == '2':
        try:
            cantidad = int(input("Ingresa la cantidad de azúcar a recargar (cucharadas): "))
            maquina.recargar_azucar(cantidad)
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")
    elif opcion == '3':
        tamano = input("Ingresa el tamaño del vaso a recargar (Pequeño, Mediano, Grande): ")
        try:
            cantidad = int(input("Ingresa la cantidad de vasos a recargar: "))
            maquina.recargar_vasos(tamano, cantidad)
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")
        except VasoInvalidoError as e:
            print(f"Error: {e}")
    else:
        print("Opción inválida. Por favor, intenta nuevamente.")

def mostrar_estado(maquina):
    print("\n--- Estado Actual de la Máquina ---")
    print(f"Café disponible: {maquina.cantidad_cafe} Oz")
    print(f"Azúcar disponible: {maquina.cantidad_azucar} cucharadas")
    print("Vasos disponibles:")
    for tamano, cantidad in maquina.vasos.items():
        print(f"  {tamano}: {cantidad} unidades")
    print("-------------------------------------")

def main():
    # Inicializamos la máquina con recursos predeterminados
    maquina = MaquinaCafe(
        cantidad_cafe=100, 
        cantidad_azucar=50, 
        vasos={"Pequeño": 10, "Mediano": 10, "Grande": 10}
    )

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            seleccionar_tamano(maquina)
        elif opcion == '2':
            seleccionar_azucar(maquina)
        elif opcion == '3':
            recoger_vaso(maquina)
        elif opcion == '4':
            recargar_recursos(maquina)
        elif opcion == '5':
            mostrar_estado(maquina)
        elif opcion == '6':
            print("¡Gracias por usar la Máquina Dispensadora de Café! Hasta luego.")
            break
        else:
            print("Opción inválida. Por favor, intenta nuevamente.")

if __name__ == '__main__':
    main()
