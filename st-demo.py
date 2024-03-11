
import altair as alt
import folium
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_folium import folium_static
from pymongo import MongoClient
from datetime import datetime, timedelta
from enums import AccountType
from enums import BillType
from enums import categories
def create_map():
    # 创建地图
    m = folium.Map(location=[39.9042, 116.4074], zoom_start=5)

    # 添加坐标点和地理位置信息 TODO 定义Schema，然后for range传入
    locations = {
        'City': ['北京', '成都', '重庆', '凤凰', '哈尔滨', '牡丹江', '天津', '厦门', '福州', '深圳', '汕头', '潮州',
                 '南充', '乐山', '雅安', '眉山', '甘孜'],
        'Info': ['天安门', '东郊记忆', '洪崖洞', '凤凰古城', '哈尔滨', '雪乡', '天津之眼', '厦门岛', '平潭岛', '深圳湾',
                 '南澳岛', '潮州古城', '南充', '乐山', '雅安', '印象水街', '新都桥'],
        'Latitude': [39.9042, 30.5728, 29.5597, 27.9483, 45.757, 45.2751, 39.1247, 24.4798, 25.5232, 22.5295, 22.4747,
                     23.6655, 30.8373, 29.5521, 29.9805, 30.6701, 30.809],
        'Longitude': [116.4074, 104.0668, 106.5749, 109.5996, 126.652, 126.9744, 117.2003, 118.0894, 119.7837, 113.981,
                      114.4659, 116.6221, 106.1101, 103.7656, 103.0132, 104.1019, 102.5949],
    }

    df = pd.DataFrame(locations)

    for index, row in df.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=row['City'],
            tooltip=row['Info']
        ).add_to(m)

    return m


# markdown
st.markdown('Streamlit Demo')

# 设置网页标题
st.title('一个傻瓜式构建可视化 web的 Python 神器 -- streamlit')

x = st.slider("Select a value")
st.write(x, "squared is", x * x)

# 展示一级标题
st.header('1. 安装')

st.text('和安装其他包一样，安装 streamlit 非常简单，一条命令即可')
code1 = '''pip3 install streamlit'''
st.code(code1, language='bash')

# 展示一级标题
st.header('2. 使用')

# 展示二级标题
st.subheader('2.1 生成 Markdown 文档')

# 纯文本
st.text('导入 streamlit 后，就可以直接使用 st.markdown() 初始化')

# 展示代码，有高亮效果
code2 = '''import streamlit as st
st.markdown('Streamlit Demo')'''
st.code(code2, language='python')

st.header("3. 添加指标")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
col4.metric("Visibility", "10 miles", "2%")

st.header("4. 添加表格")
df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('第%d列' % (i + 1) for i in range(5))
)
st.table(df)

st.header("5. 添加图片")
st.image("https://twitter.com/golang")

st.header("6. 添加地图-成都")
df = pd.DataFrame(
    np.random.randn(100, 2) / [10, 10] + [30.76, 104.1],
    columns=['lat', 'lon'])
st.map(df)

st.header("7. 添加一起去过的城市")

# 创建包含城市和对应经纬度的数据框
# data = {
#     'info': ['北京', '成都', '重庆'],
#     'size': 500,
#     'lat': [39.9042, 30.5728, 29.4316],
#     'lon': [116.4074, 104.0668, 106.9123]
# }
# df = pd.DataFrame(data)
# st.map(df)

st.markdown('<h2>地图</h2>', unsafe_allow_html=True)
folium_map = create_map()
folium_static(folium_map)

#
st.header("8. 添加一个旋转的圆")
num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
.mark_point(filled=True)
.encode(
    x=alt.X("x", axis=None),
    y=alt.Y("y", axis=None),
    color=alt.Color("idx", legend=None, scale=alt.Scale()),
    size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
))

st.header("9. 魔术方法")
# Draw a title and some text to the app:
'''
# This is the document title

This is some _markdown_.
'''

df = pd.DataFrame({'col1': [1, 2, 3]})
df  # <-- Draw the dataframe

