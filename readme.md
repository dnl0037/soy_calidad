# Product Management Application

Esta aplicación es una sencilla herramienta de gestión de productos que permite agregar, eliminar y actualizar productos
en un inventario. Utiliza una arquitectura modular con separación clara entre frontend, backend y lógica de aplicación.

## Estructura del Proyecto

- `app.py`: Contiene la clase principal `ProductApp` que maneja el flujo de la aplicación.
- `interface.py`: Contiene la clase `Interface` que maneja la interacción con el usuario.
- `product_manager.py`: Contiene la clase `ProductManager` que maneja la lógica de negocio y la validación de datos.

## Requisitos

- Python 3.10+

## Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/dnl0037/soy_calidad.git
    cd product-management-app  # Al directorio donde hayas hecho la clonación
    ```

2. (Opcional) Crea un entorno virtual para la aplicación:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias necesarias (si las hay):

    ```bash
    pip install -r requirements.txt  # No hay dependencias externas por defecto
    ```

## Uso

Para ejecutar la aplicación, simplemente corre el script `app.py`:

```bash
python app.py 
