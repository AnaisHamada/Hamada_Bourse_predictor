import pandas as pd

def prepare_catastrophe_dates(df):
    """
    Convertit les colonnes de dates de début et de fin en strings et crée des colonnes de date de début et de fin formatées.

    Args:
        df (pd.DataFrame): DataFrame contenant les colonnes 'Start Year', 'Start Month', 'End Year', et 'End Month'.

    Returns:
        pd.DataFrame: DataFrame avec les colonnes de date ajoutées 'Start_Date' et 'End_Date'.
    """
    # Conversion des colonnes en string
    df['Start Year'] = df['Start Year'].astype(str)
    df['Start Month'] = df['Start Month'].astype(str)
    df['End Year'] = df['End Year'].astype(str)
    df['End Month'] = df['End Month'].astype(str)

    # Concaténation des colonnes pour créer des dates formatées
    df['Start_Date'] = df['Start Year'] + '-' + df['Start Month'].str.split('.').str[0]
    df['End_Date'] = df['End Year'] + '-' + df['End Month'].str.split('.').str[0]

    return df