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
# CSS - NỀN TÍM + CHỮ PALMISTRY HIỆU ỨNG ĐỘNG
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
    
    /* Hiệu ứng động nhẹ cho chữ */
    @keyframes pixelGlow {
        0% {
            text-shadow: 0 0 2px #a78bfa, 0 0 4px #8b5cf6;
            opacity: 0.9;
        }
        50% {
            text-shadow: 0 0 6px #c084fc, 0 0 10px #a855f7;
            opacity: 1;
        }
        100% {
            text-shadow: 0 0 2px #a78bfa, 0 0 4px #8b5cf6;
            opacity: 0.9;
        }
    }
    
    @keyframes pixelLetter {
        0% {
            letter-spacing: 2px;
        }
        50% {
            letter-spacing: 5px;
        }
        100% {
            letter-spacing: 2px;
        }
    }
    
    .palmistry-title {
        font-family: 'Press Start 2P', monospace;
        font-size: 3rem;
        text-align: center;
        color: #c084fc;
        animation: pixelGlow 2.5s ease-in-out infinite, pixelLetter 3s ease-in-out infinite;
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
