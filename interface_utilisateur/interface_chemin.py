import tkinter as tk
from tkinter import filedialog

class ImageSelector:
    def __init__(self):
        self.root = tk.Tk()
        self.file_path = None

        self.root.title("Sélection d'une image")
        self.root.geometry("400x200")

        self.label = tk.Label(self.root, text="Veuillez sélectionner une image")
        self.label.pack(pady=20)

        self.button = tk.Button(self.root, text="Parcourir", command=self.open_file_dialog)
        self.button.pack()

    def open_file_dialog(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if self.file_path:
            print("Chemin d'accès de l'image sélectionnée :", self.file_path)
            self.root.destroy()

    def get_file_path(self):
        self.root.mainloop()
        return self.file_path

# Exemple d'utilisation
#image_selector = ImageSelector()
#file_path = image_selector.get_file_path()
#print("Chemin d'accès de l'image récupéré :", file_path)
