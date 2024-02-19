






while True:
    want_instructions = input("Do you want to read instructions\n"). lower()

    if want_instructions == "yes" or want_instructions == "y":
        print("Good choice")

    elif want_instructions == "no" or want_instructions == "n":
        print ("Bad choice")

    else:
        print("You didnt Give a valid response buddy\n")

