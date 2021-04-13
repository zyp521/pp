from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer

test_a = ['天天 爱 LOL',
          '爱 玩 游戏',
          '我 是 男生',
          '男生 ',
          '爸爸 也 爱 玩 lol'
          ]
tf = TfidfVectorizer()
print(tf.fit_transform(test_a).toarray())
print(tf.vocabulary_)  # 返回columns字段字典

test_b = ['爸爸 也 爱 玩 lol']
print(tf.transform(test_b).toarray())  # 以test_a数据创建的词袋模型，一一查找新文本的分词结果，
                                       # 匹配上填充单体基于新文档，总体文档基于测试集算的的tf-idf值
                                       # 新文档有的，而词袋模型没有的词填充为0,不影响原模型

test_c = ['爸爸 也 爱 玩 lol','爸爸 也 爱 玩 lol']
print(tf.transform(test_c))  # 以test_a数据创建的词袋模型，一一查找新文本，匹配上有数，匹配不上为0


# test_a = ['天天 爱 LOL',
#           '爱 玩 游戏',
#           '我 是 男生',
#           '男生 ',
#          '爸爸 也 爱 玩 lol'
#           ]
# tf = CountVectorizer()
# print(tf.fit_transform(test_a).toarray())
# print(tf.vocabulary_)  # 返回columns字段字典
#
# test_b = ['爸爸 爸爸 爱 玩 lol']
# print(tf.transform(test_b).toarray())  # 以test_a数据创建的词袋模型，一一查找新文本，匹配上有数，匹配不上为0,不影响原模型
# test_c = ['爸爸 爸爸 爱 玩 lol']
# print(tf.transform(test_c).toarray())  # 以test_a数据创建的词袋模型，一一查找新文本，匹配上有数，匹配不上为0
