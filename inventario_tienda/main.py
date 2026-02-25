from servicios.inventario import Inventario
from modelos.producto import Producto


def mostrar_menu():
    print("\n" + "=" * 50)
    print("       SISTEMA DE GESTIÓN DE INVENTARIOS")
    print("=" * 50)
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Listar todos los productos")
    print("0. Salir")
    print("=" * 50)


def obtener_entero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("¡Error! Debe ingresar un número entero.")


def obtener_float(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("¡Error! Debe ingresar un número decimal válido.")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "0":
            print("\n¡Gracias por usar el sistema! Hasta luego.\n")
            break

        elif opcion == "1":
            print("\n--- AÑADIR NUEVO PRODUCTO ---")
            id_prod = obtener_entero("ID del producto: ")
            nombre = input("Nombre del producto: ").strip()
            while not nombre:
                print("El nombre no puede estar vacío.")
                nombre = input("Nombre del producto: ").strip()

            cantidad = obtener_entero("Cantidad en stock: ")
            precio = obtener_float("Precio unitario ($): ")

            try:
                nuevo_producto = Producto(id_prod, nombre, cantidad, precio)
                if inventario.agregar_producto(nuevo_producto):
                    (f"\nProducto '{nombre}' agregado correctamente y guardado en archivo.")
                else:
                    print(f"\n¡Error! Ya existe un producto con ID {id_prod} o fallo al guardar en archivo.")
            except ValueError as e:
                print(f"\nError de validación: {e}")

        elif opcion == "2":
            print("\n--- ELIMINAR PRODUCTO ---")
            id_prod = obtener_entero("Ingrese el ID del producto a eliminar: ")
            if inventario.eliminar_producto(id_prod):
                print("Producto eliminado correctamente y archivo actualizado.")
            else:
                print("No se encontró producto con ese ID o fallo al guardar cambios.")

        elif opcion == "3":
            print("\n--- ACTUALIZAR PRODUCTO ---")
            id_prod = obtener_entero("ID del producto a actualizar: ")

            print("(Deje en blanco o presione Enter si no desea cambiar el valor)")
            cantidad_str = input("Nueva cantidad: ").strip()
            precio_str = input("Nuevo precio ($): ").strip()

            nueva_cantidad = int(cantidad_str) if cantidad_str else None
            nuevo_precio = float(precio_str) if precio_str else None

            if inventario.actualizar_producto(id_prod, nueva_cantidad, nuevo_precio):
                print("Producto actualizado correctamente y cambios guardados en archivo.")
            else:
                print("No se encontró ningún producto con ese ID.")

        elif opcion == "4":
            print("\n--- BUSCAR PRODUCTO POR NOMBRE ---")
            texto = input("Ingrese parte del nombre a buscar: ").strip()
            resultados = inventario.buscar_por_nombre(texto)

            if resultados:
                print(f"\nResultados encontrados ({len(resultados)}):")
                for prod in resultados:
                    print(prod)
            else:
                print("No se encontraron productos que coincidan.")

        elif opcion == "5":
            print("\n--- LISTADO COMPLETO DEL INVENTARIO ---")
            productos = inventario.obtener_todos()
            if inventario.esta_vacio():
                print("El inventario está vacío.")
            else:
                for prod in productos:
                    print(prod)
                print(f"\nTotal de productos: {len(productos)}")

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()