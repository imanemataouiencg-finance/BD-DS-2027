# Prompt : Conception d'un TP universitaire – Acquisition, stockage et exploitation de données avec Google Colab et SQL

## 1. Contexte pédagogique

Agis en tant qu'enseignant-chercheur spécialisé en informatique, bases de données et analyse de données.

Conçois un **travail pratique (TP) complet, progressif et réalisable sur Google Colab**, destiné à des étudiants universitaires découvrant l'intégration de Python, Google Drive et SQL dans un projet d'analyse de données.

Le TP doit être organisé autour d'un **mini-projet concret**, fondé sur l'exploitation d'un jeu de données réel.

**Principe pédagogique :** les étudiants doivent réaliser eux-mêmes les différentes étapes. Le document doit donc présenter des consignes, des questions, des indications et des espaces de réponse, sans fournir immédiatement toutes les solutions.

## 2. Objectifs pédagogiques

À l'issue du TP, les étudiants devront être capables de :

1. Rechercher et sélectionner un jeu de données public pertinent.
2. Télécharger un dataset depuis une source fiable.
3. Importer et stocker les données dans Google Drive.
4. Connecter Google Colab à Google Drive.
5. Charger et explorer un dataset avec Python et Pandas.
6. Créer une base de données SQLite à partir du dataset.
7. Exécuter des requêtes SQL depuis Python.
8. Réaliser des analyses statistiques simples avec SQL.
9. Interpréter les résultats obtenus.
10. Sauvegarder le notebook et les résultats du projet.

## 3. Choix du dataset

L'étudiant doit sélectionner un jeu de données provenant de l'une des sources suivantes :

- **Kaggle** : <https://www.kaggle.com/datasets>
- **Fonds monétaire international (FMI)** : <https://www.imf.org/en/Data>
- **Haut-Commissariat au Plan du Maroc (HCP)** : <https://www.hcp.ma>

Le dataset doit respecter les critères suivants :

- Être public et accessible légalement.
- Être disponible en CSV ou Excel, ou dans un format facilement convertible.
- Contenir au moins 100 observations et 5 variables, sauf justification.
- Comporter des variables numériques et catégorielles.
- Permettre l'utilisation de requêtes SQL d'agrégation.
- Être suffisamment simple pour être exploité pendant un TP.

Proposer trois exemples de datasets pertinents, idéalement liés à l'économie, à l'emploi, à la démographie ou aux entreprises.

Pour chaque dataset, indiquer la source, le lien d'accès, les principales variables et les analyses SQL possibles. Ne pas inventer de liens ni de caractéristiques non vérifiées.

## 4. Déroulement du TP

### Partie 1 – Recherche et téléchargement du dataset

Demander aux étudiants de :

1. Choisir une source de données.
2. Identifier un dataset pertinent.
3. Télécharger le fichier.
4. Présenter brièvement son contenu.
5. Justifier leur choix.

**Questions :**

- Quelle est la source du dataset ?
- Quel est le domaine étudié ?
- Combien d'observations et de variables contient-il ?
- Quelles analyses pourrait-on réaliser à partir de ces données ?

### Partie 2 – Stockage sur Google Drive

Les étudiants doivent :

1. Créer un dossier `TP_SQL_Dataset` sur Google Drive.
2. Y déposer le dataset téléchargé.
3. Créer un notebook Google Colab.
4. Monter Google Drive dans Colab.
5. Vérifier l'existence du fichier.
6. Charger le dataset avec Pandas.

Fournir uniquement le code de départ nécessaire à la connexion Google Drive et au chargement du fichier.

### Partie 3 – Exploration et préparation des données

Demander aux étudiants d'utiliser Pandas pour :

- Afficher les 10 premières lignes.
- Identifier les noms et les types des colonnes.
- Déterminer le nombre d'observations.
- Identifier les valeurs manquantes.
- Rechercher les doublons.
- Calculer quelques statistiques descriptives.
- Effectuer les transformations nécessaires avant l'importation dans SQLite.

### Partie 4 – Création de la base de données SQLite

Les étudiants doivent :

1. Créer une base SQLite dans leur dossier Google Drive.
2. Créer une table adaptée à la structure du dataset.
3. Importer les données dans cette table.
4. Vérifier le nombre de lignes importées.
5. Afficher les premières lignes avec une requête SQL.

