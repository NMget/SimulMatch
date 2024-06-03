# Changelog

Tous les changements notables de ce projet seront documentés dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/), et ce projet adhère à [Semantic Versioning](https://semver.org/lang/fr/).

## [1.0.0] - 2024-05-30
### Ajouté
- Initialisation du projet avec Flask.
- Configuration de la base de données PostgreSQL.
- Mise en place de l'ORM SQLAlchemy.
- Création des tables `Team`, `Poule`, `Liaison`, `Joueur`, et `Match`.
- Implémentation de la gestion des équipes (création, mise à jour, suppression).
- Implémentation de la gestion des joueurs (création, mise à jour, suppression).
- Création et organisation des poules.
- Fonctionnalité de création et de gestion des matchs.
- Interface utilisateur pour l'affichage et la mise à jour des scores en temps réel.
- Enregistrement des résultats des matchs dans la base de données.

## [Unreleased]
### Ajouté
- Planification de l'ajout de la fonctionnalité de gestion des utilisateurs avec différents rôles (administrateur, utilisateur).
- Planification de l'ajout des statistiques détaillées pour chaque match.
- Planification de l'ajout d'une interface utilisateur améliorée pour la visualisation des poules et des classements.

### Modifié
- Amélioration de la documentation pour l'installation et la configuration du projet.
- Refactorisation du code pour améliorer la maintenabilité et la lisibilité.

### Corrigé
- Correction de bugs mineurs dans la mise à jour des scores en temps réel.
- Correction de problèmes de migration de base de données.

## Historique des versions
### [0.1.0] - 2024-04-30
- Prototype initial de l'application avec des fonctionnalités de base.
- Implémentation de la création de matchs et de la mise à jour des scores.
