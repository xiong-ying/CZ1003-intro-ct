from sense_hat import SenseHat
sense= SenseHat()
sense.set_rotation(180)

#---function get_color() ---

def get_color(color):
    
    keep_looping = True
    no_of_try = 1
    
    while keep_looping:
        
        if no_of_try <= 3:
            
            color_str = input("Enter the value of the " + color + " color for message (0 to 255):")
            print(color_str)
            
            try:
                if 0 <= int(color_str) <=255 :
                    
                    if color == "red":
                        color_code = int(color_str)
                    elif color == "green":
                        color_code = int(color_str)
                    elif color == "blue":
                        color_code = int(color_str)
                    else:
                        print("Input Error")
                    
                    return color_code
                    
                else:
                    print("Invalid input range, please try again!")
                    no_of_try += 1
            
            except ValueError:
                print("Invalid input range, please try again!")
                no_of_try += 1
        
        else:
            print("You have reached maximum 3 times of try.")
            color_code = 0
            keep_looping = False
            
            return color_code
            
        
# ---
if __name__ == '__main__':
    r_int = get_color("red")
    g_int = get_color("green")
    b_int = get_color("blue")
    msg_color = (r_int, g_int, b_int)
    sense.show_message("I got it!", text_colour = msg_color)