# Utilise une image Python officielle
FROM python:3.10-slim

# Crée un dossier de travail
WORKDIR /app

# Copie les fichiers du projet dans l’image
COPY . .

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Téléchargement des données NLTK
RUN python -m nltk.downloader punkt stopwords wordnet omw-1.4 punkt_tab

# Commande par défaut : exécuter main.py
CMD ["python", "main.py"]
