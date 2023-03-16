import mysql.connector
import sys
sys.path.append('./classe')
from classe.Categorie import *
from classe.Produit import *
import tkinter as tk
from tkinter import *


#Ouverture de la base de Données
datab = mysql.connector.connect(
			host="localhost",
			user="root",
			password="root",
			database="boutique"
		)



#Fenêtre principale
win = Tk()
win.title('Gestionnaire de Stock')
win.configure(bg =  "grey")
window_width = 1024
window_height = 600
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

def b_ajout():
	ajout = Toplevel()
	ajout.title('Ajouter un produit')
	ajout.configure(bg="grey")
	ajout.geometry('400x400')


	addnom = Entry(ajout)
	addnom.insert(0, "Nom")
	addnom.pack()

	adddesc = Entry(ajout)
	adddesc.insert(0, "Description")
	adddesc.pack()

	addprix = Entry(ajout)
	addprix.insert(0, "Prix")
	addprix.pack()

	addqty = Entry(ajout)
	addqty.insert(0, "Quantité")
	addqty.pack()

	addid_cat = Entry(ajout)
	addid_cat.insert(0, "Categorie")
	addid_cat.pack()

	nom = addnom.get()
	description = adddesc.get()
	prix = addprix.get()
	quantite = addqty.get()
	id_cat = addid_cat.get()

	cur = datab.cursor()

	cur.execute(f"INSERT INTO produit (nom, description, prix, quantite, id_categorie) values ('{nom}', '{description}', {prix}, {quantite}, {id_cat});")
	datab.commit()
	cur.close()


	bouton_soumettre = Button(ajout, text = "Ajouter le produit au stock", command = addProduct).pack()


def b_modif():
	modif = Toplevel()
	modif.title('Modifier un produit')
	modif.configure(bg="grey")
	modif.geometry("400x400")
	bouton_soumettre = Button(modif, text =  "Modifier le produit", command = "").pack()

def b_suppr():
	suppr = Toplevel()
	suppr.title('Supprimer un produit')
	suppr.configure(bg="grey")
	suppr.geometry("400x400")
	bouton_soumettre = Button(suppr, text ='Soumettre' ).pack()


bouton_ajout = Button(win, text = "Ajouter un produit", command = b_ajout).grid(row = 3, column = 0)
bouton_modif = Button(win, text = "Modifier un produit", command = b_modif).grid(row = 3, column = 1)
bouton_suppr = Button(win, text = "Supprimer un produit", command = b_suppr).grid(row = 3, column = 2)


win.mainloop()
#tk.Label(win, text='CRUD des Produits', bg = 'grey').pack()

# a = Entry(win, width = 15)
# a.pack()