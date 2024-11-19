import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from image_processing import *

class ImageProcessingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Processing App")
        self.image = None

        self.upload_button = tk.Button(master, text="Upload Image", command=self.upload_image)
        self.upload_button.pack()

        self.process_button = tk.Button(master, text="Process Image", command=self.process_image)
        self.process_button.pack()

        self.canvas = tk.Canvas(master, width=500, height=500)
        self.canvas.pack()

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            self.display_image(self.image)

    def process_image(self):
        if self.image is not None:
            processed_image = linear_contrast(self.image)  # Пример: линейное контрастирование
            self.display_image(processed_image)
        else:
            messagebox.showwarning("Warning", "Please upload an image first.")

    def display_image(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        img = Image.fromarray(img)
        img = img.resize((500, 500), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
        self.canvas.image = img_tk  # Сохранение ссылки на изображение

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessingApp(root)
    root.mainloop()