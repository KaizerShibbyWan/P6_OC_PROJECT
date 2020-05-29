# P6_OC_PROJECT
Participez à la vie de la communauté Open Source

# Secur_OS.py
Le programme "secur_os.py" a été conçu dans le but de sécuriser un serveur Linux .
Les logiciels sélectionnés pour la création des modules permettent de fournir un bon niveau de sécurité afin de se protéger des cyber-attaques fréquement rencontrées tel que :

*_les méthhodes de force brute

*_L'exploitation des failles logiciels 

*_Les spams

*_les rootkits et dénis de service

*_Les backdoors

## Getting Started

1- Installation et configuration des logiciels suivants :

*_Fail2ban

*_Logwatch

*_Cron-apt

*_Openssh-server

*_Rkhunter

2- Modification et chiffrement du mot de passe "root" 

3- Création d'un compte utilisateur "Administrateur"

4- Configuration des interfaces réseaux

### Prerequisites

L'utlisation du programme nécessite l'acquisition d'un système d'exploiation Linux

Le programme a été conçu avec la version 3.8 de Python

Le programme a été testé sur l'OS Debian 64bits 
 

## Installing & Using

1- Copiez les fichiers dans le répertoire de vore choix

2- Lancez le programme avec la commande suivante : "python secure_os.py config.yaml"

3- Vous pouvez appliquer vos propres paramètres en modifiant les valeurs du fichier "config.yaml"


## Running the tests

les modules ont été testés afin de vérifier la bonne application des paramètres fournis par le fchier congif.yaml

Vérification du bon fonctionnement des logiciels installés une fois les paramètres appliqués

Recherche et analyse des différentes exceptions levées par Python lors de l'utilisation des modules et du script secure_os.py

Optimisation des paramètres de configuration des logiciels , cependant comme indiqué dans la section précédente , leur modifiation est 
possible via le fichier "config.yaml" 


## Versioning

Version 1.0 > https://github.com/KaizerShibbyWan/P6_OC_PROJECT

## Authors

Jean - Samuel BOURGUIT 

Etudiant OpenClassrooms , parcours AIC (Administrateur Infrastuture et Cloud)

## License
    Apache License
    Version 2.0, January 2004
    http://www.apache.org/licenses/
https://www.apache.org/licenses/LICENSE-2.0.txt
