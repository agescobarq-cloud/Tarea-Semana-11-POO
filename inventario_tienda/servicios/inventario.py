from modelos.producto import Producto
from typing import List, Optional
import os

class Inventario:
    """
    Clase que gestiona la colección de productos con persistencia en archivo de texto.
    Cada cambio (agregar, eliminar, actualizar) se refleja inmediatamente en el archivo.
    """
    
    def __init__(self, archivo: str = "inventario.txt"):
        self._productos: List[Producto] = []
        self.archivo = archivo
        self._cargar_desde_archivo()

    def _cargar_desde_archivo(self) -> None:
        """Carga los productos desde el archivo al iniciar el inventario."""
        if not os.path.exists(self.archivo):
            print(f"Archivo {self.archivo} no existe → se creará uno nuevo al guardar.")
            return

        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                for linea in f:
                    linea = linea.strip()
                    if not linea or linea.startswith('#'):
                        continue
                    try:
                        id_str, nombre, cant_str, precio_str = linea.split('|', 3)
                        producto = Producto(
                            id_producto=int(id_str.strip()),
                            nombre=nombre.strip(),
                            cantidad=int(cant_str.strip()),
                            precio=float(precio_str.strip())
                        )
                        self._productos.append(producto)
                    except (ValueError, IndexError) as e:
                        print(f"Advertencia: línea inválida ignorada → {linea!r} ({e})")
        except PermissionError:
            print(f"ERROR: No tienes permiso de lectura en {self.archivo}")
        except Exception as e:
            print(f"ERROR inesperado al leer {self.archivo}: {e}")

    def _guardar_en_archivo(self) -> bool:
        """Guarda TODOS los productos actuales en el archivo (sobrescribe)."""
        try:
            with open(self.archivo, 'w', encoding='utf-8') as f:
                f.write("id|nombre|cantidad|precio\n")  # encabezado opcional
                for p in sorted(self._productos, key=lambda x: x.id):
                    f.write(f"{p.id}|{p.nombre}|{p.cantidad}|{p.precio:.2f}\n")
            return True
        except PermissionError:
            print(f"ERROR: No tienes permiso de escritura en {self.archivo}")
            return False
        except Exception as e:
            print(f"ERROR al guardar en {self.archivo}: {e}")
            return False

    def agregar_producto(self, producto: Producto) -> bool:
        if any(p.id == producto.id for p in self._productos):
            return False
        
        self._productos.append(producto)
        if self._guardar_en_archivo():
            return True
        else:
            # rollback básico (opcional)
            self._productos.remove(producto)
            return False

    def eliminar_producto(self, id_producto: int) -> bool:
        for i, producto in enumerate(self._productos):
            if producto.id == id_producto:
                del self._productos[i]
                if self._guardar_en_archivo():
                    return True
                else:
                    # rollback (poco probable pero buena práctica)
                    self._productos.insert(i, producto)
                    return False
        return False

    def actualizar_producto(self, id_producto: int, cantidad: Optional[int] = None, 
                           precio: Optional[float] = None) -> bool:
        for producto in self._productos:
            if producto.id == id_producto:
                viejo_cantidad = producto.cantidad
                viejo_precio = producto.precio
                
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                    
                if self._guardar_en_archivo():
                    return True
                else:
                    # rollback
                    producto.cantidad = viejo_cantidad
                    producto.precio = viejo_precio
                    return False
        return False

    def buscar_por_nombre(self, texto: str) -> List[Producto]:
        texto = texto.lower().strip()
        return [p for p in self._productos if texto in p.nombre.lower()]

    def obtener_todos(self) -> List[Producto]:
        return sorted(self._productos, key=lambda p: p.id)

    def esta_vacio(self) -> bool:
        return len(self._productos) == 0