import streamlit as st

st.title("Ứng dụng đầu tiên của tôi")
st.write("Chào mừng bạn đến với app Streamlit!")

name = st.text_input("Nhập tên của bạn:")
if name:
    st.write(f"Xin chào {name}!")
