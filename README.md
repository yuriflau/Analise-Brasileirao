# ⚽ Análise de Dados do Brasileirão

Este projeto tem como objetivo analisar dados do **Campeonato Brasileiro de Futebol (Brasileirão)**, explorando o desempenho dos times e estatísticas gerais da competição.  
O foco é aplicar técnicas de **Ciência de Dados** para transformar dados brutos em **insights visuais e análises úteis**.

---

## 📊 Objetivos do Projeto
- Explorar estatísticas gerais do campeonato (vitórias, derrotas, gols, pontos).  
- Identificar os times com melhor e pior desempenho.  
- Criar visualizações que facilitem o entendimento dos dados.  
- Desenvolver um dashboard interativo para consulta rápida.

---

## 1️⃣ Base de Dados

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
```

![Primeiras linhas do dataset](images/print_head.png)

---

## 2️⃣ Novas métricas criadas

Além dos dados originais, o projeto gera novas colunas para enriquecer a análise:

percentual_vitoria → Taxa de vitórias (%) por temporada

media_gols_marcados → Média de gols marcados por jogo

media_gols_sofridos → Média de gols sofridos por jogo

media_pontos → Média de pontos conquistados por jogo

Essas métricas permitem comparar eficiência, ataque e defesa entre os clubes.

---

## 3️⃣ Principais análises realizadas

Times campeões: identificação dos campeões de cada temporada.

Ranking de títulos: clubes mais vezes campeões.

Melhor campanha da história: campeão com maior percentual de vitórias.

Melhor defesa campeã: campeão que menos sofreu gols em média.

Top 10 históricos:

Clubes com mais vitórias acumuladas.

Clubes que mais marcaram gols.

Clubes com melhor saldo de gols.

Evolução por temporada: linha do tempo mostrando a pontuação de clubes selecionados.

---

## 4️⃣ Exemplos de visualizações

📈 Gráfico de barras com os times mais vitoriosos da história.

⚽ Top 10 clubes que mais marcaram gols.

🛡️ Comparação entre médias de gols sofridos.

📊 Evolução dos pontos ao longo das temporadas para times específicos.

(as imagens dos gráficos podem ser adicionadas aqui com ![alt text](caminho/imagem.png))

## 🛠️ Tecnologias Utilizadas

Python → Pandas, Matplotlib, Seaborn

Jupyter Notebook → Exploração interativa dos dados

Power BI / Streamlit → Dashboard interativo

Git & GitHub → Controle de versão e publicação do projeto

📂 Estrutura do Projeto
Analise-Brasileirao/
│── dados/
│   └── brasileirao.csv        # Base de dados
│── main.py                    # Script principal de análise
│── README.md                  # Documentação do projeto
│── requirements.txt           # Dependências do projeto

🚀 Como executar o projeto

Clone este repositório:

git clone https://github.com/seu-usuario/Analise-Brasileirao.git
cd Analise-Brasileirao


Instale as dependências:

pip install -r requirements.txt


Execute o script:

python main.py

📌 Próximos passos
