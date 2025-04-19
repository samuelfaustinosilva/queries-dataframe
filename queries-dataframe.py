#!/usr/bin/env python
# coding: utf-8

# ### Bibliotecas

# In[9]:


get_ipython().system('pip install pandasql')


# In[23]:


import pandas as pd
from pandasql import sqldf


# ### Carregamento de Dados

# In[24]:


categories = pd.read_csv('categories.csv')


# In[25]:


categories


# In[26]:


products = pd.read_csv('products.csv')


# In[27]:


products


# ### Combinando as informações dos dataframes com linguagem SQL

# In[31]:


query = """

SELECT
p.id as product_id,
p.name as product_name,
p.price,
c.name as category_name 

FROM products p
JOIN categories c on c.id = p.category_id

"""


# In[32]:


resultado = sqldf(query)


# In[33]:


resultado


# In[ ]:




