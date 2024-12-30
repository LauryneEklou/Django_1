# Django_1
# mon premier crud avec django
Commande pour créer le projet :
django-admin startproject crudproject1

Ensuite, nous avons fait :
`python manage.py startapp enroll`
pour créer une nouvelle application au sein du projet.

Création d'un superutilisateur avec la commande: `python manage.py createsuperuser`

Nous avons créé un dossier static pour notre code CSS et JS, dans lequel nous avons copié les fichiers CSS et JS de Bootstrap.

Un dossier templates contient des fichiers HTML pour l'affichage du formulaire et la mise à jour.

Ensuite, nous avons créé un fichier statique nommé base.html qui appelle les fichiers CSS et JS :
`{% load static %}`
Cela permet de dire que le fichier est statique.

Le fichier addandshow.html hérite de base.html.
`{% block content %}` : Lorsqu’un fichier enfant hérite d’un fichier parent avec `{% extends 'base.html' %}`, il peut redéfinir ou ajouter du contenu dans la zone `{% block content %}`. C’est avec ce fichier et le fichier forms.py que nous avons créé le formulaire d'ajout.

Le fichier views.py contient la méthode pour l'ajout.

La route est configurée dans urls.py comme ceci :
`path('', views.add_show, name="addandshow")`.
