# -*- coding:utf-8 -*-
# @Time : 2020/12/8 0008 18:47
# 文件名称 lagou_spider.py
# 开发人员  周云鹏
# 开发环境 PyCharm

import requests

base_url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false'

headers = {
     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    # 'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'user_trace_token=20201208182106-e3de3bee-b8cb-4d02-8d81-29f926603889; _ga=GA1.2.542631647.1607422869; LGUID=20201208182107-1990c865-685f-4987-a4fc-715b81848f77; sajssdk_2015_cross_new_user=1; _gid=GA1.2.653353218.1607422883; gate_login_token=d5e2bc451a339f86082f7566343cda9ed7729ab80800f7252a920f230ccef58b; LG_LOGIN_USER_ID=8de14245ad862c06caea5c0b6c8790c1273a78e50e3bdc346f7599ac36ca1dce; LG_HAS_LOGIN=1; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; privacyPolicyPopup=false; index_location_city=%E5%8C%97%E4%BA%AC; RECOMMEND_TIP=true; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1607422869,1607430536; LGSID=20201208202854-b6486e9f-e1e6-4511-b6ba-bc1cb7db94ee; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fother.php%3Fsc.060000aFQ4IwZlengVQK54KhCt0ticSr5XHGkITvNxSmIB%5FcI5D2QOG2if%5F-UxpvPOPRUBmLXZaB5T7I0CK07M0XLgngJH1HoUoYP9DMDmNpYayAUe2b-bIOeEqTwClnFOxu%5FqRKZdDi3vs6P-rGLOLlGBnbx2-rwHcSTKBl0UB8rin58AXkgwLdu-zg1H4siBfJJ3PDIpkS6QjvrrZmVuYzE4do.7Y%5FNR2Ar5Od663rj6tJQrGvKD77h24SU5WudF6ksswGuh9J4qt7jHzk8sHfGmYt%5FrE-9kYryqM764TTPqKi%5FnYQZHuukL0.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqs2v4VnL30ZN1ugFxIZ-suHYs0A7bgLw4TARqnsKLULFb5TaV8UHPS0KzmLmqnfKdThkxpyfqnHRznWf3PHRsnsKVINqGujYkn16Ln1TkP0KVgv-b5HDsP1bvnWmv0AdYTAkxpyfqnHDdn1f0TZuxpyfqn0KGuAnqiDFK0APzm1Ykn1RsP6%26ck%3D5996.3.142.426.155.554.156.240%26dt%3D1607430524%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26tpl%3Dtpl%5F11534%5F23295%5F19442%26l%3D1522485503%26us%3DlinkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520-%252520%2525E4%2525BA%252592%2525E8%252581%252594%2525E7%2525BD%252591%2525E9%2525AB%252598%2525E8%252596%2525AA%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%25258B%252589%2525E5%25258B%2525BE%21%2526linkType%253D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm%5Fsource%3Dm%5Fcf%5Fcpt%5Fbaidu%5Fpcbt; _putrc=18E12A446CB24BC2123F89F2B170EADC; JSESSIONID=ABAAABAABEIABCI38E944C02BFB317EC4F277BA32D9B2BA; login=true; unick=%E5%91%A8%E4%BA%91%E9%B9%8F; WEBTJ-ID=20201208202904-17642539ba97d9-027c516824a92a-3b3d5203-1049088-17642539baa85f; sensorsdata2015session=%7B%7D; X_HTTP_TOKEN=cfad7cdcf85b5c7d76503470617b544368ecdb81fe; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216389941%22%2C%22%24device_id%22%3A%2217641deb39d6f2-0c9e5db086d1b6-3b3d5203-1049088-17641deb39e8ac%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2286.0.4240.198%22%2C%22lagou_company_id%22%3A%22%22%7D%2C%22first_id%22%3A%2217641deb39d6f2-0c9e5db086d1b6-3b3d5203-1049088-17641deb39e8ac%22%7D; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1607430570; TG-TRACK-CODE=search_code; LGRID=20201208203551-6182cf28-904a-44fb-bb33-a8bc3b53ef5d; SEARCH_ID=cceaa5d5de7341a8b3165ab9ec45a361',
    # 'origin': 'https://www.lagou.com',
    'referer': 'https://www.lagou.com/jobs/list_python/p-city_0?px=default'
}

data = {
    'first': 'true',
    'pn': '1',
    'kd': 'python',

}

sess = requests.session()
sess.get('https://www.lagou.com/jobs/list_Python?labelWords=&fromSearch=true&suginput=')
sess.headers.update(headers)
response = sess.post(url=base_url, headers=headers, data=data)
print(response.json())