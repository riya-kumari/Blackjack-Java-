from tkinter import*
import PIL
from PIL import ImageTk
from PIL import Image


root = Tk()
root.title("test window")


frame = LabelFrame(root,text = "frame 1", padx=50, pady = 50)
frame.pack(padx=10, pady=10)
# frame2 = LabelFrame(root,text = "frame 2", padx = 5, pady = 5)

five = Button(frame, text = "red")
five_hundred = Button(frame, text = "purple")
hundred = Button(frame, text = "black")
one = Button(frame, text = "white")
twenty_five = Button(frame, text = "green")



# frame2.grid(row=1, column = 0)


five.grid( row = 0, column=0)
five_hundred.grid( row=0, column=1)
hundred.grid(row=0, column=2)
one.grid(row=0, column=3)
twenty_five.grid( row=0, column=4)


root.mainloop()



# window = Tk()

# im = Image.open("download.jpg")
# resized_im = im.resize((1000, 1000))

# # resized_im.save("resized.sample3.png")
# ph = ImageTk.PhotoImage(resized_im)
# label1 = Label(window, image = ph)
# label1.pack()

# window.mainloop()
# resized_im.show()




