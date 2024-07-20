from inventory import Inventory
from product import Product

def main():
    # Crear una instancia de inventario
    inventory = Inventory()

    # Ejemplo de agregar productos al inventario
    product1 = Product("001", "Camisa", 20, 15.99)
    product2 = Product("002", "Pantalón", 15, 29.99)
    product3 = Product("003", "Zapatos", 30, 49.99)

    inventory.add_product(product1)
    inventory.add_product(product2)
    inventory.add_product(product3)

    # Ejemplo de mostrar el inventario
    print("Inventario Actual:")
    inventory.display_inventory()

if __name__ == "__main__":
    main()
    class Inventory:
    
    
    
    def
    
    
    __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_inventory(self):
        for product in self.products:
            print(f"Código: {product.code}, Nombre: {product.name}, Cantidad: {product.quantity}, Precio: ${product.price}")