class Interface:

    def __init__(self):
        self.messages = {
            "success": "Producto agregado exitosamente.",
            "id_used": "ID ya asignado a otro producto.",
            "invalid_data": "Datos inválidos. Por favor intente de nuevo.",
            "del_success": "Producto eliminado exitosamente.",
            "id_no_exist": "ID de producto no existe.",
            "invalid_id": "ID del producto inválido. Por favor intente de nuevo.",
            "update_success": "Producto actualizado exitosamente.",
            "exit": "Saliendo del programa.",
            "invalid_option": "Opción inválida. Por favor intente de nuevo.",
        }

    @staticmethod
    def display_menu(display_func):
        print("\n\n")
        print("========================================")
        print("Lista de Productos:")
        print("========================================")
        display_func()
        print("========================================")
        print("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir")
        return input("Elija opción: ").strip()

    @staticmethod
    def get_product_details(new_product=True):
        if new_product:
            name = input("Ingrese nombre del producto: ").strip()
            price = input("Ingrese precio del producto: ").strip()
            stock = input("Ingrese stock del producto: ").strip()
        else:
            name = input("Ingrese nuevo nombre del producto (dejar vacío si no quiere cambiarlo): ").strip()
            price = input("Ingrese nuevo precio del producto (dejar vacío si no quiere cambiarlo): ").strip()
            stock = input("Ingrese nuevo stock del producto (dejar vacío si no quiere cambiarlo): ").strip()
        return name, price, stock

    @staticmethod
    def get_product_id():
        return input("Ingrese ID del producto: ").strip()
