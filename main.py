import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import image_detector as image_det
import video_detector as video_det
import sound
import os


flag = True

root = tk.Tk()
root.title('Color Detection')

canvas = tk.Canvas(root, width=600, height=500)
canvas.grid(columnspan=4, rowspan=6)

def open_image():
    image_text.set("Loading...")
    file = askopenfilename(title='Choose an image', initialdir='/', filetypes=[("jpg file", "*.jpg"), ("png file", "*.png"), ("jpeg file", "*.jpeg")])
    file = os.path.split(file)[-1]
    image_det.color_detector(file)
    image_text.set("Image Detection")


def open_video():
    if var1.get() == 0:
        video_text.set("Loading...")
        video_det.video_detector()
        video_text.set('Video Detection')
    elif var1.get() == 1:
        video_text.set("Loading...")
        sound.sound()
        video_text.set('Video Detection')
    
     

#logo
logo = Image.open('logotipo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instructions
ins = tk.Label(root, text = 'Select \"Image Detection\" if you want to detect colors from an image.\n\nSelect \"Video Detection\" if you want to detect colors from an live video.\n\n', anchor='w')
ins.grid(columnspan=3, column=0, row=1)

#image button
image_text = tk.StringVar()
image_btn = tk.Button(root, textvariable=image_text, command=lambda:open_image(), font='Raleway', bg='#20bebe', fg='white', height=2, width=15)
image_text.set('Image Detection')
image_btn.grid(column=1, row=3)

#video button
video_text = tk.StringVar()
video_btn = tk.Button(root, textvariable=video_text, command=lambda:open_video(), font='Raleway', bg='#20bebe', fg='white', height=2, width=15)
video_text.set('Video Detection')
video_btn.grid(column=1, row=4)



#sound check box
var1 = tk.IntVar()
sound_check = tk.Checkbutton(root, text='Video with Sound',variable=var1, onvalue=1, offvalue=0)
sound_check.grid(column=1, row=5)


canvas = tk.Canvas(root, width=600, height=50)
canvas.grid(columnspan=3)

root.mainloop()




