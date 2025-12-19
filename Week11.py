#Variant A
def validate_and_sell(inventory, item_name, quantity):
        
        if not type(quantity) ==int:
            raise TypeError("Quantity must be integer")
        if quantity<=0:
            raise ValueError("Quantity must be positive")
        if item_name not in inventory:
            raise KeyError("Item not found")
        if inventory[item_name]<quantity:
            raise ValueError("Insufficient stock")
        inventory[item_name]-=quantity
        return True
def process_cart(inventory, cart_list):
     for item_name,quantity in cart_list:
          try:
              validate_and_sell(inventory,item_name,quantity)
              print(f"Shipped {quantity} x {item_name}")
          except (TypeError,ValueError,KeyError) as e:
               print(f"Skipping {item_name}: {e}")
warehouse = {"Laptop": 5, "Mouse": 10, "Monitor": 2}
cart = [
    ("Laptop", 2),       # Valid
    ("Monitor", "two"),  # Error: TypeError (String)
    ("Mouse", -5),       # Error: ValueError (Negative)
    ("Keyboard", 1),     # Error: KeyError (Not found)
    ("Monitor", 20)      # Error: ValueError (Stock)
]  
process_cart(warehouse,cart)




