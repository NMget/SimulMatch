# Architecture de l'Application Web de Retranscription de Matchs de Volley

## Introduction

Ce document décrit l'architecture de l'application web de retranscription de matchs de volley. Il couvre les aspects clés de la conception, y compris les composants principaux, la structure de la base de données, et les interactions entre les différentes parties de l'application.

## Vue d'Ensemble

L'application utilise une architecture web classique avec un backend en Flask (Python) et une base de données PostgreSQL. L'ORM SQLAlchemy est utilisé pour interagir avec la base de données. L'interface utilisateur est rendue à l'aide de modèles Jinja2.

## Composants Principaux

### Backend (Flask)

- **Flask** : Un micro-framework Python pour le développement web.
- **SQLAlchemy** : Un ORM (Object-Relational Mapping) pour interagir avec la base de données PostgreSQL.
- **Flask-Migrate** : Utilisé pour la gestion des migrations de la base de données.

### Base de Données (PostgreSQL)

- **PostgreSQL** : Un système de gestion de base de données relationnelle robuste et open-source.
- **PGAdmin** : Un outil de gestion pour PostgreSQL.

### Frontend

- **Jinja2** : Un moteur de template pour Flask, permettant de générer des pages HTML dynamiques.

## Structure de la Base de Données

La base de données est conçue pour stocker les informations nécessaires à la gestion des équipes, des joueurs, des poules et des matchs. Voici les tables principales :

### Tables

- **Team**
  - `id` : Identifiant unique de l'équipe.
  - `name` : Nom de l'équipe.
  - `logo_url` : URL du logo de l'équipe.

- **Poule**
  - `id` : Identifiant unique de la poule.
  - `name` : Nom de la poule.

- **Liaison**
  - `id` : Identifiant unique de la liaison.
  - `team_id` : Référence vers l'ID de l'équipe.
  - `poule_id` : Référence vers l'ID de la poule.
  - `points` : Points accumulés par l'équipe dans la poule.

- **Joueur**
  - `id` : Identifiant unique du joueur.
  - `first_name` : Prénom du joueur.
  - `last_name` : Nom du joueur.
  - `team_id` : Référence vers l'ID de l'équipe.

- **Match**
  - `id` : Identifiant unique du match.
  - `poule_id` : Référence vers l'ID de la poule.
  - `team1_id` : Référence vers l'ID de la première équipe.
  - `team2_id` : Référence vers l'ID de la deuxième équipe.
  - `result` : Résultat du match (0 si le match n'a pas eu lieu, 1 si l'équipe 1 a gagné, 2 si l'équipe 2 a gagné).

## Diagramme de la Base de Données

```plaintext
+-------------+     +-----------+     +----------+
|   Team      |     |  Poule    |     |  Match   |
+-------------+     +-----------+     +----------+
| id          |     | id        |     | id       |
| name        |     | name      |     | poule_id |
| logo_url    |     +-----------+     | team1_id |
+-------------+                       | team2_id |
                                      | result   |
+-------------+                       +----------+
|   Joueur    |     +-----------+
+-------------+     |  Liaison  |
| id          |     +-----------+
| first_name  |     | id        |
| last_name   |     | team_id   |
| team_id     |     | poule_id  |
+-------------+     | points    |
                    +-----------+
