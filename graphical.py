import mysql.connector
import tkinter as tk
from tkinter import ttk
from main import *


# Créer la fenêtre principale
root = tk.Tk()
root.title("Gestion de stock")
root.geometry("600x400")

# Créer les sous-frames pour les boutons de gauche et de droite
frame_left = tk.Frame(root)
frame_right = tk.Frame(root)
frame_left.pack(side=tk.LEFT, padx=10, pady=10)
frame_right.pack(side=tk.RIGHT, padx=10, pady=10)

# Créer les sous-frames pour chaque bouton
frame_add = tk.Frame(frame_left)
frame_modif = tk.Frame(frame_left)
frame_supp = tk.Frame(frame_right)
frame_afficher = tk.Frame(frame_right)

# Ajouter les sous-frames dans la grille pour qu'elles soient bien rangées
frame_add.grid(row=0, column=0, padx=10, pady=10)
frame_modif.grid(row=1, column=0, padx=10, pady=10)
frame_supp.grid(row=0, column=0, padx=10, pady=10)
frame_afficher.grid(row=1, column=0, padx=10, pady=10)

# Créer les boutons et les ajouter dans les sous-frames correspondantes
btn_add = tk.Button(frame_add, text="Ajouter un produit",  font=("Arial", 15), bg="white", fg="black", width=20, height=2)
btn_modif = tk.Button(frame_modif, text="Modifier un produit", command=Modif.modif_produits, font=("Arial", 15), bg="white", fg="black", width=20, height=2)
btn_supp = tk.Button(frame_supp, text="Supprimer un produit", font=("Arial", 15), bg="white", fg="black", width=20, height=2)
btn_afficher = tk.Button(frame_afficher, text="Afficher les produits", command=Afficher.afficher_produits, font=("Arial", 15), bg="white", fg="black", width=20, height=2)

# Ajouter les boutons dans les sous-frames correspondantes
btn_add.pack(expand=True, fill="both")
btn_modif.pack(expand=True, fill="both")
btn_supp.pack(expand=True, fill="both")
btn_afficher.pack(expand=True, fill="both")





root.mainloop()