from PIL import Image, ImageTk, ImageDraw
import numpy as np
import tkinter as tk
import AI

model = AI.load_ai()

window = tk.Tk()

img = Image.new(mode="1", size=(300, 300), color=0)
tkimg = ImageTk.PhotoImage(img)
canvas = tk.Label(window, image=tkimg)
canvas.pack()

pen = ImageDraw.Draw(img)

last_point = (0, 0)

teks = tk.StringVar()
label = tk.Label(window, textvariable=teks)

def draw_img(event):
    global last_point, tkimg
    current_point = (event.x, event.y)
    pen.line([last_point, current_point], fill=255, width=15)
    last_point = current_point
    tkimg = ImageTk.PhotoImage(img)
    canvas['image'] = tkimg
    canvas.pack()
    img_temp = img.resize((28, 28))
    img_temp = np.array(img_temp)
    img_temp = img_temp.flatten()
    output = model.predict([img_temp])
    if(output[0] == 0):
        teks.set("kotak")
    elif(output[0] == 1):
        teks.set("lingkaran")
    elif(output[0] == 2):
        teks.set("segitiga")
    elif(output[0] == 3):
        teks.set("centang")
    elif(output[0] == 4):
        teks.set("silang")
    else:
        teks.set("ERROR")
    label.pack()

def start_draw(event):
    global last_point
    last_point = (event.x, event.y)

def reset_canvas(event):
    global tkimg, img, pen
    img = Image.new(mode="1", size=(300, 300), color=0)
    pen = ImageDraw.Draw(img)
    tkimg = ImageTk.PhotoImage(img)
    canvas['image'] = tkimg
    canvas.pack()

kotak = 0
segitiga = 0
lingkaran = 0
centang = 0
silang = 0

def save_img(event):
    global kotak, lingkaran, segitiga, centang, silang, teks
    img_temp = img.resize((28, 28))
    if(event.char == "k"):
        img_temp.save(f"kotak/{kotak}.png")
        kotak += 1
    elif(event.char == "s"):
        img_temp.save(f"segitiga/{segitiga}.png")
        segitiga += 1
    elif(event.char == "l"):
        img_temp.save(f"lingkaran/{lingkaran}.png")
        lingkaran += 1
    elif(event.char == "c"):
        img_temp.save(f"centang/{centang}.png")
        centang += 1
    elif(event.char == "i"):
        img_temp.save(f"silang/{silang}.png")
        silang += 1


window.bind("<B1-Motion>", draw_img)
window.bind("<ButtonPress-1>", start_draw)
window.bind("<ButtonPress-3>", reset_canvas)
window.bind("<Key>", save_img)

label.pack()

window.mainloop()