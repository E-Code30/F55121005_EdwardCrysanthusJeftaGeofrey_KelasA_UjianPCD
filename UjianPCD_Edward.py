import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps
import numpy as np
import cv2


class ImageProcessingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Processing App")

        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        file_menu = tk.Menu(menubar)
        file_menu.add_command(label="Open Image", command=self.open_image)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        tools_menu = tk.Menu(menubar)
        tools_menu.add_command(label="Histogram Equalization", command=self.histogram_equalization)
        tools_menu.add_command(label="Average Filter", command=self.average_filter)
        menubar.add_cascade(label="Tools", menu=tools_menu)

        self.status_bar = tk.Label(self.master, text="Image Processing App by Your Name", bd=1, relief=tk.SUNKEN,
                                   anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.image_label = tk.Label(self.frame)
        self.image_label.pack()

        self.image = None
        self.image_path = None

    def open_image(self):
        self.image_path = filedialog.askopenfilename()

        pil_image = Image.open(self.image_path)

        self.image = ImageTk.PhotoImage(pil_image)

        self.image_label.config(image=self.image)

        self.status_bar.config(text="Opened Image: " + self.image_path)

    def histogram_equalization(self):
        if self.image is not None:
            pil_image = Image.open(self.image_path)

            pil_image = ImageOps.equalize(pil_image)

            np_image = np.array(pil_image)

            pil_image = Image.fromarray(np_image)

            self.image = ImageTk.PhotoImage(pil_image)

            self.image_label.config(image=self.image)

            self.status_bar.config(text="Histogram Equalization Applied")

    def average_filter(self):
        if self.image is not None:
            pil_image = Image.open(self.image_path)

            np_image = np.array(pil_image)

            kernel = np.ones((3, 3), np.float32)
            kernel /= 9
            np_image = cv2.filter2D(np_image, -1, kernel)

            pil_image = Image.fromarray(np_image)

            self.image = ImageTk.PhotoImage(pil_image)

            self.image_label.config(image=self.image)

            self.status_bar.config(text="Average Filter Applied")
root = tk.Tk()
app = ImageProcessingApp(root)
root.mainloop()