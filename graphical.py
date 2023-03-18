import mysql.connector
import tkinter as tk
from tkinter import ttk
from main import *
from PIL import Image, ImageTk


# Créer la fenêtre principale
root = tk.Tk()
root.title("Stock Librairie")
root.geometry("1200x700")

image = Image.open("/home/cezcew/Bureau/Ecole/gestion_de_stock/book.png")
image = image.resize((200, 200), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)

frame_photo = tk.Frame(root)
frame_photo.pack(side=tk.TOP, padx=10, pady=10)
label_photo = tk.Label(frame_photo, image=photo)
label_photo.pack()

# Créer les sous-frames pour les boutons de gauche et de droite
frame_left = tk.Frame(root)
frame_right = tk.Frame(root)
frame_left.pack(side=tk.LEFT, padx=10, pady=10)
frame_right.pack(side=tk.RIGHT, padx=10, pady=10)

frame_south =tk.Frame(root)
frame_south.pack(side=tk.TOP, padx=10, pady=20)
frame_south2 =tk.Frame(root)
frame_south2.pack(side=tk.TOP, padx=10, pady=20 )

# Créer les sous-frames pour chaque bouton
frame_add = tk.Frame(frame_left)
frame_modif = tk.Frame(frame_left)
frame_supp = tk.Frame(frame_right)
frame_afficher = tk.Frame(frame_right)
frame_categories = tk.Frame(frame_south)
frame_add_categories = tk.Frame(frame_south2)

# Ajouter les sous-frames dans la grille pour qu'elles soient bien rangées
frame_add.grid(row=0, column=0, padx=10, pady=10)
frame_modif.grid(row=1, column=0, padx=10, pady=10)
frame_supp.grid(row=0, column=0, padx=10, pady=10)
frame_afficher.grid(row=1, column=0, padx=10, pady=10)
frame_categories.grid(row=2, column=0, padx=10, pady=10)
frame_add_categories.grid(row=3, column=0, padx=10, pady=10)
# Créer les boutons et les ajouter dans les sous-frames correspondantes
btn_add = tk.Button(frame_add, text="Ajouter un produit", command=Ajouter.ajouter_produit, font=("Arial", 15), bg="white", fg="black", width=20, height=2)
btn_modif = tk.Button(frame_modif, text="Modifier un produit", command=Modif.modif_produits, font=("Arial", 15), bg="white", fg="black", width=20, height=2)
btn_supp = tk.Button(frame_supp, text="Supprimer un produit", command=Supprimer.supprimer_produit, font=("Arial", 15), bg="white", fg="black", width=20, height=2)
btn_afficher = tk.Button(frame_afficher, text="Afficher les produits", command=Afficher.afficher_produits, font=("Arial", 15), bg="white", fg="black", width=20, height=2)
btn_categories = tk.Button(frame_categories, text="Afficher les catégories",command=Afficher_Categorie.afficher_categorie, font=("Arial", 15), bg="white", fg="black", width=20, height=2)
btn_categories2 = tk.Button(frame_add_categories, text="Ajouter une catégorie",command=Ajouter_Categorie.ajouter_categorie, font=("Arial", 15), bg="white", fg="black", width=20, height=2)
# Ajouter les boutons dans les sous-frames correspondantes
btn_add.pack(expand=True, fill="both")
btn_modif.pack(expand=True, fill="both")
btn_supp.pack(expand=True, fill="both")
btn_afficher.pack(expand=True, fill="both")
btn_categories.pack(expand=True, fill="both")
btn_categories2.pack(expand=True, fill="both")





root.mainloop()