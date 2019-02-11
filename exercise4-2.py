# Ask the user to enter their age, and then display a message telling them how many years apart in age
# you are from them. If they enter a number larger than 105, print "I'm not sure I believe you".

print("How old are you?")

user_age = input()
my_age = 50

age_difference = abs(my_age - int(user_age))

print("We are {} years apart.".format(age_difference))

if int(user_age) > 105:
    print("I'm not sure I believe you")
