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
# CSS - NỀN TÍM + CHỮ PALMISTRY
# ============================================
st.markdown("""
<style>
    /* Nền tím */
    .stApp {
        background: linear-gradient(135deg, #0a0a1a 0%, #1a0a2e 50%, #0a0a1a 100%);
        min-height: 100vh;
    }
    
    /* Chữ PALMISTRY to, rõ, pixel */
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
    
    .palmistry-title {
        font-family: 'Press Start 2P', monospace;
        font-size: 3rem;
        text-align: center;
        color: #c084fc;
        text-shadow: 0 0 5px #8b5cf6;
        letter-spacing: 4px;
        margin-top: 50px;
        padding: 20px;
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
