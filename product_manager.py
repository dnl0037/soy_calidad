class ProductManager:
    def __init__(self):
        self.products = {1: 'Pantalones', 2: 'Camisas', 3: 'Corbatas', 4: 'Casacas'}
        self.prices = {1: 200.00, 2: 120.00, 3: 50.00, 4: 350.00}
        self.stock = {1: 50, 2: 45, 3: 30, 4: 15}

    def add_product(self, name, price, stock):
        product_id = max(self.products.keys(), default=0) + 1
        self.products[product_id] = name
        self.prices[product_id] = price
        self.stock[product_id] = stock
        return True

    def remove_product(self, product_id):
        if product_id not in self.products:
            return False
        del self.products[product_id]
        del self.prices[product_id]
        del self.stock[product_id]
        return True

    def update_product(self, product_id, name=None, price=None, stock=None):
        if product_id not in self.products:
            return False
        if name:
            self.products[product_id] = name
        if price:
            self.prices[product_id] = price
        if stock:
            self.stock[product_id] = stock
        return True

    @staticmethod
    def validate_id(product_id):
        try:
            product_id = int(product_id)
            if product_id <= 0:
                raise ValueError
            return product_id, True
        except ValueError:
            return product_id, False

    @staticmethod
    def validate_name(name):
        return name, bool(name)

    @staticmethod
    def validate_price(price):
        try:
            price = float(price)
            if price <= 0:
                raise ValueError
            return price, True
        except ValueError:
            return price, False

    @staticmethod
    def validate_stock(stock):
        try:
            stock = int(stock)
            if stock < 0:
                raise ValueError
            return stock, True
        except ValueError:
            return stock, False

    def show_products(self):
        print("{:<5} {:<20} {:<10} {:<10}".format("ID", "Nombre", "Precio", "Stock"))
        print("=" * 50)
        for key in self.products:
            print("{:<5} {:<20} {:<10.2f} {:<10}".format(
                key, self.products[key], self.prices[key], self.stock[key]
            ))
