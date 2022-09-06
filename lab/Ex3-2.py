from sense_hat import SenseHat
sense = SenseHat()

#display first message

'''
sense.set_rotation(180)
sense.show_message("This is fun!", text_colour = (255,255,0),back_colour=(0,153,255), scroll_speed = 0.5)
'''


#ask for user input, display second message
print ("What color of text do you like?\n1.Blue\n2.Red\n3.Yellow")
color_msg_input = input("Enter your choice:")

#set text color
try:
    if int(color_msg_input) == 1:
        
        #blue text
        color_msg = (51,204,255)
        
    elif int(color_msg_input) == 2:
        
        #red text
        color_msg = (255,102,153)
        
    elif int(color_msg_input) == 3:
        
        #yellow text
        color_msg= (255,255,102)
        
    else:
        
        print ("You've entered a invalid choice, please only key in a number 1, 2 or 3.")
        color_msg_input = input("Enter your choice:")
        
except ValueError:
    
    print ("You've entered a invalid choice, please only key in a number 1, 2 or 3.")
    color_msg_input = input("Enter your choice:")
    
    
    
    
#ask for user input for bg color

print ("What color of background do you like?\n1.Blue\n2.Red\n3.Yellow")
color_bg_input = input("Enter your choice:")

#set text color
try:
    if int(color_bg_input) == 1:
        
        #blue text
        color_bg = (0,0,255)
        
    elif int(color_bg_input) == 2:
        
        #red text
        color_bg = (255,0,0)
        
    elif int(color_bg_input) == 3:
        
        #yellow text
        color_bg= (255,255,0)
        
    else:
        
        print ("You've entered a invalid choice, please only key in a number 1, 2 or 3.")
        color_bg_input = input("Enter your choice:")
        
except ValueError:
    
    print ("You've entered a invalid choice, please only key in a number 1, 2 or 3.")
    color_bg_input = input("Enter your choice:")
    


#ask user to enter scroll speed
speed_input = input("Enter scrolling speed (Please only enter a number):")

try:
    speed = float(speed_input)
    
except ValueError:
    
    print ("You've entered a invalid answer, please only key in a number.")
    speed_input = input("Enter scrolling speed (Please only enter a number):")
    


# display second message

sense.show_message("I got it!", text_colour = color_msg, \
                                back_colour = color_bg, \
                                scroll_speed = speed)
