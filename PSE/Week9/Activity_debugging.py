from random import randint

# the loop is
for i in range(1, 20):
    if i == 20:
        print(f"You got it!")

# example 2
dice_images = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(1, 6)
print(dice_images[dice_num])