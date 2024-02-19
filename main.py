# check users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question). lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("You didnt Give a valid response buddy\n")



# Main routine
while True:
    want_instructions = yes_no("Do you want instructions\n")
    print(f"You chose {want_instructions}\n")
    print("I like to kiss little boys and touch their bums")
 
