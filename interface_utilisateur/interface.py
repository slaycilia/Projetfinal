#On demande à l'utilisateur combien de points de repère il souhaite avoir
import tkinter as tk
from tkinter import ttk


class InterfaceUtilisateur:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Saisie du nombre de points")
        self.style = ttk.Style(self.window)
        self.style.theme_use("clam")

        self.frame = ttk.Frame(self.window, padding=20)
        self.frame.grid(column=0, row=0, sticky="nsew")

        self.label = ttk.Label(self.frame, text="Nombre de points :")
        self.label.grid(column=0, row=0, padx=5, pady=5)
        self.entry = ttk.Entry(self.frame)
        self.entry.grid(column=1, row=0, padx=5, pady=5)

        self.button = ttk.Button(self.frame, text="Valider", command=self.saisir_points)
        self.button.grid(column=0, row=1, columnspan=2, padx=5, pady=10)

        self.window.mainloop()

    def saisir_points(self):
        nombre_points = int(self.entry.get())
        self.points = []

        def memoriser_points():
            for i in range(nombre_points):
                x = float(entrees[i][0].get())
                y = float(entrees[i][1].get())
                self.points.append((x, y))

            self.window_points.destroy()
            self.window.destroy()

        self.window_points = tk.Tk()
        self.window_points.title("Saisie des coordonnées des points")
        self.style = ttk.Style(self.window_points)
        self.style.theme_use("clam")

        self.frame = ttk.Frame(self.window_points, padding=20)
        self.frame.grid(column=0, row=0, sticky="nsew")

        entrees = []

        for i in range(nombre_points):
            subframe = ttk.Frame(self.frame, padding=5)
            subframe.grid(column=0, row=i, pady=5)

            x_label = ttk.Label(subframe, text=f"Point {i + 1} - Coordonnée x :")
            x_label.grid(column=0, row=0, sticky="w")
            x_entry = ttk.Entry(subframe)
            x_entry.grid(column=1, row=0, padx=5)

            y_label = ttk.Label(subframe, text=f"Coordonnée y :")
            y_label.grid(column=2, row=0, padx=10, sticky="w")
            y_entry = ttk.Entry(subframe)
            y_entry.grid(column=3, row=0, padx=5)

            entrees.append((x_entry, y_entry))

        save_button = ttk.Button(self.frame, text="Enregistrer", command=memoriser_points)
        save_button.grid(column=0, row=nombre_points, columnspan=4, pady=10)

        self.window_points.mainloop()

# Utilisation de la classe InterfaceUtilisateur
#app = InterfaceUtilisateur()
#points_list = app.points
#print("Liste des points de passage :", points_list)