def calculate_tip(bill, tip_percent):
    tip = bill * (tip_percent / 100)
    return tip

# Input
bill = float(input("Enter the bill amount: Rs."))
tip_percent = float(input("Enter the tip percentage: "))

# Calculate and display the tip
tip = calculate_tip(bill, tip_percent)
print(f"Tip amount: Rs.{tip:.2f}")
