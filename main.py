
menu = {
    "Еспресо": 20,
    "Рістрето": 23,
    "Лате": 30,
    "Капучіно": 30,
    "Американо": 25,
    "Допіо": 35,
}

def show_menu():
    for item, price in menu.items():
        print(item, '-', price)

def add_to_menu(name, price):
    menu[name] = price
    show_menu()

def calculate_order(order, menu):
    total_cost = 0
    print("Your order:")
    for item, quantity in order.items():
        item_price = menu[item]
        item_cost = item_price * quantity
        total_cost += item_cost
        print(f"{item}: {quantity} x {item_price} = {item_cost}")

    print(f"Total amount: {total_cost}")

def checkOrder(orderName):
    return isinstance(orderName, str) and orderName in menu

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        try:
            float(s)
            return True
        except ValueError:
            try:
                complex(s)
                return True
            except ValueError:
                return False

def to_number(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            try:
                return complex(s)
            except ValueError:
                return False


def main():
    choice = ""
    order = {}
    show_menu()

    while True:

        if len(choice) == 0:
            choice = input("To choose your coffee please type the name:")
            if not checkOrder(choice):
                print("Only string are allowed or there is no such item, please try again")
                choice = input("If you wish to add something new to menu type 'new' or press any bottom to skip")
                if choice == "new":
                    name = input("Enter name")
                    price = int((input("Enter price")))
                    add_to_menu(name, price)

                choice = ""
                continue

        if choice == "end":
            break
        elif choice == "new":
            print("new")

        else:
            amount = input("Enter amount: ")
            if is_number(amount):
                order[choice] = order.get(choice, 0) + to_number(amount)
                choice = input("If you wish to continue type 'Y' if yon want to finish press any bottom")
                if choice == "Y":
                    choice = ""
                    continue
                else:
                    break


            else:
                print("Only numbers are allowed, please try again")
                continue

    calculate_order(order, menu)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
