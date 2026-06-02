import streamlit as st

st.set_page_config(layout="centered")

st.markdown("""
<style>
    .test-font {
        font-family: 'Courier New', monospace;
        font-size: 2rem;
        color: red;
    }
</style>
<div class="test-font">
    ABC 123
</div>
""", unsafe_allow_html=True)

st.write("Dòng này dùng font mặc định")
