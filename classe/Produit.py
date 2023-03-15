import mysql.connector

class CRUDproduit:
	def __init__(self):
		self.datab = mysql.connector.connect(
			host="localhost",
			user="root",
			password="root",
			database="boutique"
		)

	def Create(self, nom, description, prix, quantite, id_categorie):
		cur = self.datab.cursor()
		cur.execute(f"INSERT INTO produit (nom, description, prix, quantite, id_categorie) values ('{nom}', '{description}', {prix}, {quantite}, {id_categorie});")
		self.datab.commit()
		cur.close()

	def Read(self):
		cur = self.datab.cursor()
		cur.execute(f"SELECT * FROM produit;")
		res = cur.fetchall()
		for line in res:
			print(line)
		cur.close()

	def Update(self, nom, condition, nouveauNom):
		cur = self.datab.cursor()
		cur.execute(f"UPDATE produit set {nom} = '{nouveauNom}' WHERE {condition};")
		self.datab.commit()
		cur.close()

	def Delete(self, condition):
		cur = self.datab.cursor()
		cur.execute(f"DELETE FROM produit WHERE {condition};")
		self.datab.commit()
		cur.close()