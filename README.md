# polycarnet

## Introduction

*Polycarnet* est un programme permettant de générer facilement le carnet de suivi demandé en DII à l’école Polytech Tours.

*NOTE :* Si vous ne modifiez pas le paramétrage, vous pouvez directement passer à la partie *Importation dans Word*.

## Paquets nécessaires

Pour utiliser le programme, il vous faut Python 3 et un navigateur web

## Paramétrage

Pour paramétrer le générateur de carnet de suivi, il faut modifier le fichier `cste.py`.

Dans ce fichier est présent la déclaration d'un élément json `assocValue`. C'est dans ce json que les matières sont définies avec le champ *name*. Vous avez à modifier pour chaque matières :

1. Les notions étudié pendant le cours *notions*
2. Le niveau que vous avez *niveau*
3. Le commentaire que vous souhaiter ajouter *comm*


## Génération du carnet de suivi

Pour la génération du carnet de suivi, il suffit d’exécuter le script python `readInfos.py`.

Le fichier sera généré dans le dossier data.


## Importation dans Word

Pour importer vos semaines dans word, il faut ouvrir le fichier `index.html` avec votre navigateur internet.

Vous aurez ainsi la liste des semaines pour chaque groupe (sauf si vous avez configuré vos groupes), et vos tableaux pour chaque semaine du carnet de suivi formaté avec des *;*.

Pour créer un tableau à partir de ces valeurs, copiez les dans Word. Ensuite sélectionner Tableau/Nouveau/Convertir Texte en Tableau… tout en ayant sélectionner vos données de la semaine.

Une boite de dialogue apparaitra pour vous demander le caractère séparateur. Sélectionner le point virgule *;*.

Votre tableau de la semaine sera ainsi importé dans Word.
Il faut réitérer cette manipulation pour chaque semaine.

## Changelog

v1.0 : Version 2014/2015 pour la génération du carnet de suivi DII5