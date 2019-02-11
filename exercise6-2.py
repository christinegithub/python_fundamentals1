# You started the day with energy, but you are going to get tired as you travel! Keep track of your energy.
# If you walk, your energy should increase.
# If you run, it should decrease. Moreover, you should not be able to run if your energy is zero.
# ...then, go crazy with it! Allow the user to rest and eat. Do whatever you think might be interesting.

energy = 10
user_distance = 0
walk_or_run = ''

while walk_or_run != 'go home':
    print("Would you like to walk or run?")

    walk_or_run = input()

    if walk_or_run == 'walk':
        user_distance += 1
        print("Distance travelled is {}km".format(user_distance))
        energy += 1
        print("Your energy level is {}cal".format(energy))

    elif walk_or_run == 'run' and energy > 0:
        user_distance += 5
        print("Distance travelled is {}km".format(user_distance))
        energy -= 5
        print("Your energy level is {}cal".format(energy))

    elif walk_or_run == 'run' and energy <= 0:
        print("You don't have enough energy to run. Try walking.")

    elif walk_or_run == 'go home':
        print("Heading home.")

    else:
        print("Your response is invalid. Try again.")
