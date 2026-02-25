class Producto:
    """
    Clase que representa un producto en el inventario de la tienda.
    Contiene los atributos básicos y métodos para acceder/modificarlos (getters y setters).
    """

    def __init__(self, id_producto: int, nombre: str, cantidad: int, precio: float):
        """
        Constructor de la clase Producto.

        Args:
            id_producto (int): Identificador único del producto (debe ser único en el inventario)
            nombre (str): Nombre del producto
            cantidad (int): Cantidad disponible en stock (debe ser >= 0)
            precio (float): Precio unitario del producto (debe ser > 0)
        """
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero")

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
    def nombre(self, nuevo_nombre: str):
        self._nombre = nuevo_nombre.strip()

    @cantidad.setter
    def cantidad(self, nueva_cantidad: int):
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self._cantidad = nueva_cantidad

    @precio.setter
    def precio(self, nuevo_precio: float):
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor que cero")
        self._precio = nuevo_precio

    def __str__(self) -> str:
        """Representación legible del producto para mostrar en consola."""
        return (f"ID: {self._id} | Nombre: {self._nombre:.<30} | "
                f"Cantidad: {self._cantidad:>4} | Precio: ${self._precio:>7.2f}")