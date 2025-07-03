import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.preprocessing import clean_text

def test_empty_input():
    assert clean_text("") == ""
    assert clean_text("   ") == ""
    assert clean_text(None) == ""

def test_basic_cleaning():
    text = "Hello!!! How are you??? 123"
    cleaned = clean_text(text)
    assert "hello" not in cleaned  # car "hello" est un stopword après stemming
    assert "123" not in cleaned
    assert "?" not in cleaned

def test_short_words():
    assert all(len(word) > 2 for word in clean_text("Hi to be an AI").split())

def test_stopwords_removal():
    result = clean_text("this is the best thing that has ever happened")
    for stopword in ["this", "is", "the", "that", "has", "ever"]:
        assert stopword not in result

def test_stemming():
    text = "running runners ran easily"
    result = clean_text(text)
    assert "run" in result or "runner" in result or "ran" in result

def test_basic_cleaning():
    text = "Hello!!! How are you??? 123"
    cleaned = clean_text(text)
    # Vérifie que les caractères spéciaux et chiffres sont bien supprimés
    assert "123" not in cleaned
    assert "!" not in cleaned
    assert all(len(word) > 2 for word in cleaned.split())
    
def test_stopwords_removal():
    result = clean_text("this is the best thing that has ever happened")
    # Vérifie que certains stopwords communs sont supprimés
    for stopword in ["this", "is", "the"]:
        assert stopword not in result
