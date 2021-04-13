# @Time : 2021/4/1016:15
# @Author : 周云鹏
# @File : gensim_词向量模型.PY


from gensim.models import Word2Vec
import pandas as pd


texts = [['human', 'interface', 'computer'],
         ['survey', 'user', 'computer', 'system', 'response', 'time'],
         ['eps', 'user', 'interface', 'system'],
         ['system', 'human', 'system', 'eps'],
         ['user', 'response', 'time'],
         ['trees'],
         ['graph', 'trees'],
         ['graph', 'minors', 'trees'],
         ['graph', 'minors', 'survey']]

w = Word2Vec(texts, vector_size=5, window=1, min_count=0)

print(w.wv['human'])