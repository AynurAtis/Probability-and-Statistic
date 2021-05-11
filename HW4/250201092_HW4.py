# 250201092

import random


def gambler_A(x):

    bet = 1
    total_money = x

    while (total_money < 2*x) and (total_money > bet):
        result = rule_of_craps()
        if result:
            total_money += bet
        else:
            total_money -= bet
            bet *= 2   # if gambler lost then the bet is doubled.

    return total_money - x


# -----------Inverse Transformation Method -------------------
def Inverse_Fx(x, r):  # We take the integral of f(x) = 2x / r**2 then we take the inverse of F(x) = x**2 / r**2
    return r * x**0.5


def gambler_B(m):
    r = 0 # r is the current round number
    bet = 0
    total_money = m
    earned_money = 0

    while (earned_money < 500) and (total_money > bet):
        result = rule_of_craps()
        r += 1  # r is the current round number
        x = random.randint(0, r)
        bet = Inverse_Fx(x, r)    # inverse of pdf function (first we take an integral then we take an inverse)
        if result:
            total_money += bet
            earned_money += bet
        else:
            total_money -= bet
            earned_money -= bet

    return total_money - m


def rule_of_craps():
    flag_win = False
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    dice_sum = dice_2 + dice_1
    if dice_sum == 7 or dice_sum == 11:
        flag_win = True
    elif dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
        flag_win = False
    else:
        while True:
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            new_dice_sum = dice2 + dice1
            if dice_sum == new_dice_sum:
                flag_win = True
                break
            elif new_dice_sum == 7:
                flag_win = False
                break

    return flag_win


def main():
    counter_craps_win = 0
    counter_gamblerA1 = 0
    counter_gamblerA2 = 0
    counter_gamblerB1 = 0
    counter_gamblerB2 = 0
    for i in range(10000):      # monte carlo simulation for prob of winning a round of craps
        result = rule_of_craps()
        if result:
            counter_craps_win += 1
    for i in range(10000):      # monte carlo simulation for expected gain for gamblerA and gamblerB
        counter_gamblerA1 += gambler_A(1000)
        counter_gamblerA2 += gambler_A(1000000)
        counter_gamblerB1 += gambler_B(100)
        counter_gamblerB2 += gambler_B(10000)

    prob_of_win = counter_craps_win / 10000  # probability of winning a round of craps
    expected_gain_gamblerA1 = counter_gamblerA1 / 10000 # expected gain of gambler A for 1000 $
    expected_gain_gamblerA2 = counter_gamblerA2 / 10000 # expected gain of gambler A for 1000000 $
    expected_gain_gamblerB1 = counter_gamblerB1 / 10000 # expected gain of gambler B for 100 $
    expected_gain_gamblerB2 = counter_gamblerB2 / 10000 # expected gain of gambler B for 10000 $
    print("Probability of winning a round of craps = ", prob_of_win)
    print("Expected gain of gambler A for 1.000 $ =", expected_gain_gamblerA1)
    print("Expected gain of gambler A for 1.000.000 $ =", expected_gain_gamblerA2)
    print("Expected gain of gambler B for 100 $ =", expected_gain_gamblerB1)
    print("Expected gain of gambler B for 10000 $ =", expected_gain_gamblerB2)
    print("\n################################################################################### \n")


main()
