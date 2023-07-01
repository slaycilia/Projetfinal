import tkinter as tk
from tkinter import filedialog

class ImageSelector:
    """Une classe pour sélectionner une image à partir d'une boîte de dialogue."""

    def __init__(self):
        """Initialise la fenêtre d'interface utilisateur pour la sélection d'une image."""
        self.root = tk.Tk()
        self.file_path = None

        self.root.title("Sélection d'une image")
        self.root.geometry("400x200")

        self.label = tk.Label(self.root, text="Veuillez sélectionner une image")
        self.label.pack(pady=20)

        self.button = tk.Button(self.root, text="Parcourir", command=self.open_file_dialog)
        self.button.pack()

    def open_file_dialog(self):
        """Ouvre une boîte de dialogue de sélection de fichier et enregistre le chemin d'accès du fichier sélectionné."""
        self.file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if self.file_path:
            print("Chemin d'accès de l'image sélectionnée :", self.file_path)
            self.root.destroy()

    def get_file_path(self):
        """
        Démarre la boucle principale de l'interface utilisateur et retourne le chemin d'accès du fichier sélectionné.

        Returns:
            str: Le chemin d'accès du fichier sélectionné.
        """
        self.root.mainloop()
        return self.file_path


# Exemple d'utilisation
#image_selector = ImageSelector()
#file_path = image_selector.get_file_path()
#print("Chemin d'accès de l'image récupéré :", file_path)