Utiliser les bibliothèques :

```python
import sqlite3
import pandas as pd
```

Expliquer brièvement le rôle de `sqlite3`, de `pandas` et de la méthode `to_sql()`.

### Partie 5 – Exploitation du dataset avec SQL

Construire une série de 15 exercices SQL de difficulté progressive.

**Niveau 1 – Requêtes fondamentales**

1. Afficher toutes les observations.
2. Sélectionner certaines colonnes.
3. Limiter le nombre de résultats.
4. Trier les observations.
5. Filtrer les données avec `WHERE`.

**Niveau 2 – Agrégations**

6. Calculer le nombre total d'enregistrements.
7. Calculer une moyenne.
8. Déterminer les valeurs minimale et maximale.
9. Regrouper les observations avec `GROUP BY`.
10. Filtrer les groupes avec `HAVING`.

**Niveau 3 – Analyses avancées**

11. Combiner plusieurs conditions avec `AND` et `OR`.
12. Utiliser `BETWEEN` ou `IN`.
13. Réaliser un classement avec `ORDER BY`.
14. Construire une sous-requête SQL.
15. Produire une analyse synthétique répondant à une question métier ou économique.

Les requêtes doivent être adaptées aux colonnes réellement présentes dans le dataset choisi.

### Partie 6 – Analyse et interprétation

Demander aux étudiants de sélectionner cinq requêtes SQL significatives et de :

- Présenter les résultats sous forme de tableaux Pandas.
- Interpréter les résultats.
- Produire au moins deux graphiques avec Matplotlib.
- Formuler trois conclusions sur les données analysées.

### Partie 7 – Livrables

Chaque étudiant ou groupe doit remettre :

1. Un notebook Google Colab fonctionnel (`.ipynb`).
2. Le dataset original.
3. La base SQLite (`.db`).
4. Les 15 requêtes SQL et leurs résultats.
5. Une synthèse d'une page présentant les principaux résultats et difficultés rencontrées.

## 5. Modalités d'évaluation

Proposer une grille d'évaluation sur 20 points :

| Critère | Points |
|---|---:|
| Choix et justification du dataset | 2 |
| Téléchargement et stockage sur Drive | 3 |
| Exploration et préparation des données | 3 |
| Création de la base SQLite | 3 |
| Qualité des requêtes SQL | 5 |
| Analyse et interprétation | 3 |
| Organisation et documentation du notebook | 1 |
| **Total** | **20** |

## 6. Contraintes techniques et pédagogiques

- Le TP doit être réalisable dans Google Colab sans installation complexe.
- Privilégier les bibliothèques Python déjà disponibles dans Colab.
- Utiliser SQLite, sans serveur de base de données externe.
- Prévoir une méthode de téléchargement manuelle pour les sources nécessitant une authentification, notamment Kaggle.
- Éviter de demander aux étudiants de publier des identifiants ou des clés API.
- Prévoir des messages de vérification après chaque étape.
- Adapter la difficulté à des étudiants débutants ou intermédiaires.
- Prévoir une durée totale de 3 à 4 heures.
- Distinguer clairement les consignes obligatoires et les exercices facultatifs.

## 7. Format de sortie attendu

Générer deux livrables distincts :

**Document étudiant**

- Présentation du TP et objectifs.
- Consignes détaillées et progressives.
- Questions et exercices numérotés.
- Squelettes de code à compléter.
- Espaces réservés aux observations et aux réponses.
- Grille d'évaluation.

**Corrigé enseignant**

- Notebook Google Colab complet et exécutable.
- Code Python commenté.
- Requêtes SQL corrigées.
- Résultats attendus et explications.
- Solutions alternatives lorsque cela est pertinent.
- Erreurs fréquentes et pistes de remédiation.

Le corrigé doit s'appuyer sur un dataset réel, accessible et précisément identifié. Les résultats chiffrés doivent être obtenus par exécution du code, et non inventés.

**Résultat attendu :** un TP universitaire autonome, directement exploitable en séance, permettant aux étudiants de suivre toute la chaîne de traitement :

**Source de données → Téléchargement → Google Drive → Google Colab → Pandas → SQLite → Requêtes SQL → Analyse des résultats.**
