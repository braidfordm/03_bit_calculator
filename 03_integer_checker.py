# checks input is a number more than given value
def num_check(question, low):
    valid = False
    while not valid:

        error = "Please enter a integer more than "
        "(or equal to) {}".format(low)

        try:

            # ask user to enter a number 
            response = float(input(question))
    
            # checks if number is more than zero
            if response > 0:
                return response
    
            # outputs error if input is invalid
            else:
                print(error)
                print()
        
        except ValueError:
           print(error)