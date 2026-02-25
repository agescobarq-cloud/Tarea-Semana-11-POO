# Tarea-Semana-11-POO
## Estructura del Proyecto
...

## Cómo Ejecutar
...

## Decisiones de Diseño y Justificación Técnica

### Uso de colecciones
Se eligió un **diccionario** (`Dict[int, Producto]`) como estructura principal para almacenar los productos en la clase `Inventario`, en lugar de una lista. Esta decisión se tomó por las siguientes ventajas:

- **Búsqueda por ID en tiempo constante O(1)**: acceder a un producto mediante su ID es extremadamente rápido (`self.productos[id]`), ideal para operaciones frecuentes como actualizar o eliminar.
- **Eliminación y actualización directa sin recorrer la colección**: no es necesario iterar sobre todos los elementos para encontrar el producto (como ocurriría con una lista), lo que mejora significativamente el rendimiento cuando hay muchos productos.
- **Evita duplicados de ID automáticamente**: el diccionario garantiza que no existan dos productos con el mismo ID, ya que las claves son únicas por definición.

### Almacenamiento en archivos (persistencia)
Se implementó persistencia simple pero robusta utilizando un archivo de texto plano (`inventario.txt`), con las siguientes características:

- **Formato simple y legible**: cada producto se guarda en una línea con el formato  
  `id|nombre|cantidad|precio`  
  Ejemplo:
  1|Cuaderno espiral 100 hojas|25|3.50
  5|Marcador permanente negro|40|1.20
 
- **Carga automática al iniciar**: el método `_cargar_desde_archivo()` lee y reconstruye el diccionario de productos cada vez que se crea una instancia de `Inventario`.
- **Guardado automático después de cada modificación**: tras agregar, eliminar o actualizar un producto, se llama a `_guardar_en_archivo()` para sobrescribir el archivo con el estado actual completo.
- **Manejo de excepciones y robustez**:
- Líneas mal formadas (números inválidos, campos faltantes, formato incorrecto) se ignoran con una advertencia clara en consola, sin detener el programa.
- Se capturan y notifican errores como `FileNotFoundError`, `PermissionError` y excepciones inesperadas.
- Permisos de archivo denegados o errores de escritura se informan al usuario de forma amigable.

Estas decisiones permiten un sistema eficiente, tolerante a errores y fácil de depurar/inspeccionar manualmente, cumpliendo con los objetivos de la tarea sin introducir dependencias externas innecesarias.

...
