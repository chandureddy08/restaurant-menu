# Define the menu of restaurant
menu = {
    "veg biryani": 300,
    "chicken biryani": 500,
    "mutton biryani": 600,
    "fish biryani": 700,
    "prawns biryani": 800,
}

# Greet
print("****************************")
print("Welcome to the CR Restaurant")
print("****************************")
print("Veg Biryani: Rs 300\nChicken Biryani: Rs 500\nMutton Biryani: Rs 600\nFish Biryani: Rs 700\nPrawns Biryani: Rs 800")
print("****************************")

order_total = 0
ordered_items = []  # List to track ordered items
while True:
    item = input("Enter the name of the item you wanna order: ").lower()
    if item in menu:
        order_total += menu[item]
        ordered_items.append(item)  # Add item to the list
        print(f"Item {item} has been added to your order")
        print(f"Your current total is Rs{order_total}")
    else:
        print(f"Ordered item {item} is not available!!")

    # Validate input for another order
    while True:
        another_order = input("Do you want to add another item? (Y/N): ").upper()
        if another_order in ['Y', 'N']:
            break
        else:
            print("Invalid input! Please enter 'Y' or 'N'.")

    if another_order != 'Y':
        break

# Display all ordered items and the total amount
print(f"Ordered items are: {', '.join(ordered_items)}")
print(f"The total amount is Rs{order_total}")
