# 路由
from views import *

urlpatterns = [
    (r'/carindex1/', CarIndex1),
    (r'/vuetest/', VueHandler),
    (r'/vueajax/', VueAjaxHandler),
    (r'/carindex2/', CarIndex2),
    (r'/carjson/', CarJsonHandler),
    (r'/carindex3/', CarIndex3),
    (r'/carjson3/', CarJson3Handler),
    (r'/carindex4/', CarIndex4),
    (r'/carjson4/', CarJson4Handler),
    (r'/carindex5/', CarIndex5),
    (r'/carjson5/', CarJson5Handler),
]
