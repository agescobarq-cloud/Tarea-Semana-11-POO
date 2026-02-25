class Producto:
    """
    Representa un producto en el inventario de la tienda.
    Utiliza encapsulamiento con propiedades para controlar acceso a atributos.
    """
    def __init__(self, id_producto: int, nombre: str, cantidad: int, precio: float):
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero")
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        self._id = id_producto
        self._nombre = nombre.strip()
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    @property
    def id(self) -> int:
        return self._id

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def cantidad(self) -> int:
        return self._cantidad

    @property
    def precio(self) -> float:
        return self._precio

    # Setters
    @nombre.setter
    def nombre(self, valor: str):
        if not valor.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor.strip()

    @cantidad.setter
    def cantidad(self, valor: int):
        if valor < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self._cantidad = valor

    @precio.setter
    def precio(self, valor: float):
        if valor <= 0:
            raise ValueError("El precio debe ser mayor que cero")
        self._precio = valor

    def __str__(self) -> str:
        return f"ID: {self._id:>4} | {self._nombre:<35} | Cant: {self._cantidad:>4} | ${self._precio:>8.2f}"