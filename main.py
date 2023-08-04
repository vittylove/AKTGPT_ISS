import streamlit as st
from user_app import user_website
from admin_app import admin_website

def main():
    st.title("ASKGPT 应用")

    # 设置左侧应用名的宽度
    st.markdown('<style>div.row-widget.stRadio > div{flex-basis: 50%;}</style>', unsafe_allow_html=True)

    # 创建按钮并获取用户类型
    user_button_key = "user_button"
    admin_button_key = "admin_button"

    user_button_clicked = st.button("用户", key=user_button_key)
    admin_button_clicked = st.button("管理员", key=admin_button_key)

    # 判断按钮点击事件
    if user_button_clicked:
        st.empty()  # 清空主页面内容
        user_website()  # 显示用户页面
    elif admin_button_clicked:
        st.empty()  # 清空主页面内容
        admin_website()  # 显示管理员页面

if __name__ == '__main__':
    main()
