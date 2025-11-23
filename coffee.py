class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, coffee):
        self.items.append(coffee)
        print(f"Added {coffee.name} to your order.")

    def total(self):
        return sum(item.price for item in self.items)

    def show_order(self):
        if not self.items:
            print("No items in order.")
            return

        print("\nYour Order:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - ${item.price}")

        print(f"Total: ${self.total()}\n")

    def checkout(self):
        if not self.items:
            print("Your cart is empty.")
            return

        self.show_order()
        confirm = input("Proceed to checkout? (yes/no): ").lower()

        if confirm == "yes":
            print("Order confirmed! Thank you.")
            self.items.clear()
        else:
            print("Checkout cancelled.")


def main():
    menu = [
        Coffee("Espresso", 3),
        Coffee("Americano", 5),
        Coffee("Latte", 2.35),
        Coffee("Cappuccino", 2.5),
        Coffee("Cold Coffee With Ice Cream", 4.25)
    ]

    order = Order()

    while True:
        print("\n--- Coffee Menu ---")
        for i, coffee in enumerate(menu, 1):
            print(f"{i}. {coffee.name} - ${coffee.price}")

        print("6. View Order")
        print("7. Checkout")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice.isdigit() and 1 <= int(choice) <= 5:
            order.add_item(menu[int(choice) - 1])

        elif choice == "6":
            order.show_order()

        elif choice == "7":
            order.checkout()

        elif choice == "8":
            print("Thanks for visiting. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
    