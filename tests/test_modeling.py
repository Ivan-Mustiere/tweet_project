import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from src.modeling import train_and_evaluate

def test_pipeline_execution():
    # Dataset minimal (texte + cible)
    data = pd.DataFrame({
        "text": [
            "Forest fire near La Ronge", 
            "Everything is fine in the city",
            "Flood in Jakarta causes chaos", 
            "Having a nice coffee at the beach"
        ],
        "target": [1, 0, 1, 0]
    })

    result = train_and_evaluate(data["text"], data["target"])

    # Vérifie que les métriques sont bien retournées
    for metric in ["accuracy", "precision", "recall", "f1"]:
        assert metric in result
        assert isinstance(result[metric], float)

    # Vérifie que le pipeline renvoie bien un modèle entraîné
    assert hasattr(result["model"], "predict")
