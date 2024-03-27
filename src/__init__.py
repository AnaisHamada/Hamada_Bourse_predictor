from data.load_data import load_data_csv
from data.load_data import load_data_xlsx
import pandas as pd

df_guerre = load_data_csv("D:/ProjetPython/ProjetBoursePredictor/data/raw/Guerre.csv")
df_epidemie = load_data_xlsx("D:/ProjetPython/ProjetBoursePredictor/data/raw/CastastopheNaturelle.xlsx")


print(df_guerre)
print(df_epidemie)