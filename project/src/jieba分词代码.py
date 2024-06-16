import pandas as pd
import jieba

# 读取 Excel 文件
file_path = 'comments.xlsx'  # 替换为你的文件路径
sheet_name = 'Sheet1'  # 替换为你的工作表名称，默认读取第一个工作表
column_name = 'Comment'  # 替换为包含评论的列名称

# 使用 pandas 读取 Excel 文件
df = pd.read_excel(file_path, sheet_name=sheet_name)

# 确认读取的列名
print(df.columns)

# 读取评论数据
comments = df[column_name].dropna().tolist()  # 去除空值并转换为列表

# 对每条评论进行分词并保存结果到一个新文件中
output_file_path = 'segmented_comments.txt'  # 分词结果保存路径
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for comment in comments:
        words = jieba.lcut(comment.strip())  # 使用精确模式分词
        output_file.write(' '.join(words) + '\n')

print(f"分词结果已保存到 {output_file_path}")
