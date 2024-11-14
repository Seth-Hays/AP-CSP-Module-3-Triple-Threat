"""
Triple threat simulation game for AP Computer Science Principles.
Monarch High School - Boulder Valley School District
Seth Hays - November 2024
"""

import random

def main() -> None:
    # set variables for cost to play and base prize
    cost_to_play: int = 1
    base_prize: int = 10
    profit: int = 0
    casino_collects: int = 0
    mega_number: int = 6
    mega_multiplier: int = 10

    # roll three dice
    dice_1: int = random.randint(1,6)
    dice_2: int = random.randint(1,6)
    dice_3: int = random.randint(1,6)


    # check if they are equal
    # if they are, calculate the prize

    payout: int = 0
    casino_collects += cost_to_play
    if dice_1 == dice_2 and dice_1 == dice_3:
        if dice_1 == mega_number:
            payout += dice_1 * mega_multiplier
        else:
            payout += base_prize * dice_1

    profit += casino_collects
    profit -= payout

    print(f" Casino Collects: ${casino_collects}")
    print(f"Player Rolls: {dice_1}-{dice_2}-{dice_3}")
    print(f"Casino Pays Out: ${payout}")
    print(f"Profit: ${profit}")

    # output results

if __name__ == "__main__":
    main()