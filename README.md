# ⚽ Análise de Dados do Brasileirão

Este projeto tem como objetivo analisar dados do **Campeonato Brasileiro de Futebol (Brasileirão)**, explorando o desempenho de times, jogadores e estatísticas gerais da competição.  
O foco é aplicar técnicas de **Ciência de Dados** para transformar dados brutos em **insights visuais e análises úteis**.

---

## 📊 Objetivos do Projeto
- Explorar estatísticas gerais do campeonato (vitórias, derrotas, gols, pontos).  
- Identificar os times com melhor e pior desempenho.  
- Destacar jogadores em destaques (artilheiros, assistências, cartões).  
- Criar visualizações que facilitem o entendimento dos dados.  
- Desenvolver um dashboard interativo para consulta rápida.

---

## 1️⃣ Base de Dados Cru

A base contém as seguintes colunas:

| Coluna        | Descrição |
|---------------|-----------|
| season        | Ano da temporada |
| place         | Posição final do time |
| team          | Nome do time |
| points        | Pontos conquistados |
| played        | Jogos disputados |
| won           | Jogos vencidos |
| draw          | Empates |
| loss          | Derrotas |
| goals         | Gols marcados |
| goals_taken   | Gols sofridos |
| goals_diff    | Saldo de gols (gols - gols sofridos) |

Exemplo das primeiras linhas do CSV:

```python
import pandas as pd
df = pd.read_csv("dados/brasileirao.csv")
df.head()

## 🛠️ Tecnologias Utilizadas
- **Python** → Pandas, Matplotlib, Seaborn  
- **Jupyter Notebook** → Exploração dos dados  
- **Power BI / Streamlit** → Dashboard interativo  
- **GitHub** → Controle de versão e portfólio  

---

## 📂 Estrutura do Projeto
