def get_x_input():
    c = ord(input("Input value for x: "))

    while((c<(ord('A'))) | (c>(ord('P')))):
        print("Please input letter between 'A' and 'K'")
        c = ord(input("Input value for x: "))

    return c-65

def get_y_input():
    c = int(input("Input value for y: "))

    print(c)
    while((c<1) | (c>16)):
        print("Please input number between 1 and 16")
        c = int(input("Input value for y: "))

    return c-1
