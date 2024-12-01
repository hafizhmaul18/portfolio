class Item:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item: Item):
        # Add the item to the cart
        self.items.append(item)

    def total(self) -> int:
        # Calculate the total price of all items in the cart
        return sum(item.price for item in self.items)

    def __len__(self):
        # Return the number of items in the cart
        return len(self.items)


# Example usage:
# Create items
item1 = Item("apple", 10)
item2 = Item("banana", 5)

# Create a shopping cart and add items
cart = ShoppingCart()
cart.add(item1)
cart.add(item2)

# Get total price and the number of items in the cart
print(cart.total())      # Output should be 15
print(len(cart))         # Output should be 2
