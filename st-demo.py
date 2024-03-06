import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import folium
from streamlit_folium import folium_static

def create_map():
    # 创建地图
    m = folium.Map(location=[39.9042, 116.4074], zoom_start=5)

    # 添加坐标点和地理位置信息
    locations = {
        'City': ['北京', '成都', '重庆', '凤凰古城', '哈尔滨', '雪乡'],
        'Latitude': [39.9042, 30.5728, 29.4316, 27.9483, 45.757, 45.2751],
        'Longitude': [116.4074, 104.0668, 106.9123, 109.5996, 126.652, 126.9744],
        'Info': ['北京天安门', '成都宽窄巷子', '重庆洪崖洞', '凤凰古城', '哈尔滨', '雪乡']
    }

    df = pd.DataFrame(locations)

    for index, row in df.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=row['Info'],
            tooltip=row['City']
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
