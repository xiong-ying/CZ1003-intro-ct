from sense_hat import SenseHat
sense = SenseHat()

#display first message

'''
sense.set_rotation(180)
sense.show_message("This is fun!", text_colour = (255,255,0),back_colour=(0,153,255), scroll_speed = 0.5)
'''


#function to ask for user input, display second message
text_r = input("Enter the value of the red color for message:")
text_g = input("Enter the value of the green color for message:")
text_b = input("Enter the value of the blue color for message:")


#set text color
while True:
    try:

        if 0 <= int(text_r) <= 256 and  0 <= int(text_g) <= 256  and  0 <= int(text_b) <= 256 :
            color_msg = (int(text_r),int(text_g),int(text_b))
            break
        
        else:
        
            print ("You've entered a invalid number, please only key in a number between 0 to 255")
            text_r = input("Enter the value of the red color for message:")
            text_g = input("Enter the value of the green color for message:")
            text_b = input("Enter the value of the blue color for message:")
        
    except ValueError:
    
        print ("You've entered a invalid date type, please only key in a number between 0 to 255")
        text_r = input("Enter the value of the red color for message:")
        text_g = input("Enter the value of the green color for message:")
        text_b = input("Enter the value of the blue color for message:")
    
    
    
    
#ask for user input for bg color

print ("What color of background do you like?\n1.Blue\n2.Red\n3.Yellow")
color_bg_input = input("Enter your choice:")

#set text color
while True:
    try:

        if int(color_bg_input) == 1:
        
            #blue text
            color_bg = (0,0,255)
            break
        
        elif int(color_bg_input) == 2:
        
            #red text
            color_bg = (255,0,0)
            break
        
        elif int(color_bg_input) == 3:
        
            #yellow text
            color_bg= (255,255,0)
            break
        
        else:
        
            print ("You've entered a invalid choice, please only key in a number 1, 2 or 3.")
            color_bg_input = input("Enter your choice:")
        
    except ValueError:
    
        print ("You've entered a invalid choice, please only key in a number 1, 2 or 3.")
        color_bg_input = input("Enter your choice:")




#ask user to enter scroll speed
speed_input = input("Enter scrolling speed (Please only enter a number):")

while True:
    
    try:
        speed = float(speed_input)
        break
    
    except ValueError:
    
        print ("You've entered a invalid answer, please only key in a number.")
        speed_input = input("Enter scrolling speed (Please only enter a number):")
    


# display second message

print(color_msg)
print(color_bg)
print(speed)

sense.show_message("I got it!", text_colour = color_msg, \
                                back_colour = color_bg, \
                                scroll_speed = speed)

