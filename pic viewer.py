from tkinter import *
from PIL import ImageTk, Image
from styles import *

root = Tk()
root.title("images")
root.configure(bg=color_bg)
# root.geometry('1920x1080')
# root.state("zoomed")
# Changing Icon
root.iconbitmap('C:/Users/Arjit/Desktop/pythonProject/image code.ico')


# Adding any image type
img1 = ImageTk.PhotoImage(Image.open('images/1.png').resize((450, 350), Image.ANTIALIAS))
img2 = ImageTk.PhotoImage(Image.open('images/2.jpg').resize((450, 350), Image.ANTIALIAS))
img3 = ImageTk.PhotoImage(Image.open('images/3.jpg').resize((450, 350), Image.ANTIALIAS))
img4 = ImageTk.PhotoImage(Image.open('images/4.jpg').resize((450, 350), Image.ANTIALIAS))

img_l = [img1, img2, img3, img4]

status = Label(root, text="Image 1 of "+str(len(img_l)),
               bg=color_bg, fg=color_fg, bd=1,
               relief=SUNKEN, anchor=E, padx=20)

label = Label(image=img1)
label.grid(row=0, column=0, columnspan=3, padx=20, pady=20)


def fwd(ig_num):
    global label
    global btn_fwd
    global btn_back
    global status
    label.grid_forget()
    label = Label(image=img_l[ig_num - 1])
    btn_fwd = Button(root, text=">>", command=lambda: fwd(ig_num+1),
                     padx=40, pady=5, bg=color_bg, fg=color_fg)
    btn_back = Button(root, text="<<", command=lambda: back(ig_num-1), padx=40, pady=5, bg=color_bg, fg=color_fg)

    if ig_num == 4:
        btn_fwd = Button(root, text=">>", state=DISABLED, padx=40, pady=5, bg=color_bg, fg=color_fg)

    label.grid(row=0, column=0, columnspan=3, padx=20, pady=20)
    btn_fwd.grid(row=1, column=2)
    btn_back.grid(row=1, column=0)

    # Status Bar Update

    status = Label(root, text="Image " + str(ig_num) + " of " + str(len(img_l)), bg=color_bg, fg=color_fg, bd=1,
                   relief=SUNKEN, anchor=E, padx=20)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)
    pass


def back(ig_num):
    global label
    global btn_fwd
    global btn_back
    global status
    label.grid_forget()
    label = Label(image=img_l[ig_num - 1])
    btn_fwd = Button(root, text=">>", command=lambda: fwd(ig_num + 1), padx=40, pady=5, bg=color_bg, fg=color_fg)
    btn_back = Button(root, text="<<", command=lambda: back(ig_num - 1), padx=40, pady=5, bg=color_bg, fg=color_fg)

    if ig_num == 1:
        btn_back = Button(root, text="<<", state=DISABLED, padx=40, pady=5, bg=color_bg, fg=color_fg)

    label.grid(row=0, column=0, columnspan=3, padx=20, pady=20)
    btn_fwd.grid(row=1, column=2)
    btn_back.grid(row=1, column=0)

    # Status Bar Update

    status = Label(root, text="Image " + str(ig_num) + " of " + str(len(img_l)), bg=color_bg, fg=color_fg, bd=1,
                   relief=SUNKEN, anchor=E, padx=20)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)
    pass


btn_back = Button(root, text="<<", command=back, state=DISABLED, padx=40, pady=5, bg=color_bg, fg=color_fg)
btn_quit = Button(root, text="Exit", command=root.quit, padx=40, pady=5, bg=color_bg, fg=color_fg)
btn_fwd = Button(root, text=">>", command=lambda: fwd(2),  padx=40, pady=5, bg=color_bg, fg=color_fg)
btn_back.grid(row=1, column=0)
btn_quit.grid(row=1, column=1, pady=10)
btn_fwd.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3, sticky=W + E)

root.mainloop()
