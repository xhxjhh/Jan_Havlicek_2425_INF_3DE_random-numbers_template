import random

def roll_multiple_dice(n, k):
    return [random.randint(1, 6) for _ in range(n)]
    pass

# Otestování funkce
print(roll_multiple_dice(3, 6))  # Simulace hodu 3 kostkami, každá má 6 hran
