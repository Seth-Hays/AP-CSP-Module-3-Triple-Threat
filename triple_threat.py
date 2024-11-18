"""
Triple threat simulation game for AP Computer Science Principles.
Monarch High School - Boulder Valley School District
Seth Hays - November 2024
"""

import random

def main() -> None:
    # set variables for cost to play and base prize
    cost_to_play: int = 3
    base_prize: int = 20
    mega_number: int = 6
    mega_multiplier: int = 10

    min_plays: int = 1000
    max_plays: int = 5000

    num_days: int = 10
    print("Games Played,Total Collected,Total Paid Out,Profit")

    for _ in range(num_days):
        #Generate random number of plays
        num_plays: int = random.randint(min_plays, max_plays)

        total_collected: int = 0
        total_payout: int = 0
        total_profit: int = 0

        for _ in range(num_plays):
            # roll three dice
            dice_1: int = random.randint(1,6)
            dice_2: int = random.randint(1,6)
            dice_3: int = random.randint(1,6)


            # check if they are equal
            # if they are, calculate the prize

            payout: int = 0
            if dice_1 == dice_2 and dice_1 == dice_3:
                if dice_1 == mega_number:
                    payout += dice_1 * mega_multiplier
                else:
                    payout += base_prize * dice_1
            
            profit: int = cost_to_play - payout
            total_collected += cost_to_play
            total_payout += payout
            total_profit += profit

            #Output results for one game
        print(f"{num_plays},{total_collected},{total_payout},{total_profit}")


if __name__ == "__main__":
    main()