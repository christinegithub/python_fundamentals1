user_distance = 0

while True:
    print("Would you like to walk or run?")

    walk_or_run = input()

    if walk_or_run == 'walk':
        user_distance += 1
        print("Distance travelled is {}km".format(user_distance))

    elif walk_or_run == 'run':
        user_distance += 5
        print("Distance travelled is {}km".format(user_distance))

    else:
        print("Your response is invalid. Try again.")
