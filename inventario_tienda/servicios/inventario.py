from modelos.producto import Producto
from typing import Dict, List, Optional
import os

class Inventario:
    """
    Gestiona el inventario usando un diccionario para acceso rápido por ID.
    Clave: ID (int) → Valor: objeto Producto
    Implementa persistencia en archivo de texto plano.
    """
    ARCHIVO = "inventario.txt"
    SEPARADOR = "|"

    def __init__(self):
        self.productos: Dict[int, Producto] = {}
        self._cargar_desde_archivo()

    def _cargar_desde_archivo(self) -> None:
        """Carga productos desde archivo al iniciar."""
        if not os.path.exists(self.ARCHIVO):
            print(f"→ Archivo {self.ARCHIVO} no encontrado. Se creará uno nuevo al guardar.")
            return

        try:
            with open(self.ARCHIVO, 'r', encoding='utf-8') as f:
                for num_linea, linea in enumerate(f, 1):
                    linea = linea.strip()
                    if not linea or linea.startswith('#'):
                        continue
                    try:
                        partes = linea.split(self.SEPARADOR, 3)
                        if len(partes) != 4:
                            raise ValueError("formato incompleto")
                        id_str, nombre, cant_str, precio_str = [p.strip() for p in partes]
                        prod = Producto(
                            id_producto=int(id_str),
                            nombre=nombre,
                            cantidad=int(cant_str),
                            precio=float(precio_str)
                        )
                        self.productos[prod.id] = prod
                    except Exception as e:
                        print(f"Advertencia: línea {num_line} inválida → ignorada ({e}): {linea}")
        except PermissionError:
            print(f"ERROR: Sin permiso para leer {self.ARCHIVO}")
        except Exception as e:
            print(f"ERROR al cargar {self.ARCHIVO}: {e}")

    def _guardar_en_archivo(self) -> bool:
        """Sobrescribe el archivo con todos los productos actuales."""
        try:
            with open(self.ARCHIVO, 'w', encoding='utf-8') as f:
                f.write("# Formato: id|nombre|cantidad|precio\n")
                for prod in sorted(self.productos.values(), key=lambda p: p.id):
                    f.write(f"{prod.id}{self.SEPARADOR}{prod.nombre}{self.SEPARADOR}{prod.cantidad}{self.SEPARADOR}{prod.precio:.2f}\n")
            return True
        except PermissionError:
            print(f"ERROR: Sin permiso para escribir en {self.ARCHIVO}")
            return False
        except Exception as e:
            print(f"ERROR al guardar {self.ARCHIVO}: {e}")
            return False

    # ──────────────────────────────────────────────
    # Métodos requeridos
    # ──────────────────────────────────────────────

    def agregar(self, producto: Producto) -> bool:
        """Añade producto nuevo. Retorna False si ID ya existe."""
        if producto.id in self.productos:
            return False
        self.productos[producto.id] = producto
        return self._guardar_en_archivo()

    def eliminar(self, id_producto: int) -> bool:
        """Elimina por ID. Retorna True si existía y se eliminó."""
        if id_producto in self.productos:
            del self.productos[id_producto]
            return self._guardar_en_archivo()
        return False

    def actualizar(self, id_producto: int, cantidad: Optional[int] = None, precio: Optional[float] = None) -> bool:
        """Actualiza cantidad y/o precio. Retorna True si se encontró y guardó."""
        if id_producto not in self.productos:
            return False
        prod = self.productos[id_producto]

        if cantidad is not None:
            prod.cantidad = cantidad
        if precio is not None:
            prod.precio = precio

        return self._guardar_en_archivo()

    def buscar_por_nombre(self, texto: str) -> List[Producto]:
        """Búsqueda parcial (case-insensitive) por nombre."""
        texto = texto.lower().strip()
        return [p for p in self.productos.values() if texto in p.nombre.lower()]

    def mostrar_todos(self) -> None:
        """Muestra todos los productos ordenados por ID."""
        if not self.productos:
            print("  El inventario está vacío.")
            return
        print("\n  Listado de productos (ordenado por ID):")
        print("  " + "-" * 85)
        for prod in sorted(self.productos.values(), key=lambda p: p.id):
            print(f"  {prod}")
        print("  " + "-" * 85)
        print(f"  Total productos: {len(self.productos)}")

    def existe_id(self, id_producto: int) -> bool:
        return id_producto in self.productos