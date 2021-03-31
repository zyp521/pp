# 新文本预测
from text_classific import cut_word, read_text
import joblib

counter = joblib.load('counter_model')
nb = joblib.load('nb_model')


def new_text_pre():
    '''
    :param filepath:
    :return: 返回分类结国列表
    '''
    new_text = read_text('./text_classification-master/text classification/new_text', encoding='utf-8')
    new_text['text'] = cut_word(new_text['text'])
    new_text_x = counter.transform(new_text['text']).toarray()
    map_dict = {0: '体育', 1: '女性', 2: '文学', 3: '校园'}
    print(f'预测结果为：{[map_dict[i] for i in nb.predict(new_text_x)]}')


if __name__ == '__main__':
    new_text_pre()
