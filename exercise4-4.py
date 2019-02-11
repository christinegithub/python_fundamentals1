# Pick a number and save it in a variable called secret_number. Ask the user to enter a number.
# If they enter the secret number, print "You win!". If they are off by 1, print "So close!".
# Otherwise, print "Try again".

secret_number = 13

print("Please enter a number.")

user_number = input()

number_diff = abs(secret_number - int(user_number))

if int(user_number) == secret_number:
    print("You win!")
elif number_diff == 1:
    print("So close!")
else:
    print("Try again")
