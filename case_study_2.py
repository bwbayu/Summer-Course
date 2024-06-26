import random
# first_dice = int(input())
# second_dice = int(input())
first_dice = random.randint(1,6)
second_dice = random.randint(1,6)
dice_sum = first_dice + second_dice

print(f"first dice: {first_dice}")
print(f"second dice: {second_dice}")
print(f"sum : {dice_sum}")

if dice_sum in [7,11]:
    print("You Win!")

elif dice_sum in [2,3,12]:
    print("You Lose :(")

elif dice_sum in range(4,11):

    point = dice_sum
    first_dice = random.randint(1,6)
    second_dice = random.randint(1,6)
    dice_sum = first_dice + second_dice

    while dice_sum != point and dice_sum != 7:
        print(f"first dice: {first_dice}")
        print(f"second dice: {second_dice}")
        print(f"sum : {dice_sum}")
        first_dice = random.randint(1,6)
        second_dice = random.randint(1,6)
        dice_sum = first_dice + second_dice

    print(f"first dice: {first_dice}")
    print(f"second dice: {second_dice}")
    print(f"sum : {dice_sum}")
    if dice_sum == point:
        print("You Win!")
    elif dice_sum == 7:
        print("You Lose :(")