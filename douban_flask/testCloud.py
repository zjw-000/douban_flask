# -*- coding:utf-8 -*-
"""
作者：z'j'w
日期：2022年08月31日
"""
import jieba        # 分词
from matplotlib import pyplot as plt    # 绘图，数据可视化
from wordcloud import WordCloud         # 词云
from PIL import Image                   # 图片处理
import numpy as np                      # 矩阵运算
import sqlite3                          # 数据库

# 准备词云所需的文字（词）
con = sqlite3.connect('movie.db')
cur = con.cursor()
sql = 'select instroduction from movie250'
data = cur.execute(sql)
text = ""
for item in data:
    text = text + item[0]
cur.close()
con.close()

# 分词
cut = jieba.cut(text)
string = ' '.join(cut)
print(len(string))

img = Image.open(r'.\static\assets\img\tree.jpg')
img_array = np.array(img)
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path='msyh.ttc',  # 字体所在位置：C:\Windows\Fonts
    stopwords=['的', '是', '你', '了', '都', '就是', '在', '和', '我']
)
wc.generate_from_text(string)


# 绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')     # 是否显示坐标轴

# plt.show()      # 显示生成的词云图片
# 输出词云图片到文件
plt.savefig(r'.\static\assets\img\word.jpg', dpi=500)
