# 🐳 Utilisation Docker – Tweet Classifier

Ce fichier explique comment exécuter le projet **Tweet Classifier** dans un conteneur Docker.

---

## 📦 1. Prérequis

- Docker installé sur votre machine (Docker Desktop pour Windows)  
  👉 https://www.docker.com/products/docker-desktop

---

## 🔨 2. Construire l’image Docker

Dans le dossier racine du projet :

```bash
docker build -t tweet-pipeline .
```

## ▶️ 3. Exécuter le pipeline principal

```bash
docker run --rm tweet-pipeline
```