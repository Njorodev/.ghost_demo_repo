"""
Grandfather Ghost Calculator 👻

A haunted calculator that performs calculations
while offering wisdom from Grandfather Ghost.
"""

import random


class GrandfatherGhostCalculator:
    GHOST_QUOTES = [
        "Back in my day, we calculated this by hand!",
        "A wise ghost always checks their math twice.",
        "The spirits approve of your calculation.",
        "Even beyond the grave, numbers still matter.",
        "Your ancestors are impressed by this arithmetic.",
    ]

    def __init__(self, name="Grandfather Ghost"):
        self.name = name

    def whisper(self):
        print(f"\n👻 {self.name}: {random.choice(self.GHOST_QUOTES)}")

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Ghosts cannot divide by zero!")
        return a / b


def main():
    ghost = GrandfatherGhostCalculator()

    print("=" * 50)
    print("👻 GRANDFATHER GHOST CALCULATOR 👻")
    print("=" * 50)

    while True:
        print("\nChoose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("\nYour choice: ")

        if choice == "5":
            print("\n👻 Farewell, young one...")
            break

        try:
            a = float(input("First number: "))
            b = float(input("Second number: "))

            if choice == "1":
                result = ghost.add(a, b)
            elif choice == "2":
                result = ghost.subtract(a, b)
            elif choice == "3":
                result = ghost.multiply(a, b)
            elif choice == "4":
                result = ghost.divide(a, b)
            else:
                print("Invalid choice.")
                continue

            print(f"\n✅ Result: {result}")
            ghost.whisper()

        except Exception as e:
            print(f"\n💀 Error: {e}")


if __name__ == "__main__":
    main()