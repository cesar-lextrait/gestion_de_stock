import mysql.connector
import mysql.connector
import tkinter as tk
from tkinter import ttk
import graphical

def fetch_data():
    db = mysql.connector.connect(
        host="localhost",
        user="gestion_stock",
        password="abcde12345;ABCDE",
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
        afficher.geometry("1400x600")

        # Créer la frame pour la liste des produits
        treeview = ttk.Treeview(afficher, columns=(1, 2, 3, 4, 5), show="headings", height="6")
        treeview.pack(expand=True, fill="both")

        treeview.heading(1, text="ID")
        treeview.heading(2, text="Nom")
        treeview.heading(3, text="Description")
        treeview.heading(4, text="Prix")
        treeview.heading(5, text="Quantité")

        data = fetch_data()

        for row in data:
            treeview.insert("", tk.END, values=(row[0], row[1], row[2], row[3], row[4]))

        afficher.mainloop()

     


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
        btn_modif_prix = tk.Button(frame_btn, text="Modifier le prix", command=Modif.modif_prix, font=("Arial", 15), bg="white", fg="black", width=20, height=2)
        btn_modif_quantite = tk.Button(frame_btn, text="Modifier la quantité", command=Modif.modif_quantite, font=("Arial", 15), bg="white", fg="black", width=20, height=2)
        # Ajouter les boutons dans la frame
        btn_modif_prix.pack(expand=True, fill="both")
        btn_modif_quantite.pack(expand=True, fill="both")


    def modif_prix(): # Fonction pour modifier le prix
        afficher = tk.Toplevel()
        afficher.title("Modifier le prix")
        afficher.geometry("800x600")
        frame_liste = tk.Frame(afficher)
        frame_liste.pack(expand=True, fill="both")
        data = fetch_data()
        # Créer la frame pour la liste des produits
        treeview = ttk.Treeview(afficher, columns=(1, 2, 3, 4, 5), show="headings", height="6")
        treeview.pack(expand=True, fill="both")

        treeview.heading(1, text="ID")
        treeview.heading(2, text="Nom")
        treeview.heading(3, text="Description")
        treeview.heading(4, text="Prix")
        treeview.heading(5, text="Quantité")

        data = fetch_data()

        for row in data:
            treeview.insert("", tk.END, values=(row[0], row[1], row[2], row[3], row[4]))

        frame_input = tk.Frame(afficher)
        frame_input.pack(expand=True, fill="both")

        label_nouveau_prix = tk.Label(frame_input, text="Nouveau prix", font=("Arial", 15))
        label_nouveau_prix.pack(expand=True, fill="both")
        entry_nouveau_prix = tk.Entry(frame_input, font=("Arial", 15))
        entry_nouveau_prix.pack(expand=True, fill="both")

        label_id_produit = tk.Label(frame_input, text="ID du produit", font=("Arial", 15))
        label_id_produit.pack(expand=True, fill="both")
        id_produit = [row[0] for row in data]
        combobox_id_produit = ttk.Combobox(frame_input, values=id_produit, font=("Arial", 15))
        combobox_id_produit.pack(expand=True, fill="both")
        button_valider = tk.Button(frame_input, text="Valider", font=("Arial", 15), bg="blue", fg="black", width=20, height=2,
                       command=lambda: valider_modif_prix(entry_nouveau_prix.get(), combobox_id_produit.get()))
        button_valider.pack(expand=True, fill="both")
    

        def valider_modif_prix(nouveaux_prix, id_produit):
                db = mysql.connector.connect(
                    host="localhost",
                    user="gestion_stock",
                    password="abcde12345;ABCDE",
                    database="Boutique"
                )
                cur = db.cursor()
                sql = f"UPDATE produit SET prinx = {nouveaux_prix} WHERE id = {id_produit}"
                print(sql)
                cur.execute(sql)
                db.commit()
                db.close()
                afficher.destroy()




    def modif_quantite():
        afficher = tk.Toplevel()
        afficher.title("Modifier le prix")
        afficher.geometry("800x600")
        frame_liste = tk.Frame(afficher)
        frame_liste.pack(expand=True, fill="both")
        data = fetch_data()
        # Créer la frame pour la liste des produits
        treeview = ttk.Treeview(afficher, columns=(1, 2, 3, 4, 5), show="headings", height="6")
        treeview.pack(expand=True, fill="both")

        treeview.heading(1, text="ID")
        treeview.heading(2, text="Nom")
        treeview.heading(3, text="Description")
        treeview.heading(4, text="Prix")
        treeview.heading(5, text="Quantité")

        data = fetch_data()

        for row in data:
            treeview.insert("", tk.END, values=(row[0], row[1], row[2], row[3], row[4]))

        frame_input = tk.Frame(afficher)
        frame_input.pack(expand=True, fill="both")
        frame_input = tk.Frame(afficher)
        frame_input.pack(expand=True, fill="both")

        label_nouvelle_quantite = tk.Label(frame_input, text="Nouvelle quantité", font=("Arial", 15))
        label_nouvelle_quantite.pack(expand=True, fill="both")
        entry_nouvelle_quantite = tk.Entry(frame_input, font=("Arial", 15))
        entry_nouvelle_quantite.pack(expand=True, fill="both")

        label_id_produit = tk.Label(frame_input, text="ID du produit", font=("Arial", 15))
        label_id_produit.pack(expand=True, fill="both")
        id_produit = [row[0] for row in data]
        combobox_id_produit = ttk.Combobox(frame_input, values=id_produit, font=("Arial", 15))
        combobox_id_produit.pack(expand=True, fill="both")

        button_valider = tk.Button(frame_input, text="Valider", font=("Arial", 15), bg="blue", fg="black", width=20, height=2,
                           command=lambda: valider_modif_quantite(entry_nouvelle_quantite.get(), combobox_id_produit.get()))
        button_valider.pack(expand=True, fill="both")

        def valider_modif_quantite(nouvelle_quantite, id_produit):
                db = mysql.connector.connect(
                    host="localhost",
                    user="gestion_stock",
                    password="abcde12345;ABCDE",
                    database="Boutique"
                )
                cur = db.cursor()
                sql = f"UPDATE produit SET quantité = {nouvelle_quantite} WHERE id = {id_produit}"
                cur.execute(sql)
                db.commit()
                db.close()


class Ajouter:
    def ajouter_produit():
        ajout = tk.Toplevel()
        ajout.title("Ajouter un produit")
        ajout.geometry("800x600")

        label_nom = tk.Label(ajout, text="Nom", font=("Arial", 15))
        label_nom.pack(expand=True, fill="both")
        entry_nom = tk.Entry(ajout, font=("Arial", 15))
        entry_nom.pack(expand=True, fill="both")

        label_description = tk.Label(ajout, text="Description", font=("Arial", 15))
        label_description.pack(expand=True, fill="both")
        entry_description = tk.Entry(ajout, font=("Arial", 15))
        entry_description.pack(expand=True, fill="both")

        label_prix = tk.Label(ajout, text="Prix", font=("Arial", 15))
        label_prix.pack(expand=True, fill="both")
        entry_prix = tk.Entry(ajout, font=("Arial", 15))
        entry_prix.pack(expand=True, fill="both")

        label_quantite = tk.Label(ajout, text="Quantité", font=("Arial", 15))
        label_quantite.pack(expand=True, fill="both")
        entry_quantite = tk.Entry(ajout, font=("Arial", 15))
        entry_quantite.pack(expand=True, fill="both")

        label_categorie = tk.Label(ajout, text="Catégorie", font=("Arial", 15))
        label_categorie.pack(expand=True, fill="both")
        entry_categorie = tk.Entry(ajout, font=("Arial", 15))
        entry_categorie.pack(expand=True, fill="both")


        button_valider = tk.Button(ajout, text="Valider", font=("Arial", 15), bg="blue", fg="black", width=20, height=2,
                                    command=lambda: valider_ajout(entry_nom.get(), entry_prix.get(), entry_description.get(),  entry_quantite.get(), entry_categorie.get()))
        button_valider.pack(expand=True, fill="both")

        def valider_ajout(nom, prix, description, quantite, categorie):
            db = mysql.connector.connect(
                host="localhost",
                user="gestion_stock",
                password="abcde12345;ABCDE",
                database="Boutique"
            )
            cur = db.cursor()
            sql = f"INSERT INTO produit (nom, description, prinx, quantité, id_catégorie) SELECT '{nom}', \
            '{description}', {int(prix)}, {int(quantite)}, (SELECT id FROM categorie WHERE nom = '{categorie}')"
            cur.execute(sql)
            db.commit()
            db.close()
