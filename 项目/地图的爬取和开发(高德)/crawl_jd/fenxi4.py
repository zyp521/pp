#统计站台中命名最多的词
#画词云图
import jieba
from wordcloud import WordCloud
import pandas
from matplotlib import pyplot
subways=pandas.read_csv("subway.csv",names=["name","line","station"])
#思路：把每个station进行jieba分词,形成统一的jieba分词后的模式
#"天气 睛朗 "
text=""
for station in subways["station"]:
    text+=" ".join(jieba.cut(station,cut_all=True))
    text+=" "
background=pyplot.imread("rocket.jpg")
wc=WordCloud(
    background_color="white",
    mask=background,
    font_path="华康俪金黑W8.TTF",
    max_words=300,
    max_font_size=150,
    min_font_size=10,
    random_state=50
)
wc.generate_from_text(text)
wc.to_file("地铁站词云图.png")