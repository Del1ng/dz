class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - {self.price} грн (в наявності: {self.stock})"

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        if product.stock >= quantity:
            self.items.append({'product': product, 'quantity': quantity})
            product.stock -= quantity
            print(f"Додано {quantity} одиниць товару '{product.name}' в кошик.")
        else:
            print(f"Недостатньо товару '{product.name}' в наявності. Доступно: {product.stock}.")

    def remove_product(self, product_name):
        for item in self.items:
            if item['product'].name == product_name:
                self.items.remove(item)
                item['product'].stock += item['quantity']
                print(f"Товар '{product_name}' видалено з кошика.")
                return
        print(f"Товар '{product_name}' не знайдено в кошику.")

    def total_price(self):
        total = sum(item['product'].price * item['quantity'] for item in self.items)
        return total

    def show_cart(self):
        if not self.items:
            print("Ваш кошик порожній.")
        else:
            print("Вміст вашого кошика:")
            for item in self.items:
                print(f"{item['product'].name} x{item['quantity']} - {item['product'].price * item['quantity']} грн")
            print(f"Загальна вартість: {self.total_price()} грн")
python
Копировать
product1 = Product("Телефон", 5000, 10)
product2 = Product("Ноутбук", 15000, 5)
product3 = Product("Гарнітура", 1000, 20)

cart = Cart()

cart.add_product(product1, 2)
cart.add_product(product2, 1)
cart.add_product(product3, 3)

cart.show_cart()

cart.remove_product("Телефон")

cart.show_cart()