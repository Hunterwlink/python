import random


def roll_20(): 
    number = random.randint(1, 20)
    return number
def roll_4(): 
    number = random.randint(1, 4)
    return number

def roll_12(): 
    number = random.randint(1, 12)
    return number

def roll_6():
    number = random.randint(1, 6)
    return number

def roll_10():
    number = random.randint(1, 10)
    return number

def roll_8():
    number = random.randint(1, 8)
    return number

def d20_logo(number):
    print("    _______   ")
    print("   /        \  ")
    print("  /          \ ")
    print(" /            \\")
    print(f"|     '{number}'     | ")
    print(" \\            /")
    print("  \\          / ")
    print("   \\________/  ")

def d4_logo(number):
    print("    /\\")
    print("   /  \\")
    print(f"  / {number}  \\")
    print(" /______\\")

def d12_logo(number):
    print("    ________")
    print("   /        \\")
    print("  /          \\")
    print(" /            \\")
    print(f"|      {number}      |")  
    print(" \\            /")
    print("  \\          /")
    print("   \\________/")

def d6_logo(number):
    print("[-----]")
    print("[     ]")
    print(f"[  {number}  ]")
    print("[     ]")
    print("[-----]")

def d10_logo(number):
    print("    ______")
    print("   /      \\")
    print("  /        \\")
    print(f" |    {number}     |") 
    print("  \\        /")
    print("   \\______/")

def d8_logo(number):
    print("   /\\")
    print("  /  \\")
    print(f" / {number}  \\")  
    print("/______\\")
    print("\\      /")
    print(" \\    /")
    print("  \\  /")
    print("   \\/")

def main(): 
    while True: 
        answer= input("Which die would you like to roll?: ")
        if answer == 'd20':
            d20_logo(roll_20())
        elif answer == 'd12':
            d12_logo(roll_12())
        elif answer == 'd10':
            d10_logo(roll_10())
        elif answer == 'd8':
            d8_logo(roll_8())
        elif answer == 'd6':
            d6_logo(roll_6())
        elif answer == 'd4':
            d4_logo(roll_4())
        elif answer == 'thunder'.lower():
            d8_logo(roll_8())
            print('')
            d8_logo(roll_8())
        else:
            print("Invalid input")

main()