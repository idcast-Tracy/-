# 打开网页，在cmd命令界面运行下面一段
# streamlit run C:\Users\Tracy\Desktop\2024寒假\科研\01.20Python-oneleaf\一叶知秋.py [ARGUMENTS]

import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd
import numpy as np
import os
# os.chdir(r'C:\Users\Tracy\Desktop\2024寒假\科研\01.18Python-streamlit') # 设定文件路径

# 设置页面配置
st.set_page_config(page_title="知秋的网站", page_icon="⭐", layout="wide")

# 通过 css样式隐藏主菜单和页脚
hide_menu = '''
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
'''
st.markdown(hide_menu,unsafe_allow_html=True)

# 配置左侧菜单项
with st.sidebar:
    choose = option_menu("知秋的网站", ["介绍", "图书", "数据可视化","音乐/视频"],
                         icons=['house', 'book-half', 'bar-chart', "boombox-fill"],
                         menu_icon="bullseye", default_index=0)

if choose == "介绍":
    st.title("欢迎来到知秋的网站")
    st.write("这是一个演示 Streamlit 页面配置的示例。")

elif choose == "图书":
    # 创建单独的容器，图片放入此容器中
    with st.container():
        # 将布局分为四列
        cols = st.columns(4)
        # 在第一列中添加图片，设置图片说明，并设置缩放比例
        cols[0].image("任务分配.png","重复做对的事",use_column_width=True)
        cols[1].image("任务分配.png","中产家庭理财清单",use_column_width=True)
        cols[2].image("任务分配.png","耐心的资本",use_column_width=True)
        cols[3].image("任务分配.png","纳瓦尔宝典",use_column_width=True)
    with st.container():
        # 将布局分为1列
        cols = st.columns(1)
        cols[0].image("任务分配.png", "小岛经济学", use_column_width=True)

elif choose == "数据可视化":
    # 结合Plotly来添加柱状图、饼图和折线图
    import plotly.express as px
    # 将图表分为三种
    selecte = option_menu(None, ["柱状图","饼图","折线图"],
                           icons=["bar-chart-fill","pie-chart-fill","graph-up"],
                           menu_icon="cast", default_index=0, orientation="horizontal")
    if selecte == "柱状图":
        # px.data.tips()`是Plotly Express提供的一个示例数据集，其中包含有关餐厅小费的数据它是一个DataFrame对象
        data_bar = px.data.tips()
        fig_bar = px.bar(data_bar, x='day', y='total_bill', color='sex')
        st.plotly_chart(fig_bar)

    elif selecte == "饼图":
        data_pie = px.data.tips()
        fig_pie = px.pie(data_pie, names='day')
        st.plotly_chart(fig_pie)

    elif selecte == "折线图":
        data_line = px.data.gapminder().query("country=='China'")
        fig_line = px.line(data_line, x='year', y='pop')
        st.plotly_chart(fig_line)

elif choose == "音乐/视频":
    selecte = option_menu(None, ["音乐", "视频"],
                          icons=["file-music-fill", "badge-vo-fill"],
                          menu_icon="cast", default_index=0, orientation="horizontal")
    if selecte == "音乐":
        st.write("1. 倩女幽魂")
        # st.audio("./music/倩女幽魂.mp3")
        st.write("2. 十年")
        # st.audio("./music/十年.mp3")
        st.write("3. 天路")
        # st.audio("./music/天路.mp3")

    elif selecte == "视频":
        st.video("S4.原型演示(视频)-赛题08-可视化AI模型平台-视界AI.mp4")
