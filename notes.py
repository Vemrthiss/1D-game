from tkinter import *

# instantiates tkinter window/root widget
root = Tk()

# ----------------------BASICS----------------------------
# #creating a label widget, then shoving it (pack) onto the GUI
# my_label = Label(root, text="Hello World!") #first arg mounts it to the root widget, second text arg sets text
# my_label.pack() #very primitive way of inserting widgets into GUI, and disregards the grid system available



#------------------------GRID SYSTEM-----------------------
# # instantiation of Labels
# my_label_2 = Label(root, text="My name is Joel")
# my_label_3 = Label(root, text=" HI")


# # grid system is 0-indexed
# # grid values are relative, i.e. 2 elements with columns 0 and 5 is the same as column 0 and 1
# # mounting of labels
# my_label.grid(row=0, column=0) 
# my_label_2.grid(row=2, column=5)
# my_label_3.grid(row=1, column=1)


# # one-liner for the above actions (instantiation+mounting)
# # might not be as clean as separating instantiation and mounting
# my_label_4 = Label(root, text="This is a one-liner").grid(row=3, column=2)



# -------------------------CREATING BUTTONS------------------
# a click event listener
def handleClick():
    print('the button was clicked!')
    

# possible kwargs for the Button class constructor
# if hardcording kwarg value, use string with quotation marks,
# if assigning pre-defined variables to the kwarg, no quotation marks
# 1) state=DISABLED will cause the btn to be disabled on mount
# 2) padx=value or pady=value will give the buttons x/y padding resp. (prob in pixels)
# 3) command=fn will cause the function fn to execute upon click
# 4) bg=colour sets the background to be colour (to be a string like CSS 'blue' or a single string of hexadecimals)
# 5) fg=colour sets the foreground (btn text) of btn to be colour
my_button = Button(root, text="Click me!", padx=50, pady=10, command=handleClick, bg="yellow", fg="blue")
my_button.grid(row=0, column=0)


# enter the main loop
# this is necessary as for GUIs to remain open and track user action, a loop must occur
# closing the GUI window will end this main loop
root.mainloop()