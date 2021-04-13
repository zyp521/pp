# @Time : 2021/4/916:45
# @Author : 周云鹏
# @File : gensim入门.PY

texts = [['human', 'interface', 'computer'],
         ['survey', 'user', 'computer', 'system', 'response', 'time'],
         ['eps', 'user', 'interface', 'system'],
         ['system', 'human', 'system', 'eps'],
         ['user', 'response', 'time'],
         ['trees'],
         ['graph', 'trees'],
         ['graph', 'minors', 'trees'],
         ['graph', 'minors', 'survey']]

# bow 词向量 ：Bag-of-Words model的缩写

from gensim import corpora

dictionary = corpora.Dictionary(texts)


# 语料预处理
# corpus = [dictionary.doc2bow(i) for i in texts]
def mycorpus():  # 迭代流式处理
    for i in texts:
        yield dictionary.doc2bow(i)


# tf-idf向量转换
from gensim import models

tfidf = models.TfidfModel(mycorpus())  # 接受的训练语料对象，应该是一个词袋模型稀疏向量的迭代器
print(tfidf[[(0, 1), (1, 1)]])  # 同样是出于内存的考虑，model[corpus]方法返回的是一个迭代器


# word2vec向量转换
from gensim.models import word2vec

# 引入日志文件
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# 引入数据集
raw_sentences = ["the quick brown fox jumps over the lazy dogs","yoyoyo you go home now to sleep"]

# 切分词汇
sentences = [i.encode('utf-8').split() for i in raw_sentences]
print(sentences)

# 构建模型
model = word2vec.Word2Vec(sentences, min_count=1,)

# 参数
# min_count : 较大的语料集中， 忽略只出现过一两次的单词，通过设置min_count参数进行控制，默认5，一般设置0~100之间
# size: 主要用来设置神经网络的层数，默认设置为100层，更大的设置意味着更多的输入数据，不过也能提升整体的准确度，合理的设置范围为 10~数百。
# workers: workers参数用于设置并发训练时候的线程数