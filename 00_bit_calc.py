# Functions go here

# Put series of symbols at start and end of text ( for emphasis)
def statement_generator(text, decoration):

    # Make string with five characters
    ends = decoration * 5

    # add decoration to start and end statement 
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

# checks user choice is 'integer', 'text' or 'image'
def user_choice():

    #list of valid responses
    text_ok = ["text", "t", "txt"]
    integer_ok = ["integer", "int", "#", "number"]
    image_ok = ["image", "img", "pix", "picture", "pic","P"]

    valid = False
    while not valid:
        
        # ask user for choice and change response to lowercase
        response = input("file type (integer / text / image): ").lower()

        # Checks for valid response and returns text, integer or image

        if response in text_ok:
            return "text"

        elif response in integer_ok:
            return "integer"

        elif response in image_ok:
            return "image"

        elif response == "i":
            want_integer = input("Press <enter> for an integer or any other key for image: ")
            if want_integer == "":
                return "integer"
            else:
                return "image"


        else:
            print("please choose a valid file type!")
            print()



# Main routine goes here

# Heading 
statement_generator("Bit calculator for integers, text and images", "-")

# Display instructions if user has not used the program before

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    # Ask user for the file type 
    data_type = user_choice()
    print("You chose", data_type)
    
    # For integers, ask for integer
    # (must be an integer more than/ equal to 0)

    #For images, ask for width and height 