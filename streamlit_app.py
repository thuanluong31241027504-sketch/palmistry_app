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
# CSS - NỀN TÍM + CHỮ PALMISTRY FONT PIXEL
# ============================================
st.markdown("""
<style>
    /* Nền tím */
    .stApp {
        background: linear-gradient(135deg, #0a0a1a 0%, #1a0a2e 50%, #0a0a1a 100%);
        min-height: 100vh;
    }
    
    /* Font pixel */
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
    
    .palmistry-title {
        font-family: 'Press Start 2P', monospace;
        font-size: 2.5rem;
        text-align: center;
        color: #c084fc;
        letter-spacing: 2px;
        margin-top: 80px;
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
