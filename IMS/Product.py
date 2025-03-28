class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"Name: {self.name}, Price: ${self.price:.2f}, Stock: {self.stock}"


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, name, price, stock):
        if name in self.products:
            print("Product already exists.")
        else:
            self.products[name] = Product(name, price, stock)
            print(f"Added product: {name}")

    def update_stock(self, name, quantity):
        if name in self.products:
            self.products[name].stock += quantity
            print(f"Updated stock for {name}. New stock: {self.products[name].stock}")
        else:
            print("Product not found.")

    def view_products(self):
        if not self.products:
            print("No products in inventory.")
        else:
            for product in self.products.values():
                print(product)

    def remove_product(self, name):
        if name in self.products:
            del self.products[name]
            print(f"Removed product: {name}")
        else:
            print("Product not found.")


def main():
    inventory = Inventory()
    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Update Stock")
        print("3. View Products")
        print("4. Remove Product")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter stock quantity: "))
            inventory.add_product(name, price, stock)
        elif choice == '2':
            name = input("Enter product name: ")
            quantity = int(input("Enter quantity to update (positive to restock, negative to sell): "))
            inventory.update_stock(name, quantity)
        elif choice == '3':
            inventory.view_products()
        elif choice == '4':
            name = input("Enter product name to remove: ")
            inventory.remove_product(name)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()