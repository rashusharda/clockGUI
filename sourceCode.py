# importing libraries
from tkinter import Label, Tk 
import time

# defining title and size of the application
app_window = Tk() 
app_window.title("Digital Clock") 
app_window.geometry("420x150") 
app_window.resizable(1,1) #set both the height and width of the resizable function as True(1,1)

# defining the font of the time and its colour, its border width and background colour
text_font= ("Boulder", 68, 'bold')
background = "#bae1ff"
foreground= "#363529"
border_width = 25

# combine all the elements to define the label of clock application
label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)

# define the main function of the digital clock - set the text of the label as the realtime
def digital_clock(): 
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live) 
   label.after(200, digital_clock)

digital_clock()
app_window.mainloop()