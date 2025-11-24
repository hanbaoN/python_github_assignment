print("Welcome to my Python program!")

#get user input
stickers= input("How many stickers did you buy today?")

#convert input & perform a calculation
stickers= float(stickers)
weekly_stickers= stickers *7

#display output
print(f"You are expected to buy {weekly_stickers} stickers this week.")

#error handling
try:
    stickers+ float(stickers)
except ValueError:
    print("Please enter a valid number.")
    exit()
