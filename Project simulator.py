import tkinter as tk
from PIL import Image,ImageTk       #The ImageTk module contains support to create and modify Tkinter BitmapImage and PhotoImage objects
# PIL-  PIL images and filedialog is used for the dialog box to appear when you are opening file from anywhere in your system or saving your file in a particular position or place.

import random    #Random library is used to genearte a number in the given data or function

window=tk.Tk()    #tk is an instance of tkinter frame. It helps to display the root window and manages all the other components of the tkinter application.
window.title("Dice Simulator")
window.geometry("500x360")    #used for giving the dimension of the window inside the thikter lib


dice=["dice-six-faces-one.png","dice-six-faces-two.png","dice-six-faces-three.png","dice-six-faces-four.png","dice-six-faces-five.png","dice-six-faces-six.png"]   #importing all the images in the tkinter window
image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))    #This opens the image in the GUI window
image2=ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1=tk.Label(window,image=image1)          #Label()- It is used to display one line or more than one line of text.
label2=tk.Label(window,image=image2)

label1.image=image1                 #connecting labels to image for the random result
label2.image=image2

label1.place(x=150,y=100)             #place()-It is used to set the position.Placing the images in correct x and y axis 
label2.place(x=900,y=100)

def dice_roll():
    image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))         
    label1.configure(image=image1)           #label.configure-This method gives the text or image output in the label dynamically.
    label1.image=image1

    image2=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image=image2)
    label2.image=image2
    
button=tk.Button(window,text="ROLL",bg="black",fg="white",font="Times 20 bold",command=dice_roll)     #Button()-It is a button used to display on our window.
#bg-It is the background colour,fg-It is the colour of letters in text,font-increase or decrease the font size 
button.place(x=750,y=0)           #Placing the button in correct x and y axis
window.mainloop()                  #It is simply a method in the main window that executes what we wish to execute in an application and ends the mainloop.



#Taking reference from - https://pythonflood.com/python-project-dice-rolling-simulator-f5acc0cd64de
