# streamlit_practise
streamlit浅尝


### 项目准备

* 创建虚拟环境
```shell
python3 -m venv venv_streamlit
```
* 激活虚拟环境
```shell
source venv_streamlit/bin/activate
```
* 将依赖写入requirements.txt
```shell
pip3 freeze > requirements.txt

# 仅追加
pip3 freeze >> requirements.txt
```

### 教程
button：按钮
download_button：文件下载
file_uploader：文件上传
checkbox：复选框
radio：单选框
selectbox：下拉单选框
multiselect：下拉多选框
slider：滑动条
select_slider：选择条
text_input：文本输入框
text_area：文本展示框
number_input：数字输入框，支持加减按钮
date_input：日期选择框
time_input：时间选择框
color_picker：颜色选择器
  魔术方法
* st.title - 显示应用标题
* st.header - 显示主标题
* st.subheader - 显示副标题
* st.text - 显示文本
* st.markdown - 显示markdown文本
* st.code - 显示代码块
* st.write - 通用显示方法
* st.dataframe - 显示可交互数据帧
* st.table - 显示静态数据表
* st.json - 显示JSON对象
* st.pyplot - 显示matplotlib图表
* st.altair_chart - 显示Altair图表
* st.vega_lite_chart - 显示vega-lite图表
* st.plotly_chart - 显示plotly图表
* st.bokeh_chart - 显示Bokeh图表
* st.deck_gl_chart - 显示Deck.GL图表
* st.graphviz_chart - 显示graphviz图表
* st.line_chart - 显示折线图
* st.area_chart - 显示区域图
* st.bar_chart - 显示棒状图
* st.map - 显示地图
* st.image - 显示图像
* st.audio - 显示音频播放器
* st.video - 显示视频播放器
* st.button - 显示按钮
* st.checkbox - 显示复选框
* st.radio - 显示单选框
* st.selectbox - 显示列表选择框
* st.multiselect - 显示列表多选框
* st.slider - 显示滑动拉杆
* st.text_input - 显示文本输入框
* st.number_input - 显示数字输入框
* st.text_area - 显示多行文本输入框
* st.date_input - 显示日期输入框
* st.time_input - 显示时间输入框
* st.echo - 显示应用源代码
* st.progress - 显示进度
* st.spinner - 显示执行状态
* st.balloons - 显示庆祝气球
* st.error - 显示错误信息
* st.warning - 显示警告信息
* st.info - 显示提示信息
* st.success - 显示成功信息
* st.exception - 显示异常信息
* st.empty - 添加占位符
* st.help - 显示帮助信息
* st.get_option - 读取配置项的值
* st.set_option - 设置配置项的值
* st.cache - 函数缓存装饰器
* dg.add_rows - 追加数据行

### 平替
* [Bokeh官网](https://docs.bokeh.org/en/latest/index.html) - [Github](https://github.com/bokeh/bokeh)
* [Jupyter Voila](https://blog.jupyter.org/and-voil%C3%A0-f6a2c08a4a93)

### 参考资料
* [github地址](https://github.com/streamlit/streamlit?tab=readme-ov-file)
* [掘金教程](https://juejin.cn/post/7044757186064416798)
* [YouTube教程](https://www.youtube.com/watch?v=B2iAodr0fOo)
* [awesome streamlit](https://github.com/MarcSkovMadsen/awesome-streamlit)
* [开发手册](http://cw.hubwiz.com/card/c/streamlit-manual/)
* [画廊](https://streamlit.io/gallery)
* [官方文档](https://docs.streamlit.io/)
  * [数据源链接](https://docs.streamlit.io/knowledge-base/tutorials/databases)
    * [与MongoDB交互](https://docs.streamlit.io/knowledge-base/tutorials/databases/mongodb)
  * [高级特性](https://docs.streamlit.io/library/advanced-features)
  * [部署问题](https://docs.streamlit.io/knowledge-base/deploy)
