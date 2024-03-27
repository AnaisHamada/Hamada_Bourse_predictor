import pandas as pd

def remove_columns_from_excel(df):
    """
    Supprime les colonnes spécifiées d'un fichier Excel et enregistre le résultat dans un nouveau fichier CSV.
    
    """

    try:
        # Routes les colonnes à supprimer
        
        columns_to_remove = [
            "DisNo.", "Historic", "Classification Key", "Disaster Group", "Disaster Type",
            "Disaster Subtype", "External IDs", "Event Name", "Subregion", "Location",
            "Origin", "OFDA Response", "Appeal", "Declaration",
            "AID Contribution ('000 US$)", "Magnitude", "Magnitude Scale", "Latitude", 
            "Longitude", "River Basin", "Total Deaths", "No. Injured", "No. Affected", 
            "No. Homeless", "Total Affected", "Reconstruction Costs ('000 US$)",
            "Reconstruction Costs, Adjusted ('000 US$)", "Insured Damage ('000 US$)", 
            "Insured Damage, Adjusted ('000 US$)", "Total Damage ('000 US$)", 
            "Total Damage, Adjusted ('000 US$)", "CPI", "Admin Units"
        ]
        # Supprimer les colonnes spécifiées
        df.drop(columns=columns_to_remove, inplace=True)
        
        return df
        
        print(f"Colonnes supprimées")
    except FileNotFoundError:
        print(f"Le fichier spécifié n'a pas été trouvé ")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")