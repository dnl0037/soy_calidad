from product_manager import ProductManager
from interface import Interface


class ProductApp:
    def __init__(self):
        self.pm = ProductManager()
        self.intf = Interface()

    def handle_add_product(self):
        name, price, stock = self.intf.get_product_details()

        name, valid_name = self.pm.validate_name(name)
        price, valid_price = self.pm.validate_price(price)
        stock, valid_stock = self.pm.validate_stock(stock)

        if valid_name and valid_price and valid_stock:
            success = self.pm.add_product(name, price, stock)
            msg = self.intf.messages["success"] if success else self.intf.messages["id_used"]
        else:
            msg = self.intf.messages["invalid_data"]

        print(msg)

    def handle_remove_product(self):
        product_id = self.intf.get_product_id()
        product_id, valid_id = self.pm.validate_id(product_id)

        if valid_id:
            success = self.pm.remove_product(product_id)
            msg = self.intf.messages["del_success"] if success else self.intf.messages["id_no_exist"]
        else:
            msg = self.intf.messages["invalid_id"]

        print(msg)

    def handle_update_product(self):
        product_id = self.intf.get_product_id()
        product_id, valid_id = self.pm.validate_id(product_id)

        if valid_id:
            name, price, stock = self.intf.get_product_details(new_product=False)
            price = self.pm.validate_price(price)[0] if price else None
            stock = self.pm.validate_stock(stock)[0] if stock else None

            success = self.pm.update_product(product_id, name or None, price, stock)
            msg = self.intf.messages["update_success"] if success else self.intf.messages["id_no_exist"]
        else:
            msg = self.intf.messages["invalid_id"]

        print(msg)

    def run(self):
        actions = {
            '1': self.handle_add_product,
            '2': self.handle_remove_product,
            '3': self.handle_update_product,
            '4': lambda: (print(self.intf.messages["exit"]) or exit())
        }

        while True:
            option = self.intf.display_menu(self.pm.show_products)
            action = actions.get(option)
            if action:
                action()
            else:
                print(self.intf.messages["invalid_option"])


if __name__ == "__main__":
    app_ = ProductApp()
    app_.run()
