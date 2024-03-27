from data.load_data import *
from data.supp_colonne import *
import pandas as pd

df_guerre = load_data_csv('C:/Users/ahamada/OneDrive - Capgemini/Desktop/PROJET_M1/dataset/Guerre.csv')
df_epidemie = load_data_xlsx('C:/Users/ahamada/Downloads/CastastopheNaturelle_Epidemies.xlsx', 'EM-DAT Data')


# Utilisation correcte des noms de DataFrames
df_epidemie_cleaned = remove_columns_from_excel(df_epidemie)

# Assurez-vous d'utiliser le bon DataFrame pour vÃ©rifier les colonnes restantes
print(df_epidemie_cleaned)