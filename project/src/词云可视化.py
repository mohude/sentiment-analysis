from wordcloud import WordCloud
import matplotlib.pyplot as plt
from random import randint

# 定义自定义的颜色函数
def random_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl({}, 100%, 50%)".format(randint(0, 360))  # 随机生成hsl颜色值

# 读取segmented_comments.txt文件中的评论内容
with open('segmented_comments.txt', 'r', encoding='utf-8') as file:
    comments = file.readlines()

# 合并评论成一个字符串，并去除停用词
stop_words = ['的', '是', '在', '有', '和', '就', '不', '人']  # 停用词列表
text = ' '.join([' '.join([word for word in comment.strip().split() if word not in stop_words]) for comment in comments])

# 生成词云
wordcloud = WordCloud(
    width=1000,
    height=800,
    background_color='white',
    font_path='simhei.ttf',
    max_font_size=150,
    color_func=random_color_func  # 使用自定义的颜色函数
).generate(text)

# 显示词云
plt.figure(figsize=(12, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
