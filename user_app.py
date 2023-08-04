import streamlit as st
from model import initialize_system
import time

@st.cache_resource
def initialize_pipe():
    return initialize_system()

def user_website():
    st.title("ASKGPT_User")

    # 添加输入框
    question = st.text_input("Please enter your question")

    # 添加提交按钮
    if st.button("Submit"):
        if question:
            # 显示加载动画
            with st.spinner('Loading...'):
                # 初始化系统
                pipe = initialize_pipe()

                # 获取问题答案
                answers = pipe.run(query=question)
                answer_results = answers["results"]

                # 检查阈值
                if answer_results:
                    document = answers["documents"][0]
                    threshold = 0.6  # 设置阈值为0.6
                    document_score = document.score
                    answer = answer_results[0]
                    # 模拟加载时间
                    time.sleep(2)
                    # 显示答案
                    st.subheader("Answer:")
                    st.markdown(
                        f'<div style="background-color: #f9f9f9; padding: 10px; border-radius: 5px;">{answer}</div>',
                        unsafe_allow_html=True,
                    )
                    if document_score < threshold:
                        # 可信度较低，提醒用户
                        st.warning("The reliability of the answer is low, please refer to it with caution.")
                else:
                    # 处理没有结果的情况
                    st.warning("No answer was found.")

def run():
    user_website()

if __name__ == '__main__':
    run()