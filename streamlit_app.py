import streamlit as st

# ============================================
# CẤU HÌNH TRANG
# ============================================
st.set_page_config(
    page_title="PALMISTRY",
    page_icon="",
    layout="centered"
)

# ============================================
# CSS - NỀN TÍM + CHỮ PALMISTRY FONT CODE
# ============================================
st.markdown("""
<style>
    /* Nền tím */
    .stApp {
        background: linear-gradient(135deg, #0a0a1a 0%, #1a0a2e 50%, #0a0a1a 100%);
        min-height: 100vh;
    }
    
    /* Font code */
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code&family=Source+Code+Pro&display=swap');
    
    .palmistry-title {
        font-family: 'Fira Code', 'Source Code Pro', monospace;
        font-size: 3rem;
        text-align: center;
        color: #c084fc;
        letter-spacing: 2px;
        margin-top: 80px;
        padding: 20px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# HIỂN THỊ CHỮ PALMISTRY
# ============================================
st.markdown("""
<div style="text-align: center;">
    <div class="palmistry-title">
        PALMISTRY
    </div>
</div>
""", unsafe_allow_html=True)
