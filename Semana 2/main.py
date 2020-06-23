#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[3]:


import pandas as pd
import numpy as np


# In[4]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[5]:


black_friday.head(10)


# In[6]:


black_friday.info()


# In[7]:


#q1
black_friday.shape


# In[8]:


black_friday['Age'].value_counts()


# In[9]:


womans = black_friday.query("Age == '26-35' & Gender == 'F'")
print (womans['User_ID'].shape[0])


# In[10]:


black_friday['User_ID'].value_counts()


# In[11]:


print (black_friday.isnull().sum())


# In[12]:


black_friday['Product_Category_3'].value_counts()


# In[13]:


black_friday['Purchase'].value_counts()


# In[14]:


black_friday['Purchase'].mean()


# In[15]:


black_friday['Purchase'].std()


# In[16]:


nmlzd_bf_p = black_friday['Purchase'].mean()/black_friday['Purchase'].std()
nmlzd_bf_p


# In[17]:


#q5
q5 = black_friday.isna().sum() / black_friday.shape[0]
print (float(q5.max()))


# In[18]:


#q8
purch_norm = black_friday['Purchase']
purch_norm = (purch_norm - purch_norm.min()) / (purch_norm.max() - purch_norm.min())
print (float(purch_norm.mean()))


# In[19]:


#q9
purch_pad = black_friday['Purchase']
purch_pad = (purch_pad - purch_pad.mean()) / purch_pad.std()
    
print (purch_pad[purch_pad.between(-1, 1)].shape[0])


# In[20]:


#q10
category_null = black_friday[black_friday['Product_Category_2'].isna()][['Product_Category_2','Product_Category_3']]
print (bool(category_null.isnull().values.all()))


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[155]:


def q1():
    return black_friday.shape
    pass


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[72]:


def q2():
    mulh_age = black_friday.query("Age == '26-35' & Gender == 'F'")
    return (mulh_age['User_ID'].shape[0])
    pass


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[78]:


def q3():
    return (black_friday['User_ID'].nunique())
    pass


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[7]:


def q4():
    return black_friday.dtypes.nunique()
    pass


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[8]:


def q5():
    q5 = black_friday.isna().sum() / black_friday.shape[0]
    return float(q5.max())
    pass


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[9]:


def q6():
    return int (black_friday.isnull().sum().max())
    pass


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[10]:


def q7():
    return float(black_friday['Product_Category_3'].dropna().mode())
    pass


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[11]:


def q8():
    purch_norm = black_friday['Purchase']
    purch_norm = (purch_norm - purch_norm.min()) / (purch_norm.max() - purch_norm.min())
    return float(purch_norm.mean())
    pass


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[123]:


def q9():
    purch_pad = black_friday['Purchase']
    purch_pad = (purch_pad - purch_pad.mean()) / purch_pad.std()
    
    return purch_pad[purch_pad.between(-1, 1)].shape[0]
    pass


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[13]:


def q10():
    category_null = black_friday[black_friday['Product_Category_2'].isna()][['Product_Category_2','Product_Category_3']]
    return bool(category_null.isnull().values.all())
    pass

