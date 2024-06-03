# Application Web de Retranscription de Matchs de Volley

## Description

Ce projet a pour objectif de créer une application web permettant la retranscription de matchs de volley simplifiée, adaptée pour les tournois de notre club de volley. L'application permet de jouer des matchs déjà enregistrés dans la base de données ou de créer de nouveaux matchs, tout en affichant quelle équipe sert et le score de chaque équipe en temps réel.

## Fonctionnalités

- **Gestion des matchs** : Créer de nouveaux matchs ou jouer des matchs existants.
- **Suivi du service** : Indiquer quelle équipe est en train de servir.
- **Mise à jour des scores** : Mettre à jour le score de chaque équipe en temps réel.
- **Historique des matchs** : Enregistrer et consulter l'historique des matchs et leurs résultats.

## Technologies Utilisées

- **Framework** : Flask (Python)
- **ORM** : SQLAlchemy
- **Base de Données** : PostgreSQL
- **Outil de gestion de base de données** : PGAdmin

## Structure de la Base de Données

La base de données est conçue avec les tables suivantes :

- **Team** : Enregistre les équipes avec des champs pour le nom et l'URL du logo.
- **Poule** : Organise les équipes en groupes de compétition distincts.
- **Liaison** : Relie les équipes et les poules, en enregistrant les points accumulés par chaque équipe dans chaque poule.
- **Joueur** : Enregistre les membres de chaque équipe avec des références à leur équipe.
- **Match** : Enregistre les rencontres entre les équipes avec des champs pour l'ID de la poule, les ID des équipes impliquées et le résultat.

## Installation

### Prérequis

- Python 3.x
- PostgreSQL
- PGAdmin

### Étapes d'installation

1. **Cloner le dépôt**

    ```bash
    git clone https://github.com/NMget/SimulMatch.git
    cd SimulMatch
    ```

2. **Créer et activer un environnement virtuel**

    ```bash
    python -m venv env
    source env/bin/activate  # Sur Windows, utilisez `env\Scripts\activate`
    ```

3. **Installer les dépendances**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configurer la base de données**

    - Créez une base de données PostgreSQL pour l'application.
    - Configurez les informations de connexion à la base de données dans le fichier `app.py`.

5. **Initialiser la base de données**

    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

6. **Lancer l'application**

    ```bash
    flask run
    ```

## Utilisation

- Accédez à l'application via `http://127.0.0.1:5000`.
- Créez de nouveaux matchs ou sélectionnez des matchs existants.
- Mettez à jour le score et suivez le déroulement des matchs en temps réel.

## Contributions

Les contributions sont les bienvenues ! Veuillez soumettre une pull request ou ouvrir une issue pour toute suggestion ou amélioration.

## Licence

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus d'informations.

---

Développé par [Votre Nom](https://simul-match.vercel.app)
