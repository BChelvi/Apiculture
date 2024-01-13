# TP Django Apiculture Benjamin Chelvi-Sandin

## Dependencies
For this project, the following file has to list the python dependencies of your project.
- **requirements.in** set your app dependencies here and set version requirements if needed.


## About environment
The file named **.env-template** list the required environnement variables that your project need, but **does not** contains any citical informations such as credentials. It can contains **example values**. It's purpose is to show how to build the **.env** file.

The **.env** needs to be listed in the **.gitignore**, it's **not versionned**, it's **only in your system**.


***
## Configuration
List here the steps to follow to run the application.
- You need to have access to a PostgresQL database
- Create a virtual environment
- Install the dependencies from requirements.txt
- Create you .env file based on .env-template

## How to use
Run the following command to launch the Django server :
- `delete previous migrations present on the GitHubRepository`!!!
- `python manage.py migrate`
- `python manage.py createsuperuser`
- `python manage.py runserver`
- `watch the navigator`
- `connect as a superuser in the admin pannel`


## Project Status

## Beekeeper
• Lister leurs différents cheptels
• Par cheptel, lister les ruches
• Par ruche, est-ce qu'elle est en activité, en attente ou détruite, depuis quelle 
date. L'âge de la reine, le type d'abeilles. Date et quantité des récoltes. Est-ce 
que la ruche est contaminé. Si oui depuis quelle date et par quelle 
maladie/parasite.
• Avoir un suivi des interventions, ajouter leur nature et les typer :
    o Suppression des cellules royales
    o Check de santé
    o Récolte
    o Distribution de sirop
    o Pose de hausses
    o Destruction
    o Multiplication artificielle de l'essaim
    o Traitement (apivar, acide oxalique, antifongique, …)
    • Possibilité de filtrer les résultats

• Possibilité d'effectuer une action sur toutes les ruches d'un cheptel en même 
temps (not done)

## Visitor

• Les données suivantes doivent être disponibles sont en lecture seule
    o Apiculteurs (nom, prénom et un contact)
    o Cheptels
    o Ruches
• Pagination
• Possibilité de filtrer les résultats

