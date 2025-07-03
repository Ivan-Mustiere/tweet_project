# 🧠 Tweet Classifier – Catastrophes vs Normaux

Ce projet est un pipeline de classification automatique de tweets, visant à distinguer les tweets liés à des catastrophes de ceux normaux.  
Il suit les bonnes pratiques de data science industrielle : nettoyage, modélisation, tests unitaires, dockerisation.

---

## 📁 Structure du projet
tweet_project/
├── data/ # Contient tweets.csv
├── notebooks/ # EDA et pipeline interactif
│ ├── 01_EDA.ipynb
│ └── 02_Preprocessing_Modeling.ipynb
├── src/ # Code source
│ ├── preprocessing.py
│ └── modeling.py
├── tests/ # Tests unitaires
│ ├── test_preprocessing.py
│ └── test_modeling.py
├── main.py # Script principal d'entraînement
├── requirements.txt # Dépendances Python
├── Dockerfile # (Optionnel) pour exécution conteneurisée
└── README.md # Ce fichier

## ▶️ Exécuter le projet (en local)

### 1. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 2. Installer les dépendances

```bash
python setup_nltk_full.py
```

### 3. Lancer le pipeline

```bash
python main.py
```

### 4. Exécuter les tests

```bash
pytest
```

## 🐳 Exécuter avec Docker

### 1. Construire l’image Docker

```bash
docker build -t tweet-classifier .
```

### 2. Lancer les tests dans Docker

```bash
docker run --rm -it tweet-classifier pytest
```

### 3. Lancer un conteneur pour exécuter le pipeline

```bash
docker run --rm -it tweet-classifier
```

## 🧪 Exemple de sortie

✅ Dataset chargé avec succès.
Nombre d'exemples : 7613

📊 Résultats de l’évaluation :
Accuracy  : 0.8004
Precision : 0.8108
Recall    : 0.6934
F1 Score  : 0.7475