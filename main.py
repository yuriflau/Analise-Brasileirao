
#%%
import pandas as pd

df = pd.read_csv("Analise-Brasileirao/dados/brasileirao.csv")

df["percentual_vitoria"] = df["won"] / df["played"] * 100
df["media_gols_marcados"] = df["goals"] / df["played"] 
df["media_gols_sofridos"] = df["goals_taken"] / df["played"]
df["media_pontos"] = df["points"] / df["played"]

df

# %%
top_vitorias = df.groupby("team")["won"].sum().sort_values(ascending=False)
top_vitorias.head(10)

# %%
top_gols = df.groupby("team")["goals"].sum().sort_values(ascending=False)
top_gols.head(10)

# %%
top_saldo = df.groupby("team")["goals_diff"].sum().sort_values(ascending=False)
top_saldo.head(10)

# %%
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))
sns.barplot(x=top_vitorias.index, y=top_vitorias.values)
plt.xticks(rotation=90)
plt.title("Top 10 times com mais vitórias históricas")
plt.show()

plt.figure(figsize=(12,6))
sns.barplot(x=top_gols.index, y=top_gols.values)
plt.xticks(rotation=90)
plt.title("Top 10 times que mais marcaram gols")
plt.show()

times_exemplo = ["Flamengo", "Palmeiras", "Corinthians"]  # personalize se quiser
plt.figure(figsize=(14,7))
for team in times_exemplo:
    subset = df[df["team"] == team]
    plt.plot(subset["season"], subset["points"], marker='o', label=team)

plt.xticks(rotation=90)
plt.title("Evolução de pontos por temporada")
plt.xlabel("Temporada")
plt.ylabel("Pontos")
plt.legend()
plt.show()


# %%
