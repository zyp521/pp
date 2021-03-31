import pandas as pd
import jieba
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB,GaussianNB
from pyecharts.charts import Pie,WordCloud
import pyecharts.options as opts


# 分析问题：
#   1.好评、一般和差评占比
#   2.找出评论关键词
#   3.训练评论识别模型，验证模型准确率

data = pd.read_excel(io='./statics/douluo_comment.xlsx', index_col=0, )
data.columns = ('ids', 'comment', 'type')
data = data[['comment', 'type']].drop_duplicates(subset='comment', keep='first')
data.index = [i for i in range(data.shape[0])]


#    1.好评、一般和差评占比
out1 = data.groupby(by='type')['comment'].agg('count')
x_data = out1.index
y_data = out1.values.tolist()  # 注意pyecharts数据不识别numpy数据类型数据
data_pair = [i for i in zip(x_data, y_data)]
data_pair.sort(key=lambda x: x[1])
pie = Pie(init_opts=opts.InitOpts(width="800px", height="400px", bg_color="#2c343c"))
pie.add(series_name='斗罗真人版评论', data_pair=data_pair, rosetype="radius",
        radius="55%",
        center=["50%", "50%"],
        label_opts=opts.LabelOpts(is_show=False, position="center"),)
pie.set_global_opts(
        title_opts=opts.TitleOpts(
            title="斗罗真人版评论占比图",
            pos_left="center",
            pos_top="20",
            title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
        ),
        legend_opts=opts.LegendOpts(is_show=False),
    )
pie.set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        ),
        label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
    )
# pie.render('./templates/douluo_comment_zb.html') # 生成网页版图标
comment_zbt = pie.render_embed()


#   2.找出评论关键词，使用jieba配合词云图展示
out2 = data['comment']
words_list = jieba.lcut(''.join(out2))


# 停用词去除
stop_words =[]
with open('./statics/cn_stopwords.txt', encoding='utf-8') as f:
    for i in f:
        i = i.strip()
        stop_words.append(i)
        if i in words_list:
            while words_list.count(i):
                words_list.remove(i)

cv = CountVectorizer()  # 创建词袋数据结构
cv_fit = cv.fit_transform(words_list)
# print(cv.get_feature_names())  # 列表形式呈现文章生成的词典
# print(cv.vocabulary_)  # {词，词频}
words = list(cv.vocabulary_.items())

# 创建词云图
wc = WordCloud()
wc.add('评价词云图', words, word_size_range=[20, 100],
       textstyle_opts=opts.TextStyleOpts(font_family="cursive"))
comment_wordcloud = wc.render_embed()

# 3.训练评论识别模型，验证模型准确率
print(data)
data_ = [' '.join(jieba.cut(i))for i in data['comment']] # 生成包含所有的空格分割的文本字符串的列表
# 词频统计
# cv = CountVectorizer(stop_words=stop_words)
# out = cv.fit_transform(data_).toarray()
# print(cv.get_feature_names())



# 词频逆词频处理
cv_tfidf = TfidfVectorizer(stop_words=stop_words)
out = cv_tfidf.fit_transform(data_).toarray()

# 使用多项式朴素贝叶斯简历评论分析模型
# nb = MultinomialNB()
nb = GaussianNB()
x_train, x_test, y_train, y_test = train_test_split(out, data['type'], test_size=0.2, random_state=1)
nb.fit(x_train, y_train)
print(nb.score(x_test, y_test))
