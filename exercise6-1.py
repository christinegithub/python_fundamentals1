# Allow the user to go home when they are done exercising.
# The program should stop asking for input if the user enters 'go home'.
# See if you can also make the program tell the user when they have entered a command that does not exist.

user_distance = 0

print("Would you like to walk or run?")

walk_or_run = input()

if walk_or_run != 'go home':
    while walk_or_run != "go home":

        if walk_or_run == 'walk':
            user_distance += 1
            print("Distance from home is {}km".format(user_distance))
        elif walk_or_run == 'run':
            user_distance += 5
            print("Distance from home is {}km".format(user_distance))
        else:
            print("Your response is invalid.")
