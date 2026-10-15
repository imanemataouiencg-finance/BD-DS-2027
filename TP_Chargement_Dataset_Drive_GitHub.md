# TP — Télécharger, stocker et charger un dataset dans Google Colab

**Objectif :** télécharger un jeu de données depuis Kaggle, le Fonds monétaire international (FMI) ou le Haut-Commissariat au Plan (HCP) du Maroc, le stocker dans Google Drive ou sur GitHub, puis le charger dans Google Colab avec Python et Pandas et l'exploiter avec SQLite.

## 1. Architecture générale

```text
Kaggle / FMI / HCP
       |
   CSV ou Excel
       |
  +----+----+
  |         |
Google Drive  GitHub (dépôt public)
  |         |
  +----+----+
       |
 Google Colab + Pandas
       |
 SQLite + requêtes SQL
```

## 2. Télécharger un dataset

- **Kaggle :** <https://www.kaggle.com/datasets> — rechercher un dataset, ouvrir sa page et cliquer sur « Download ». Un compte peut être nécessaire.
- **FMI :** <https://www.imf.org/en/Data> — sélectionner une base et des indicateurs, puis exporter les données si l'option existe.
- **HCP Maroc :** <https://www.hcp.ma> — rechercher une publication statistique et télécharger un tableau CSV ou Excel lorsqu'il est disponible.

Dans la suite, on suppose que le fichier s'appelle `dataset.csv`. Vérifier les conditions de licence avant toute republication.

## 3. Méthode A — Stocker le dataset sur Google Drive

### Étape A1 — Importer le fichier

1. Ouvrir <https://drive.google.com>.
2. Créer un dossier `TP_SQL_Dataset`.
3. Importer `dataset.csv` dans ce dossier.
4. Ouvrir un notebook sur <https://colab.research.google.com>.

### Étape A2 — Monter Google Drive

```python
from google.colab import drive

# Autoriser l'accès à Google Drive
drive.mount('/content/drive')
```

### Étape A3 — Charger les données

```python
import pandas as pd
from pathlib import Path

chemin = Path('/content/drive/MyDrive/TP_SQL_Dataset/dataset.csv')

if not chemin.is_file():
    raise FileNotFoundError(f'Fichier introuvable : {chemin}')

df = pd.read_csv(chemin)
display(df.head(10))
print('Nombre de lignes :', df.shape[0])
print('Nombre de colonnes :', df.shape[1])
```

**Variantes :** pour Excel, utiliser `pd.read_excel(chemin)` avec un chemin `.xlsx` ; pour un CSV séparé par des points-virgules, utiliser `pd.read_csv(chemin, sep=';')`. Vérifier aussi l'encodage du fichier.

## 4. Méthode B — Stocker le dataset sur GitHub

### Étape B1 — Créer un dépôt et téléverser le fichier

1. Se connecter à <https://github.com> et choisir **New repository**.
2. Nommer le dépôt `TP_SQL_Dataset`.
3. Choisir **Public** si le chargement doit se faire sans authentification.
4. Créer le dépôt, puis choisir **Add file → Upload files**.
5. Ajouter `dataset.csv` et valider avec **Commit changes**.

**Attention :** ne pas publier de données confidentielles ni de dataset dont la licence interdit la redistribution. Les dépôts GitHub ne sont pas adaptés aux très gros fichiers de données.

### Étape B2 — Récupérer le lien Raw

Ouvrir `dataset.csv` dans le dépôt, cliquer sur **Raw** et copier son URL. Sa structure est généralement :

```text
https://raw.githubusercontent.com/UTILISATEUR/TP_SQL_Dataset/main/dataset.csv
```

Remplacer `UTILISATEUR` par le compte réel et `main` par le nom de la branche utilisée si nécessaire.

### Étape B3 — Charger directement depuis GitHub

```python
import pandas as pd

url = (
    'https://raw.githubusercontent.com/'
    'UTILISATEUR/TP_SQL_Dataset/main/dataset.csv'
)

df = pd.read_csv(url)
display(df.head(10))
print('Dimensions :', df.shape)
print('Colonnes :', df.columns.tolist())
```

Ce script est un **modèle à personnaliser** : l'URL d'exemple ne pointe pas vers un dataset réel.

## 5. Méthode C — Script unique : choisir Drive ou GitHub

Modifier `SOURCE` et les chemins en fonction du fichier réellement utilisé.

```python
import pandas as pd

SOURCE = 'drive'  # 'drive' ou 'github'

if SOURCE == 'drive':
    from google.colab import drive
    drive.mount('/content/drive')
    fichier = '/content/drive/MyDrive/TP_SQL_Dataset/dataset.csv'
else:
    fichier = (
        'https://raw.githubusercontent.com/'
        'UTILISATEUR/TP_SQL_Dataset/main/dataset.csv'
    )

df = pd.read_csv(fichier)
display(df.head(10))
print('Dimensions :', df.shape)
```

## 6. Exploiter ensuite le dataset avec SQLite

Le DataFrame `df` a déjà été chargé par l'une des méthodes précédentes.

```python
import sqlite3
import pandas as pd

# Base locale temporaire dans l'environnement Colab
conn = sqlite3.connect('tp_sql.db')

# Importer les données dans la table SQLite « donnees »
df.to_sql('donnees', conn, if_exists='replace', index=False)

# Première requête SQL
requete = '''
SELECT *
FROM donnees
LIMIT 10;
'''
resultat = pd.read_sql_query(requete, conn)
display(resultat)

# Vérifier le nombre de lignes importées
total = pd.read_sql_query(
    'SELECT COUNT(*) AS total FROM donnees;', conn
)
display(total)

conn.close()
```

**Persistance :** `tp_sql.db` est créé ici dans l'environnement temporaire de Colab. Pour le conserver, copier le fichier vers Drive ou créer directement la base dans un dossier Drive monté.

## 7. Comparaison des deux méthodes

| Critère | Google Drive | GitHub |
|---|---|---|
| Facilité pour les débutants | Très bonne | Bonne |
| Stockage privé | Oui | Oui, avec authentification pour l'accès programmatique |
| Chargement direct par URL | Pas avec le chemin Drive ordinaire | Oui, avec Raw et dépôt public |
| Partage | Autorisations Drive | Dépôt et collaborateurs |
| Gestion des versions | Limitée | Très bonne |
| Données volumineuses | Généralement plus adapté | Limites de taille et de dépôt |
| Usage pédagogique | TP individuels | TP collaboratifs et reproductibilité |

## 8. Recommandation pédagogique

Privilégier **Google Drive** comme méthode principale pour des étudiants débutants. Présenter **GitHub** comme méthode complémentaire pour aborder le partage des datasets, la reproductibilité et le versionnement.

**Prolongement :** demander aux étudiants de construire 15 requêtes SQL progressives sur le dataset chargé, puis de présenter et commenter les résultats avec Pandas.
