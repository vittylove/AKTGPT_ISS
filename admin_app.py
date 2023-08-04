import os
import streamlit as st

def admin_website():
    st.title("ASKGPT_Admin")

    # 获取当前工作目录
    current_dir = os.getcwd()

    # 设置子文件夹路径
    doc_dir = os.path.join(current_dir, "data")

    # 显示文件列表
    st.subheader("文件列表")

    file_list = os.listdir(doc_dir)

    for file_name in file_list:
        file_path = os.path.join(doc_dir, file_name)
        st.write(f"{file_name}<hr style='margin-top:-5px;margin-bottom:5px;border:0;height:1px;background-color:gray'>", unsafe_allow_html=True)
    
    # 上传文件
    st.subheader("上传文件")
    uploaded_file = st.file_uploader("选择要上传的文件", type=["pdf", "txt"])

    if uploaded_file is not None:
        file_path = os.path.join(doc_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())
        st.success("文件上传成功。")

if __name__ == '__main__':
    admin_website()
