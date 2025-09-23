#%% Importação das bibliotecas principais
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#%% Leitura da base de dados
# O arquivo "brasileirao.csv" contém dados do campeonato de 2003 até 2024
df = pd.read_csv("dados/brasileirao.csv")

#%% Criação de novas métricas
# Percentual de vitórias, médias de gols marcados/sofridos e média de pontos
df["percentual_vitoria"] = df["won"] / df["played"] * 100
df["media_gols_marcados"] = df["goals"] / df["played"] 
df["media_gols_sofridos"] = df["goals_taken"] / df["played"]
df["media_pontos"] = df["points"] / df["played"]

#%% Filtrar apenas os campeões de cada temporada
filtro_campeoes = df["place"] == 1
df_campeoes = df[filtro_campeoes]

#%% Estatísticas gerais dos campeões
# Descreve estatísticas básicas (média, desvio padrão, etc.)
df_campeoes.describe()

#%% Qual time mais vezes foi campeão
df_campeoes.groupby("team")["place"].count().sort_values(ascending=False)

#%% Melhor campeão em termos de % de vitórias
indice_maior_campeao = df_campeoes["percentual_vitoria"].idxmax()
df_campeoes.loc[indice_maior_campeao]

#%% Campeão com a melhor defesa (% menor média de gols sofridos)
indice_melhor_defesa = df_campeoes["media_gols_sofridos"].idxmin()
df_campeoes.loc[indice_melhor_defesa]

#%% Ranking histórico de vitórias
top_vitorias = df.groupby("team")["won"].sum().sort_values(ascending=False)
top_vitorias.head(10)

#%% Ranking histórico de gols
top_gols = df.groupby("team")["goals"].sum().sort_values(ascending=False)
top_gols.head(10)

#%% Ranking histórico de saldo de gols
top_saldo = df.groupby("team")["goals_diff"].sum().sort_values(ascending=False)
top_saldo.head(10)

#%% Visualizações - Top 10 vitórias
plt.figure(figsize=(12,6))
sns.barplot(x=top_vitorias.index[:10], y=top_vitorias.values[:10])
plt.xticks(rotation=90)
plt.title("Top 10 times com mais vitórias históricas")
plt.show()

#%% Visualizações - Top 10 gols
plt.figure(figsize=(12,6))
sns.barplot(x=top_gols.index[:10], y=top_gols.values[:10])
plt.xticks(rotation=90)
plt.title("Top 10 times que mais marcaram gols")
plt.show()

#%% Evolução de pontos por temporada - exemplo com alguns times
times_exemplo = ["Flamengo", "Palmeiras", "Corinthians"]
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
