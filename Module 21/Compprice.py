class Computer:
    def __init__(self, base_price, ram, storage):
        self.base_price = base_price
        self.ram = ram
        self.storage = storage

    def calculate_price(self):
        # Price adjustments based on RAM and storage
        ram_price = 50 * self.ram  # $50 per GB of RAM
        storage_price = 20 * self.storage  # $20 per GB of storage

        # Calculate total price
        total_price = self.base_price + ram_price + storage_price
        return total_price

# Take user input for base price, RAM, and storage
base_price = float(input("Enter the base price of the computer: "))
ram = int(input("Enter the amount of RAM (in GB): "))
storage = int(input("Enter the amount of storage (in GB): "))

# Create a Computer object
computer = Computer(base_price, ram, storage)

# Calculate and print the final price
final_price = computer.calculate_price()
print(f"The final price of the computer is: ${final_price:.2f}")
