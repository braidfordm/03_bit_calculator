# checks user choice is 'integer', 'text' or 'image'
def user_choice():

    valid = False
    while not valid:

        response = input("file type (integer / text / image): ").lower()

        if response == "text" or response == "t":
            return "text"

        else:
            print("please choose a valid file type!")
            print()


# Main routine goes here 
data_type = user_choice() 
print("You_chose",  data_type)

print()