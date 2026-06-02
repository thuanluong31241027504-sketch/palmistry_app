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
# CSS - BACKGROUND TÍM + FONT TERMINAL MAC
# ============================================
st.markdown("""
<style>
    /* Nền tím đậm giống terminal */
    .stApp {
        background: linear-gradient(135deg, #0a0a1a 0%, #1a0a2e 50%, #0a0a1a 100%);
        min-height: 100vh;
    }
    
    /* Font Terminal Mac - SF Mono hoặc Menlo */
    .palmistry-title {
        font-family: 'SF Mono', 'Menlo', 'Monaco', 'Courier New', monospace;
        font-size: 2.5rem;
        text-align: center;
        color: #c084fc;
        letter-spacing: 0px;
        margin-top: 80px;
        padding: 20px;
        font-weight: 400;
    }
    
    /* Thêm hiệu ứng cursor nhấp nháy giống terminal */
    @keyframes blink {
        0%, 100% { opacity: 1; }
        50% { opacity: 0; }
    }
    
    .cursor {
        animation: blink 1s step-end infinite;
        display: inline-block;
        width: 12px;
        margin-left: 5px;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# HIỂN THỊ CHỮ PALMISTRY GIỐNG TERMINAL
# ============================================
st.markdown("""
<div style="text-align: center;">
    <div class="palmistry-title">
        > PALMISTRY<span class="cursor">_</span>
    </div>
</div>
""", unsafe_allow_html=True)
