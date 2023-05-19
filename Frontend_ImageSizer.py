import tkinter as tk
from tkinter import filedialog
from PIL import Image,ImageTk
from tkinter import PhotoImage
filepath=None
def add_image():
    global filepath
    filepath=filedialog.askopenfilename(title="Select File",filetypes=(("Image Files","*.jpg;*.jpeg;*.png"),("All Files","*.*")))
    img=Image.open(filepath)
    img = img.resize((700,600), Image.ANTIALIAS)
    canvas.config(width=img.width,height=img.height)
    img = ImageTk.PhotoImage(img)
    canvas.image=img
    canvas.create_image(0,0, image=img, anchor="nw")

def resize_image():
    global filepath
    try:
        height = int(height_entry.get())
        width = int(width_entry.get())
        print("hello")
        print("Height is",height)
        if hasattr(canvas,"image"):
            canvas.image_path=filepath
            img = Image.open(canvas.image_path)
            img=img.resize((width,height),Image.ANTIALIAS)
            canvas.config(width=width,height=height)
            canvas.image=img
            photo_img = ImageTk.PhotoImage(img)
            canvas.create_image(0, 0, image=photo_img, anchor="nw")
            canvas.image_ref = photo_img
    except ValueError:
        pass


root=tk.Tk()
root.geometry("1000x600")
root.title("Plain Image Editor")
root.config(background="white")
canvas = tk.Canvas(root,background="Grey",width=700,height=600)
canvas.pack(side="right")

left_Frame=tk.Frame(root,background='Black',width=200,height=600)
left_Frame.pack(side="left",fill="both")


image_button=tk.Button(left_Frame,text="Add Image",bg="White",command=add_image)
image_button.pack(padx=5,pady=5)

height_label = tk.Label(left_Frame, text="Enter height: ")
height_label.pack(padx=5,pady=15)
height_entry = tk.Entry(left_Frame,width=5)
height_entry.pack()

width_label = tk.Label(left_Frame, text="Enter width: ")
width_label.pack(padx=5,pady=30)
width_entry = tk.Entry(left_Frame,width=5)
width_entry.pack()


Size_Change=tk.Button(left_Frame,text="Resize_Image",bg="White",
                      command=resize_image)
Size_Change.pack(padx=5,pady=40)



root.mainloop()

