def get_x_input():    
    appropriate_input = False
    
    while (appropriate_input == False):
        appropriate_input = True
        x_input = input("\nInput the column you'd like to hit: ")
        
        if (len(x_input) != 1):
            print("Please input a single character..")
            appropriate_input = False
        else:
            if ((ord(x_input) < (ord('A'))) | (ord(x_input) > (ord('P')))):
                print("Please input letter between 'A' and 'P'!")
                appropriate_input = False
            

    return ord(x_input) - 65

def get_y_input():
    c = int(input("\nInput the row you'd like to hit: "))

    print(c)
    while((c<1) | (c>16)):
        print("Please input number between 1 and 16!")
        c = int(input("Input value for y: "))

    return c-1
