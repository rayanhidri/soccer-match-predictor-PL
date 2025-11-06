"""
Premier League Data Fetcher
Récupère les données de matchs via l'API football-data.org
"""

import requests
import json
import pandas as pd
from datetime import datetime
import time

# ============================================
# CONFIGURATION
# ============================================

API_KEY = "013ada4bd4e04c9c9a8363c4f8a359d8"  
BASE_URL = "https://api.football-data.org/v4"
COMPETITION_ID = 2021  # Code pour Premier League dans l'API

# ============================================
# FONCTION PRINCIPALE
# ============================================

def fetch_season_matches(season_year):
    """
    Récupère tous les matchs d'une saison de Premier League.
    
    Args:
        season_year (int): Année de début de saison (ex: 2023 pour saison 2023-24)
    
    Returns:
        list: Liste de dictionnaires contenant les infos de chaque match
    """
    
    # Construire l'URL de l'endpoint
    url = f"{BASE_URL}/competitions/{COMPETITION_ID}/matches"
    
    # Headers pour l'authentification
    headers = {
        "X-Auth-Token": API_KEY
    }
    
    # Paramètres de la requête
    params = {
        "season": season_year
    }
    
    print(f"🔍 Fetching matches for season {season_year}-{season_year+1}...")
    
    try:
        # Faire la requête HTTP GET
        response = requests.get(url, headers=headers, params=params)
        
        # Vérifier le statut de la réponse
        if response.status_code == 200:
            # Succès, Parser le JSON
            data = response.json()
            matches = data.get("matches", [])
            print(f"Successfully fetched {len(matches)} matches!")
            return matches
        
        elif response.status_code == 429:
            # Too many requests - on a dépassé la limite
            print("⏳ Rate limit reached. Waiting 60 seconds...")
            time.sleep(60)
            return fetch_season_matches(season_year)  # Réessayer
        
        else:
            # Erreur
            print(f"Error {response.status_code}: {response.text}")
            return []
    
    except Exception as e:
        print(f"Exception occurred: {e}")
        return []


def process_match_data(matches):
    """
    Transforme les données brutes JSON en format structuré pour le ML.
    
    Args:
        matches (list): Liste des matchs (format JSON de l'API)
    
    Returns:
        pd.DataFrame: DataFrame pandas avec les données nettoyées
    """
    
    processed_data = []
    
    for match in matches:
        # Extraire seulement les matchs terminés (pas les futurs matchs)
        if match['status'] != 'FINISHED':
            continue
        
        # Créer un dictionnaire pour ce match
        match_info = {
            'date': match['utcDate'],
            'home_team': match['homeTeam']['name'],
            'away_team': match['awayTeam']['name'],
            'home_score': match['score']['fullTime']['home'],
            'away_score': match['score']['fullTime']['away'],
            'matchday': match['matchday'],  # Journée (1-38 en Premier League)
        }
        
        processed_data.append(match_info)
    
    # Convertir en DataFrame
    df = pd.DataFrame(processed_data)
    
    # Convertir la date en format datetime
    df['date'] = pd.to_datetime(df['date'])
    
    return df


def fetch_multiple_seasons(start_year, end_year):
    """
    Récupère les données pour plusieurs saisons.
    
    Args:
        start_year (int): Première saison (ex: 2019)
        end_year (int): Dernière saison (ex: 2023)
    
    Returns:
        pd.DataFrame: Toutes les données combinées
    """
    
    all_matches = []
    
    for year in range(start_year, end_year + 1):
        matches = fetch_season_matches(year)
        all_matches.extend(matches)
        
        # Attendre 1 seconde entre chaque requête (respect du rate limit)
        time.sleep(1)
    
    # Processer toutes les données
    df = process_match_data(all_matches)
    
    print(f"\n📊 Total matches fetched: {len(df)}")
    print(f"📅 Date range: {df['date'].min()} to {df['date'].max()}")
    
    return df


# ============================================
# EXÉCUTION
# ============================================

if __name__ == "__main__":
    print("⚽ Premier League Data Fetcher")
    print("=" * 50)
    
    # Récupérer les 2 dernières saisons 
    df = fetch_multiple_seasons(2023, 2024)
    
    # Sauvegarder en CSV
    import os
    output_path = os.path.join(os.path.dirname(__file__), "../../data/raw/premier_league_matches.csv")
    output_path = os.path.abspath(output_path)
    df.to_csv(output_path, index=False)
    
    print(f"\n✅ Data saved to: {output_path}")
    print(f"📦 Shape: {df.shape[0]} matches, {df.shape[1]} columns")
    
    # Afficher un aperçu
    print("\n👀 Sample data:")
    print(df.head())