def get_x_input():
    c = ord(input("Input the column you'd like to hit: "))

    while((c<(ord('A'))) | (c>(ord('P')))):
        print("Please input letter between 'A' and 'P'!")
        c = ord(input("Input value for x: "))

    return c-65

def get_y_input():
    c = int(input("Input the row you'd like to hit: "))

    print(c)
    while((c<1) | (c>16)):
        print("Please input number between 1 and 16!")
        c = int(input("Input value for y: "))

    return c-1
