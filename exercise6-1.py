# Allow the user to go home when they are done exercising.
# The program should stop asking for input if the user enters 'go home'.
# See if you can also make the program tell the user when they have entered a command that does not exist.

user_distance = 0
walk_or_run = ''

while walk_or_run != 'go home':
    print("Would you like to walk or run?")

    walk_or_run = input()

    if walk_or_run == 'walk':
        user_distance += 1
        print("Distance travelled is {}km".format(user_distance))

    elif walk_or_run == 'run':
        user_distance += 5
        print("Distance travelled is {}km".format(user_distance))

    elif walk_or_run == 'go home':
        print("Heading home.")

    else:
        print("Your response is invalid. Try again.")
