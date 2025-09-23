
#%%
import pandas as pd

df = pd.read_csv("Analise-Brasileirao/dados/brasileirao.csv")

df["percentual_vitoria"] = df["won"] / df["played"] * 100
df["media_gols_marcados"] = df["goals"] / df["played"] 
df["media_gols_sofridos"] = df["goals_taken"] / df["played"]
df["media_pontos"] = df["points"] / df["played"]

df
