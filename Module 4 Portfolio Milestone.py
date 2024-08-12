
# Step 1: Define the ItemToPurchase class
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        # Initialize the attributes
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        # Calculate the total cost for the item
        cost = self.item_price * self.item_quantity
        # Print the formatted output
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${cost}")


# Step 2: Create two objects of the ItemToPurchase class by prompting the user for input
print("Item 1")
item1_name = input("Enter the item name:\n")
item1_price = float(input("Enter the item price:\n"))
item1_quantity = int(input("Enter the item quantity:\n"))

item1 = ItemToPurchase(item1_name, item1_price, item1_quantity)

print("\nItem 2")
item2_name = input("Enter the item name:\n")
item2_price = float(input("Enter the item price:\n"))
item2_quantity = int(input("Enter the item quantity:\n"))

item2 = ItemToPurchase(item2_name, item2_price, item2_quantity)

# Step 3: Print item costs and total cost
print("\nTOTAL COST")
item1.print_item_cost()
item2.print_item_cost()

# Calculate the total cost of both items
total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
print(f"\nTotal: ${total_cost}")
