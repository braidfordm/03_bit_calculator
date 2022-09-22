# checks user choice is 'integer', 'text' or 'image'
def user_choice():

    #list of valid responses
    text_ok = ["text", "t", "txt"]
    integer_ok = ["integer", "int", "#", "number"]
    image_ok = ["image", "img", "pix", "picture", "pic"]
    
    valid = False
    while not valid:
        
        # ask user for choice and change response to lowercase
        response = input("file type (integer / text / image): ").lower()
       
        # If they choose "t" or "text", return text
        text_ok = ["text", "t", "txt"]
        if response in text_ok:
            return "text"

        else:
            print("please choose a valid file type!")
            print()


# Main routine goes here
keep_going = ""
while keep_going == "": 
    data_type = user_choice() 
    print("You_chose",  data_type)

    print()