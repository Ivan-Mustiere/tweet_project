import pandas as pd
from src.modeling import train_and_evaluate

def main():
    try:
        df = pd.read_csv("data/tweets.csv")
    except FileNotFoundError:
        print("❌ Fichier 'data/tweets.csv' introuvable.")
        return

    if 'text' not in df.columns or 'target' not in df.columns:
        print("❌ Le fichier CSV doit contenir les colonnes 'text' et 'target'.")
        return

    print("✅ Dataset chargé avec succès.")
    print(f"Nombre d'exemples : {len(df)}")

    results = train_and_evaluate(df['text'], df['target'])

    print("\n📊 Résultats de l’évaluation :")
    print(f"Accuracy  : {results['accuracy']:.4f}")
    print(f"Precision : {results['precision']:.4f}")
    print(f"Recall    : {results['recall']:.4f}")
    print(f"F1 Score  : {results['f1']:.4f}")

if __name__ == "__main__":
    main()
