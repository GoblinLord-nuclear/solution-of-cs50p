item_menu={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
price=0
while True:
    try:
        item=input("Item:").strip().title()
        if item not in item_menu:
            raise KeyError
        else:
            price+=item_menu[item]
            print(f"Total: ${price:.2f}")
    except EOFError:
        print("")
        print(f"Total: ${price:.2f}")
        break
    except KeyError:
        print("your item is not in the menu")