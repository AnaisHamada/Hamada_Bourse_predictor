import pandas as pd

def load_data_csv(filepath):
    """
    Charge les données depuis un fichier CSV dans un DataFrame pandas.

    Args:
        filepath (str): Chemin complet du fichier CSV à charger.

    Returns:
        DataFrame: Un DataFrame pandas contenant les données chargées du fichier.
    """
    try:
        df = pd.read_csv(filepath)
        print(f"Data chargé correctement {filepath}")
        return df
    except FileNotFoundError:
        print(f"Le fichier {filepath} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur est survenue lors du chargement du fichier {filepath}: {e}")


def load_data_xlsx(filepath , sheet):
    """
    Charge les données depuis un fichier XLSX dans un DataFrame pandas.

    Args:
        filepath (str): Chemin complet du fichier XLSX à charger.

    Returns:
        DataFrame: Un DataFrame pandas contenant les données chargées du fichier.
    """
    try:
        df = pd.read_excel(filepath , sheet_name=sheet)
        print(f"Data chargé correctement {filepath}")
        return df
    except FileNotFoundError:
        print(f"Le fichier {filepath} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur est survenue lors du chargement du fichier {filepath}: {e}")