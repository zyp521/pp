# -*- coding:utf-8 -*-
# @Time : 2020/12/15 0015 9:01
# 文件名称 7. 动态字体破译.py
# 开发人员  周云鹏
# 开发环境 PyCharm

from fontTools.ttLib import TTFont
import numpy as np
import requests
from io import StringIO,BytesIO
import base64
import json


# 比较两个数组的欧式距离
def compare_axis(axis1, axis2):
    # 以坐标（0，0）补填空缺
    if len(axis1) < len(axis2):
        axis1.extend([0, 0] for _ in range(len(axis2) - len(axis1)))
    elif len(axis2) < len(axis1):
        axis2.extend([0, 0] for _ in range(len(axis1) - len(axis2)))
    # 将列表转换为 Numpy 中的数组
    axis1 = np.array(axis1)
    axis2 = np.array(axis2)
    # 计算并返回欧式距离
    return np.sqrt(np.sum(np.square(axis1 - axis2)))


#  读取font信息
def read_font(path):
    '''
    :param path: 文件路径
    :return: 读取后的unicode；字体矩阵映射字典
    '''
    font = TTFont(path)
    series = font.getGlyphNames()
    arr_dict = {}
    for i in series:
        arr_dict[i] = list(font['glyf'][i].coordinates)
    del arr_dict['.notdef']
    return arr_dict


# 解析woff文件，返回解析后映射字典
def parse_font_code(woff_path):
    '''
    :param woff_name: 传入待解码woff文件路径
    :return: 解码后的{'unicode':num,...}
    '''

    #  生成基础矩阵字体映射
    base_dict = {
        'unia173': 6,
        'unie794': 3,
        'unif841': 2,
        'unia735': 0,
        'unif312': 8,
        'unif231': 1,
        'unic574': 9,
        'unic275': 4,
        'unic456': 5,
        'unif356': 7,
    }
    base_code_dict = read_font('2.woff')
    new_code_dict = read_font(woff_path)
    # print(new_code_dict)
    res_dict = {}
    for new_k, new_v in new_code_dict.items():
        res = float('inf')
        for base_k, base_v in base_code_dict.items():
            dis = compare_axis(new_v, base_v)
            if dis < res:
                res = dis
                res_dict[new_k] = base_k
    for i, v in res_dict.items():
        res_dict[i] = base_dict[v]
    return res_dict


if __name__ == '__main__':
    let_name = ['爷灬霸气傀儡', '梦战苍穹', '傲世哥', 'мaη肆風聲', '一刀メ隔世', '横刀メ绝杀', 'Q不死你R死你', '魔帝殤邪', '封刀不再战', '倾城孤狼', '戎马江湖', '狂得像风',
                '影之哀伤', '謸氕づ独尊', '傲视狂杀', '追风之梦', '枭雄在世', '傲视之巅', '黑夜刺客', '占你心为王', '爷来取你狗命', '御风踏血', '凫矢暮城', '孤影メ残刀',
                '野区霸王', '噬血啸月', '风逝无迹', '帅的睡不着', '血色杀戮者', '冷视天下']

    res_dict = {}
    # 获取网页胜点加密数据
    for i in [0, 1, 2]:
        print(i)
        base_url = f'http://match.yuanrenxue.com/api/match/7?page={i+1}'
        response = requests.get(base_url)
        victory_points_font = response.json()['woff']
        victory_points_data = response.json()['data']
        for v, k in enumerate(let_name[i*10:i*10+10]):
            res_dict[k] = victory_points_data[v]['value']
        font = BytesIO(base64.b64decode(victory_points_font))
        res_dict_str = json.dumps(res_dict)
        for v,k in parse_font_code(font).items():
            res_dict_str = res_dict_str.replace(f'&#x{v[3:]}', str(k))
        res_dict =json.loads(res_dict_str)

print(res_dict)