x = 10
'x', x  # <-- Draw the string 'x' and then the value of x

st.header("10. 引入进度条")
'Starting a long computation...'

# Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0)
#
# for i in range(100):
#     # Update the progress bar with each iteration.
#     latest_iteration.text(f'Iteration {i + 1}')
#     bar.progress(i + 1)
#     time.sleep(0.1)
#
# '...and now we\'re done!'


st.header("11. 添加数据库")

# 连接MongoDB
client = MongoClient("mongodb://localhost:27017")  # 根据实际情况修改MongoDB的连接地址和端口
db = client["db_finance"]  # 修改为实际的数据库名称
collection = db["my_wallet"]  # 修改为实际的集合名称

# 插入数据
# data = [
#     {"日期": "2022-01-01", "备注": "购物", "收入支出": "支出", "一级类型": "日常", "二级类型": "食品", "金额": 100, "账户": "现金"},
#     {"日期": "2022-01-02", "备注": "工资", "收入支出": "收入", "一级类型": "收入", "二级类型": "工资", "金额": 2000, "账户": "银行卡"},
#     {"日期": "2022-01-03", "备注": "餐饮", "收入支出": "支出", "一级类型": "日常", "二级类型": "餐饮", "金额": 50, "账户": "支付宝"},
#     {"日期": "2022-01-04", "备注": "交通", "收入支出": "支出", "一级类型": "日常", "二级类型": "交通", "金额": 20, "账户": "微信"},
#     {"日期": "2022-01-05", "备注": "奖金", "收入支出": "收入", "一级类型": "收入", "二级类型": "奖金", "金额": 500, "账户": "现金"},
# ]
#
# collection.insert_many(data)
# 从MongoDB读取数据
data = collection.find()

# 将数据转换为列表形式
data_list = list(data)

# 在Streamlit应用中显示数据表格
st.write("MongoDB 数据示例:")

# 创建日期范围筛选器
end_date = datetime.now().date()
start_date = end_date - timedelta(days=30)  # 默认选择最近30天的数据
selected_start_date = st.date_input("选择起始日期", value=start_date, max_value=end_date)
selected_end_date = st.date_input("选择结束日期", value=end_date, max_value=end_date)

# 创建筛选项
accounts = list(set([item["账户"] for item in data_list]))
accounts.insert(0, "")  # 添加一个空字符串作为默认选项
selected_account = st.selectbox("选择账户", accounts)

# 筛选数据
filtered_data = []

for item in data_list:
    item_date = datetime.strptime(item["日期"], "%Y-%m-%d").date()
    if selected_start_date <= item_date <= selected_end_date:
        if selected_account and item["账户"] != selected_account:
            continue
        filtered_data.append(item)

# 显示数据表格
st.table(filtered_data)

st.header("12. 添加账单")

# 在Streamlit应用中显示表单
st.write("手动录入账单")
# 提取一级类型名称列表
category_level1_options = [category["name"] for category in categories if category["level"] == 1]

# 获取用户输入
category_level1 = st.selectbox("一级类型", category_level1_options)

# 根据一级类型的选择提取相应的二级类型名称列表
for _category in categories:
    _category.get("name", category_level1)
category_level2_options = [category["name"] for category in categories if category["level"] == 2 and category["type"] == category_level1]

category_level2 = st.selectbox("二级类型", category_level2_options)

date = st.date_input("日期")
account = st.selectbox("账户", [at for at in AccountType])
bill_type = st.selectbox("类型", [bt for bt in BillType])

amount = st.number_input("金额", value=0.0, step=0.01)
description = st.text_input("描述")

# 提交按钮
if st.button("提交"):
    # 创建账单对象
    bill = {
        "日期": str(date),
        "账户": account,
        "类型": bill_type,
        "一级类型": category_level1,
        "二级类型": category_level2,
        "金额": amount,
        "描述": description
    }

    # 将账单插入MongoDB
    collection.insert_one(bill)

    st.success("账单已成功录入")
