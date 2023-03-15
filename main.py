import mysql.connector
import mysql.connector
import tkinter as tk
from tkinter import ttk
import graphical

def fetch_data():
    db = mysql.connector.connect(
        host="localhost",
        user="gestion_stock",
        password="*********",
        database="Boutique"
    )
    cur = db.cursor()
    sql = "SELECT * FROM produit"
    print(sql)
    cur.execute(sql)
    result = cur.fetchall()
    return result

class Afficher:
    def afficher_produits():
        # Créer la fenêtre pour afficher les produits
        afficher = tk.Toplevel()
        afficher.title("Afficher les produits")
        afficher.geometry("800x600")

        # Créer la frame pour la liste des produits
        frame_liste = tk.Frame(afficher)
        frame_liste.pack(expand=True, fill="both")

        # Récupérer les données depuis la base de données
        data = fetch_data()

        # Créer la liste des produits
        listbox = tk.Listbox(frame_liste, font=("Arial", 15))
        for row in data:
            listbox.insert(tk.END, f"{row[0]} - {row[1]} - {row[2]} - {row[3]} - {row[4]}")

        listbox.pack(expand=True, fill="both")


class Modif:
    def modif_produits():
        # Créer la fenêtre pour modifier les produits
        modif = tk.Toplevel()
        modif.title("Modifier les produits")
        modif.geometry("800x600")

        # Créer la frame pour la liste des produits
        frame_liste = tk.Frame(modif)
        frame_liste.pack(expand=True, fill="both")

        # Créer la frame pour les boutons
        frame_btn = tk.Frame(modif)
        frame_btn.pack(expand=True, fill="both")


        # Créer les boutons
        btn_modif_prix = tk.Button(modif, text="Modifier le prix", command=Modif.modif_prix, font=("Arial", 15), bg="white", fg="black", width=20, height=2)
        btn_modif_quantite = tk.Button(modif, text="Modifier la quantité", command=Modif.modif_quantite, font=("Arial", 15), bg="white", fg="black", width=20, height=2)

        # Ajouter les boutons dans la frame
        btn_modif_prix.pack(expand=True, fill="both")
        btn_modif_quantite.pack(expand=True, fill="both")


    def modif_prix(id, nouveau_prix):
        afficher = tk.Toplevel()
        afficher.title("Modifier le prix")
        afficher.geometry("800x600")
        frame_liste = tk.Frame(afficher)
        frame_liste.pack(expand=True, fill="both")
        cur = data.cursor()
        cur.execute("UPDATE produit SET prinx = %s, quantité = %s WHERE id = %s", (nouveau_prix, id))
        data.commit()
        data.close()
        data = fetch_data()
        listbox = tk.Listbox(frame_liste, font=("Arial", 15))
        for row in data:
            listbox.insert(tk.END, f"{row[0]} - {row[1]} - {row[2]} - {row[3]} - {row[4]}")
        listbox.pack(expand=True, fill="both")


    def modif_quantite(id, nouvelle_quantite):
        afficher = tk.Toplevel()
