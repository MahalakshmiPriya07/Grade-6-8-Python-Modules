import random
summer_activities = [
    "Go to the beach",
    "Have a picnic",
    "Play frisbee",
    "Go swimming",
    "Have a barbecue"
]
print("Welcome to the Summer Activity Suggester!")
name = input("What's your name? ")

activity = random.choice(summer_activities)
print(f"Hey {name}, why don't you {activity.lower()} today?")