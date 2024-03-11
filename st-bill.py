import streamlit as st
from pymongo import MongoClient
from datetime import datetime, timedelta
from enums import AccountType
from enums import BillType
from enums import categories
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import plotly.graph_objects as go

# 设置中文字体
font_path = '/System/Library/Fonts/Supplemental/Arial Unicode.ttf'  # 替换为你的字体文件路径
font_prop = font_manager.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()

# 连接MongoDB
client = MongoClient("mongodb://localhost:27017")  # 根据实际情况修改MongoDB的连接地址和端口
db = client["db_finance"]  # 修改为实际的数据库名称
collection = db["my_wallet"]  # 修改为实际的集合名称

st.header("1. 添加账单")

# 在Streamlit应用中显示表单
st.write("手动录入账单")
# 提取一级类型名称列表
category_level1_options = [category["name"] for category in categories if category["level"] == 1]

# 获取用户输入
category_level1 = st.selectbox("一级类型", category_level1_options)

category_level2_options = []
# 根据一级类型的选择提取相应的二级类型名称列表
for _category in categories:
    if _category.get("name") == category_level1:
        _categories = _category.get("sub")
        category_level2_options = [category["name"] for category in _categories]

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

st.header("2. 查询账单")
# 创建一个按钮用于重新查询

# 创建日期范围筛选器
end_date = datetime.now().date()
start_date = end_date - timedelta(days=30)  # 默认选择最近30天的数据
selected_start_date = st.date_input("选择起始日期", value=start_date, max_value=end_date)
selected_end_date = st.date_input("选择结束日期", value=end_date, max_value=end_date)

# 创建筛选项
accounts = list(set([item for item in AccountType]))
accounts.insert(0, "")  # 添加一个空字符串作为默认选项
selected_account = st.selectbox("选择账户", accounts)


def read_bills():
    # 从MongoDB读取数据
    data = collection.find()

    # 将数据转换为列表形式
    data_list = list(data)

    filtered_data = []

    # 筛选数据

    for item in data_list:
        item_date = datetime.strptime(item["日期"], "%Y-%m-%d").date()
        if selected_start_date <= item_date <= selected_end_date:
            if selected_account and item["账户"] != selected_account:
                continue
            filtered_data.append(item)

    return filtered_data


filtered_data = read_bills()

if st.button("重新查询"):
    # 重新查询的逻辑
    filtered_data = read_bills()

# 排序
filtered_data = sorted(filtered_data, key=lambda x: datetime.strptime(x["日期"], "%Y-%m-%d"), reverse=True)
st.table(filtered_data)


st.header("3. 统计数据")

# 统计每日不同类型的消费
daily_expenses = {}

for item in filtered_data:
    date = item["日期"]
    expense_type = item["二级类型"]
    amount = item["金额"]

    if date not in daily_expenses:
        daily_expenses[date] = {}

    if expense_type not in daily_expenses[date]:
        daily_expenses[date][expense_type] = 0

    daily_expenses[date][expense_type] += amount

# 提取日期和类型
dates = sorted(daily_expenses.keys())
expense_types = sorted(set(expense_type for expenses in daily_expenses.values() for expense_type in expenses.keys()))

# 创建条形图
plt.figure(figsize=(10, 6))
for expense_type in expense_types:
    amounts = [daily_expenses[date].get(expense_type, 0) for date in dates]
    plt.bar(dates, amounts, label=expense_type)

# 设置图表标题和标签
plt.title("每日不同类型的消费统计（条形图）")
plt.xlabel("日期")
plt.ylabel("消费金额")

# 添加图例
plt.legend()

# 显示条形图
st.pyplot(plt)

# 创建折线图
plt.figure(figsize=(10, 6))
for expense_type in expense_types:
    amounts = [daily_expenses[date].get(expense_type, 0) for date in dates]
    plt.plot(dates, amounts, label=expense_type)

# 设置图表标题和标签
plt.title("每日不同类型的消费统计（折线图）")
plt.xlabel("日期")
plt.ylabel("消费金额")

# 添加图例
plt.legend()

# 显示折线图
st.pyplot(plt)

# 创建饼状图
plt.figure(figsize=(10, 6))
for date, expenses in daily_expenses.items():
    total_amount = sum(expenses.values())
    plt.pie(expenses.values(), labels=expenses.keys(), autopct='%1.1f%%')
    plt.title(f"日期: {date}, 总消费金额: {total_amount}")

# 显示饼状图
st.pyplot(plt)


st.header("4. 月度消费统计")

# 统计每日不同类型的消费
daily_expenses = {}

for item in filtered_data:
    date = item["日期"]
    expense_type = item["二级类型"]
    amount = item["金额"]

    if date not in daily_expenses:
        daily_expenses[date] = {}

    if expense_type not in daily_expenses[date]:
        daily_expenses[date][expense_type] = 0

    daily_expenses[date][expense_type] += amount

# 提取日期和类型
dates = sorted(daily_expenses.keys())
expense_types = sorted(set(expense_type for expenses in daily_expenses.values() for expense_type in expenses.keys()))

# 创建条形图
fig = go.Figure()

for expense_type in expense_types:
    amounts = [daily_expenses[date].get(expense_type, 0) for date in dates]
    fig.add_trace(go.Bar(
        x=dates,
        y=amounts,
        name=expense_type,
        hovertemplate='<b>%{x}</b><br><br>' +
                      '类型: %{name}<br>' +
                      '消费金额: %{y}<br>',
    ))

# 设置图表标题和标签
fig.update_layout(
    title="每日不同类型的消费统计（条形图）",
    xaxis_title="日期",
    yaxis_title="消费金额"
)

# 显示图表
st.plotly_chart(fig)