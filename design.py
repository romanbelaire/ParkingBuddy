from Tkinter import *
from PIL import ImageTk, Image
root = Tk()

root.title('Parking Buddy')
root.geometry("600x500")

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

canv = Canvas(topFrame, width=500, height=300, bg='white')
canv.grid(row=2, column=3)

textBox = Text(bottomFrame, height = 2, width = 10)
textBox.pack()

img = ImageTk.PhotoImage(Image.open("/Users/mariannetolentino/Desktop/cpsc440/cars-driving.jpg"))  # PIL solution
canv.create_image(20, 20, anchor=NW, image=img)

mainloop()
