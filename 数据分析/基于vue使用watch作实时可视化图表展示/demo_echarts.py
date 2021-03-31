from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker


c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("销售额", Faker.values())
    .set_global_opts(title_opts=opts.TitleOpts(title="测试实例", subtitle="xxxxx"))
    .render("./templates/bar_base.html")
)