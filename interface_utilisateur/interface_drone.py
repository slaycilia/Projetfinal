import tkinter as tk
from tkinter import ttk


class DonneesDrone:
    def __init__(self):
        """
        Classe pour saisir les informations du drone à l'aide de l'interface graphique Tkinter.

        La fenêtre Tkinter est créée avec les champs de saisie pour la masse, la hauteur,
        le diamètre et la vitesse du drone. Lorsque l'on clique sur le bouton "Valider",
        les informations sont récupérées et affichées.

        """
        self.window = tk.Tk()
        self.window.title("Saisie des informations du drone")
        self.style = ttk.Style(self.window)
        self.style.theme_use("clam")

        self.frame = ttk.Frame(self.window, padding=20)
        self.frame.grid(column=0, row=0, sticky="nsew")

        self.masse_label = ttk.Label(self.frame, text="Masse du drone (kg) :")
        self.masse_label.grid(column=0, row=0, padx=5, pady=5)
        self.masse_entry = ttk.Entry(self.frame)
        self.masse_entry.grid(column=1, row=0, padx=5, pady=5)

        self.hauteur_label = ttk.Label(self.frame, text="Hauteur du drone (m) :")
        self.hauteur_label.grid(column=0, row=1, padx=5, pady=5)
        self.hauteur_entry = ttk.Entry(self.frame)
        self.hauteur_entry.grid(column=1, row=1, padx=5, pady=5)

        self.diametre_label = ttk.Label(self.frame, text="Diamètre du drone (m) :")
        self.diametre_label.grid(column=0, row=2, padx=5, pady=5)
        self.diametre_entry = ttk.Entry(self.frame)
        self.diametre_entry.grid(column=1, row=2, padx=5, pady=5)

        self.vitesse_label = ttk.Label(self.frame, text="Vitesse du drone (m/s) :")
        self.vitesse_label.grid(column=0, row=3, padx=5, pady=5)
        self.vitesse_entry = ttk.Entry(self.frame)
        self.vitesse_entry.grid(column=1, row=3, padx=5, pady=5)

        self.button = ttk.Button(self.frame, text="Valider", command=self.get_drone_info)
        self.button.grid(column=0, row=4, columnspan=2, padx=5, pady=10)

        self.window.mainloop()

    def get_drone_info(self):
        """
        Récupère les informations saisies sur le drone.

        Les informations de masse, hauteur, diamètre et vitesse sont récupérées à partir des champs
        de saisie de l'interface graphique. Les valeurs sont converties en nombres à virgule flottante
        et stockées dans les attributs correspondants de l'instance de la classe.

        """
        self.masse = float(self.masse_entry.get())
        self.hauteur = float(self.hauteur_entry.get())
        self.diametre = float(self.diametre_entry.get())
        self.vitesse = float(self.vitesse_entry.get())

        self.window.destroy()

        # Affichage des informations saisies
        print("Informations du drone :")
        print("Masse :", self.masse, "kg")
        print("Hauteur :", self.hauteur, "m")
        print("Diamètre :", self.diametre, "m")
        print("Vitesse :", self.vitesse, "m/s")


'''Utilisation de la classe DroneInputApp
app = DonneesDrone()

# Accès aux informations saisies par l'utilisateur
masse = app.masse
hauteur = app.hauteur
diametre = app.diametre
vitesse = app.vitesse'''


