import google.generativeai as genai
import os

# Remplacez par votre clé directement pour le test
API_KEY = "AIzaSyDgFEyYy3ubb10eW9zqbzYGOVnIwf5Z2TY" 
genai.configure(api_key=API_KEY)

print("--- Modèles accessibles avec cette clé ---")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"Nom : {m.name}")
except Exception as e:
    print(f"Erreur lors du listing : {e}")