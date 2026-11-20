# Python Template

Ce projet Python peut servir de modèle pour un nouveau projet. Il utilise Poetry pour gérer les dépendances et les scripts, Pytest pour les tests et SonarQube pour l'analyse de la qualité du code.

## Structure du projet

Ci-dessous, vous trouverez des informations sur les fichiers et répertoires importants du projet.

Le fichier `pyproject.toml` déclare les dépendances, le script `hello` et la configuration de Pytest.

Le fichier `requirements.txt` permet d'installer Poetry.

Le répertoire `src/` contient le code source et le répertoire `tests/` contient les tests.

## Installation

Une fois le projet cloné, exécutez les commandes suivantes, dans l'ordre : `pip install -r requirements.txt` pour installer Poetry, puis `poetry install` pour installer les dépendances du projet.

## Commandes utiles

- `poetry run pytest` : exécute les tests unitaires
- `poetry run hello` : exécute le script
- `./dist.sh` : crée un exécutable dans le répertoire `dist/`

## GitHub

Par défaut, le projet est configuré pour lancer Dependabot à 21 h afin de vérifier les mises à jour des dépendances Python et des GitHub Actions.

De plus, deux GitHub Actions sont configurées dans ce projet. La première, `compile-verify`, se lance à la création d'une pull request et lors des push sur la branche `develop`. La seconde, `sonar`, se lance après un push sur la branche `develop` afin d'analyser la qualité du code.

## SonarQube

Pour configurer SonarQube sur votre projet, vous devez éditer le fichier `sonar-project.properties` et modifier la valeur de `sonar.projectKey`. Vous devez également ajouter dans GitHub une variable `SONAR_URI` contenant l'URL de votre serveur, ainsi qu'un secret `SONAR_TOKEN` contenant votre token.
