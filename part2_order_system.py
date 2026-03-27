#Task 1 — Explore the Menu
menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

# 1. Grouped Menu Printing
categories = ["Starters", "Mains", "Desserts"]
for cat in categories:
    print(f"\n===== {cat} =====")
    for item, info in menu.items():
        if info["category"] == cat:
            status = "[Available]" if info["available"] else "[Unavailable]"
            # :<15 makes the name take 15 spaces for alignment
            print(f"{item:<18} ₹{info['price']:>6.2f}   {status}")

# 2. Dictionary Calculations
total_items = len(menu)
# We use a list comprehension to filter only available items
available_count = len([item for item, info in menu.items() if info["available"]])

# Finding the most expensive
most_expensive_item = max(menu, key=lambda x: menu[x]["price"])
expensive_price = menu[most_expensive_item]["price"]

# Items under 150
under_150 = [item for item, info in menu.items() if info["price"] < 150]

print("\n--- Menu Statistics ---")
print(f"Total Items: {total_items}")
print(f"Available Items: {available_count}")
print(f"Most Expensive: {most_expensive_item} (₹{expensive_price})")
print(f"Items under ₹150: {', '.join(under_150)}")



#Task 2 — Cart Operations
cart = []

def add_to_cart(item_name, qty):
    # Check if item exists in menu
    if item_name not in menu:
        print(f"❌ Error: '{item_name}' does not exist in the menu.")
        return
    
    # Check if available
    if not menu[item_name]["available"]:
        print(f"❌ Error: '{item_name}' is currently unavailable.")
        return

    # Check if already in cart
    for entry in cart:
        if entry["item"] == item_name:
            entry["quantity"] += qty
            print(f"✓ Updated {item_name} quantity to {entry['quantity']}.")
            return
            
    # If not in cart, add new entry
    cart.append({"item": item_name, "quantity": qty, "price": menu[item_name]["price"]})
    print(f"✓ Added {item_name} x{qty} to cart.")

def remove_from_cart(item_name):
    for i in range(len(cart)):
        if cart[i]["item"] == item_name:
            cart.pop(i)
            print(f"🗑️ Removed {item_name} from cart.")
            return
    print(f"⚠️ '{item_name}' not found in cart.")

# --- Simulation Steps ---
add_to_cart("Paneer Tikka", 2)
add_to_cart("Gulab Jamun", 1)
add_to_cart("Paneer Tikka", 1) # Should update to 3
add_to_cart("Mystery Burger", 1) # Invalid
add_to_cart("Chicken Wings", 1) # Unavailable
remove_from_cart("Gulab Jamun")

# --- Final Order Summary ---
print("\n========== Order Summary ==========")
subtotal = 0
for entry in cart:
    line_total = entry["quantity"] * entry["price"]
    subtotal += line_total
    print(f"{entry['item']:<18} x{entry['quantity']}    ₹{line_total:>7.2f}")

gst = subtotal * 0.05
total_payable = subtotal + gst

print("-" * 35)
print(f"Subtotal:                ₹{subtotal:>7.2f}")
print(f"GST (5%):                ₹{gst:>7.2f}")
print(f"Total Payable:           ₹{total_payable:>7.2f}")
print("====================================")



#Task 3 — Inventory & Deep Copy
import copy

inventory = {
    "Paneer Tikka": {"stock": 10, "reorder_level": 3},
    "Veg Biryani": {"stock": 6, "reorder_level": 3},
    "Garlic Naan": {"stock": 30, "reorder_level": 10},
    # ... (Include all other items from the provided data here)
}

# 1. Deep Copy
inventory_backup = copy.deepcopy(inventory)

# Prove it works:
inventory["Paneer Tikka"]["stock"] = 99
print(f"Original Stock: {inventory['Paneer Tikka']['stock']}")
print(f"Backup Stock (Should be 10): {inventory_backup['Paneer Tikka']['stock']}")

# Restore original state
inventory = copy.deepcopy(inventory_backup)

# 2. Fulfill Order from Task 2 (Paneer Tikka x3)
for entry in cart:
    item = entry["item"]
    qty_needed = entry["quantity"]
    
    if item in inventory:
        current_stock = inventory[item]["stock"]
        if current_stock >= qty_needed:
            inventory[item]["stock"] -= qty_needed
        else:
            print(f"⚠️ Low Stock for {item}! Providing only {current_stock}.")
            inventory[item]["stock"] = 0

# 3. Reorder Alerts
print("\n--- Inventory Alerts ---")
for item, data in inventory.items():
    if data["stock"] <= data["reorder_level"]:
        print(f"⚠ Reorder Alert: {item} — Only {data['stock']} left (reorder level: {data['reorder_level']})")



#Task 4 — Daily Sales Analysis
# Add the new day
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]

# 1. Revenue per day & Best-selling day
daily_totals = {}
for date, orders in sales_log.items():
    total_rev = sum(order["total"] for order in orders)
    daily_totals[date] = total_rev
    print(f"{date}: ₹{total_rev:.2f}")

best_day = max(daily_totals, key=daily_totals.get)
print(f"\nBest Selling Day: {best_day} (₹{daily_totals[best_day]})")

# 2. Numbered list using enumerate
print("\n--- All Orders List ---")
all_orders_flat = []
for date, orders in sales_log.items():
    for order in orders:
        all_orders_flat.append((date, order))

for i, (date, order) in enumerate(all_orders_flat, 1):
    items_str = ", ".join(order["items"])
    print(f"{i}. [{date}] Order #{order['order_id']} — ₹{order['total']:.2f} — Items: {items_str}")