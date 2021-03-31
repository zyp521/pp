import os
import pandas as pd
import jieba
from sklearn.preprocessing import LabelEncoder  # 标签编码
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer  # 能够完成词频向量化+去除停用词
from sklearn.naive_bayes import MultinomialNB  # 多项式朴素贝叶斯
from sklearn.metrics import recall_score, precision_score, accuracy_score, f1_score  # 评估指标召回率，精确率, 准确率,f1[0,1]


# import xgboost

# 1.数据读取--获取数据
def read_text(base_dir_path, encoding='gbk'):
    '''
    :param base_dir_path: 包含所有文件的路径
    :return: dataFrame
    '''
    text_list = []
    # base_dir_path = './text_classification-master/text classification/train'
    list_dirs = os.listdir(base_dir_path)
    for i in list_dirs:
        file_path = os.path.join(base_dir_path, i)
        for j in os.listdir(file_path):
            try:
                with open(file_path + '/' + j, encoding=encoding) as f:
                    text_list.append([f.read(), i])
            except Exception as error:
                print(f'{file_path + "/" + j}文件读取失败')
                print(error)
    return pd.DataFrame(text_list, columns=['text', 'label'])


# 2.分词------数据分析与处理

def cut_word(text):
    '''
    :param text: 待处理的文本序列
    :return: 处理后的文本序列
    '''
    return [' '.join(jieba.cut(i)) for i in text]


# 3. 停用词
stopword = [i.strip() for i in
            open('./text_classification-master/text classification/stop/stopword.txt', encoding='utf-8').readlines()]


# 4.编码器处理文本标签--数据分析与处理
def label_encode(label):
    '''
    :param label: 待处理的标签序列
    :return: 处理后的标签序列
    '''
    le = LabelEncoder()
    e = le.fit_transform(label)
    print(dict(list(enumerate(le.classes_))))
    return e


if __name__ == '__main__':
    train = read_text('./text_classification-master/text classification/train')
    test = read_text('./text_classification-master/text classification/test')
    # print(train)
    # print(test)
    train['text'] = cut_word(train['text'])
    test['text'] = cut_word(test['text'])
    print(train)
    print(test)
    train['label_'] = label_encode(train['label'])
    test['label_'] = label_encode(test['label'])
    print(train)
    print(test)

    # 5.词频向量化---特征工程与选择
    # 5.1使用tf - idf处理数据 ------------------------- 使用测试集评分0.8左右
    # tf_idf = TfidfVectorizer(stop_words=stopword)  # 停用词处理
    # tf_idf.fit(list(train['text']) + list(test['text']))
    # train_x = tf_idf.transform(train['text']).toarray()
    # test_x = tf_idf.transform(test['text']).toarray()
    # print(train_x)
    # print(test_x)

    # 5.2 使用onehot_encode处理 ------------------------- 使用测试集评分0.9左右（不知道为啥比tf-idf效果好）
    counter = CountVectorizer(stop_words=stopword)
    counter.fit(list(train['text']) + list(test['text']))
    train_x = counter.transform(train['text']).toarray()
    test_x = counter.transform(test['text']).toarray()
    print(counter.vocabulary_)  # 词频统计

    # 6.模型建立------算法模型
    nb = MultinomialNB()
    nb.fit(train_x, train['label_'])
    test_pre = nb.predict(test_x)

    # 7.模型评估与优化-----性能评估/参数优化
    # 得分=准确率
    # print(nb.score(test_x, test['label_']))
    # # 准确率
    # print(f'准确率：{accuracy_score(test["label_"], test_pre)}')
    # # 精确率
    # print(f'精确率：{precision_score(test["label_"], test_pre, average="weighted")}')
    # # 召回率
    # print(f'召回率：{recall_score(test["label_"], test_pre, average="weighted")}')
    # # f1_score
    # print(f'f1：{f1_score(test["label_"], test_pre, average="weighted")}')

    # PR曲线/ROC曲线

    # 8. 新文本预测
    new_text = read_text('./text_classification-master/text classification/new_text', encoding='utf-8')
    new_text['text'] = cut_word(new_text['text'])
    # print(new_text[''])
    new_text_x = counter.transform(new_text['text']).toarray()
    print(new_text_x)
    map_dict = {0: '体育', 1: '女性', 2: '文学', 3: '校园'}
    print(f'预测结果为：{[map_dict[i] for i in nb.predict(new_text_x)]}')
