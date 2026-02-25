from servicios.inventario import Inventario
from modelos.producto import Producto

def limpiar_pantalla():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPresione Enter para continuar...")

def leer_entero(msg: str, min_val: int = None) -> int:
    while True:
        try:
            valor = int(input(msg))
            if min_val is not None and valor < min_val:
                print(f"  Valor mínimo permitido: {min_val}")
                continue
            return valor
        except ValueError:
            print("  Ingrese un número entero válido.")

def leer_float(msg: str, min_val: float = 0.01) -> float:
    while True:
        try:
            valor = float(input(msg))
            if valor < min_val:
                print(f"  Valor mínimo permitido: {min_val}")
                continue
            return valor
        except ValueError:
            print("  Ingrese un número decimal válido.")

def main():
    inventario = Inventario()

    while True:
        limpiar_pantalla()
        print("=" * 60)
        print("       SISTEMA DE GESTIÓN DE INVENTARIOS - POO")
        print("=" * 60)
        print("  1. Agregar nuevo producto")
        print("  2. Eliminar producto por ID")
        print("  3. Actualizar cantidad / precio")
        print("  4. Buscar productos por nombre")
        print("  5. Mostrar todos los productos")
        print("  0. Salir")
        print("=" * 60)

        opcion = input("\n  Seleccione opción → ").strip()

        if opcion == "0":
            print("\n  ¡Gracias por usar el sistema!")
            break

        elif opcion == "1":
            print("\n  → Agregar producto")
            while True:
                id_prod = leer_entero("  ID (número único): ")
                if inventario.existe_id(id_prod):
                    print("  ¡Error! ID ya existe.")
                else:
                    break
            nombre = input("  Nombre: ").strip()
            cantidad = leer_entero("  Cantidad inicial: ", min_val=0)
            precio = leer_float("  Precio unitario ($): ")

            try:
                prod = Producto(id_prod, nombre, cantidad, precio)
                if inventario.agregar(prod):
                    print(f"\n  ✓ Producto '{nombre}' agregado y guardado correctamente.")
                else:
                    print("\n  ✗ Falló al guardar en archivo.")
            except ValueError as e:
                print(f"\n  ✗ Error de validación: {e}")
            pausar()

        elif opcion == "2":
            print("\n  → Eliminar producto")
            id_prod = leer_entero("  ID a eliminar: ")
            if inventario.eliminar(id_prod):
                print("  ✓ Producto eliminado y archivo actualizado.")
            else:
                print("  ✗ No se encontró el ID o falló al guardar.")
            pausar()

        elif opcion == "3":
            print("\n  → Actualizar producto")
            id_prod = leer_entero("  ID del producto: ")
            if not inventario.existe_id(id_prod):
                print("  ✗ No existe producto con ese ID.")
                pausar()
                continue

            print("  (deje en blanco si no desea cambiar)")
            cant_str = input("  Nueva cantidad: ").strip()
            prec_str = input("  Nuevo precio ($): ").strip()

            nueva_cant = int(cant_str) if cant_str else None
            nuevo_prec = float(prec_str) if prec_str else None

            if inventario.actualizar(id_prod, nueva_cant, nuevo_prec):
                print("  ✓ Producto actualizado y guardado.")
            else:
                print("  ✗ Falló al guardar cambios.")
            pausar()

        elif opcion == "4":
            print("\n  → Buscar por nombre")
            texto = input("  Texto a buscar (parcial): ").strip()
            resultados = inventario.buscar_por_nombre(texto)
            if resultados:
                print(f"\n  Encontrados {len(resultados)} producto(s):")
                for p in resultados:
                    print(f"  {p}")
            else:
                print("  No se encontraron coincidencias.")
            pausar()

        elif opcion == "5":
            inventario.mostrar_todos()
            pausar()

        else:
            print("\n  Opción no válida.")
            pausar()

if __name__ == "__main__":
    main()