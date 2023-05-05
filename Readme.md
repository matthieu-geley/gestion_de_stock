# gestion_de_stock
## Projet réalisé dans le cadre de ma formation à la Plateforme_
Le but étant de développer un programme qui permet la gestion de stock d’un magasin en Python (POO) avec
une base de données MySQL utilisant un serveur SQL.

## Depuis un tableau de bord, créé à l'aide de la librairie graphique Tkinter, il est possible à l'utilisateur de:
- consulter la liste complète des produits en stock
- ajouter un produit
- supprimer un produit
- modifier un produit (son prix, son nom, sa quantité, ...)


Pour ajouter un élément:

il faut renseigner un nom, une description, un prix, une quantité et une catégorie;

Pour supprimer un élément il faut indiquer son id;

Pour modifier un élément:
il faut renseigner un nom, une description, un prix, une quantité, une catégorie
ET se servir de l'id à supprimer comme condition de remplacement.

Pour afficher la liste d'élément en stock, il faut appuyer sur le bouton correspondant.
Cette liste est mise à jour à chaque fois qu'elle est appelée.
