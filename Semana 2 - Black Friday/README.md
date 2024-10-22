![progress](https://progress-bar.dev/100/ "progress")

# Pré-processamento de dados em Python

Neste desafio vamos praticar a manipulação de dados utilizando
a biblioteca [pandas](https://pandas.pydata.org/). Manipulação de dados é uma das tarefas
mais fundamentais para um cientista de dados e o pandas - biblioteca mais popular do Python no assunto - ajuda a tornar essa tarefa mais agradável.

## Alguns dos métodos utilizados na manipulação dos dados nessa análise
```
pd.read_csv
.info()
.dtypes
.isnull()
.isna()
.sum()
.shape
.value_counts()
.query
.nunique()
.mean()
.std()
.round()
.max()
.between
.all
```
Utilizadas para responder por exemplo:
* Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.
* Há quantas mulheres com idade entre 26 e 35 anos no dataset?


## Objetivo

O objetivo deste desafio é extrair algumas informações quantitativas
que nos ajudem a compreender a natureza dos dados à disposição e ganhar alguns _insights_
sobre o _data set_.

Para isso, utilizaremos o _data set_ [Black Friday](https://codenation-challenges.s3-us-west-1.amazonaws.com/data-science-0/black_friday.csv)
disponibilizado originalmente pela [Analytics Vidhya](https://www.analyticsvidhya.com/) e acessível
publicamente através do [Kaggle](https://www.kaggle.com). O _data set_ traz algumas variáveis relativas à transações comerciais
realizadas durante a Black Friday em uma determinada loja de varejo. Cada observação é relativa
a um determinado item comprado por um usuário e um usuário pode ter comprado mais de um item.

## Tópicos

Neste desafios nós vamos explorar:

* Python
* Pandas
* Jupyter notebook

