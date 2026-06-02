import streamlit as st
import random
import time

# ============================================
# CẤU HÌNH TRANG
# ============================================
st.set_page_config(
    page_title="✨ PALMISTRY - BÓI TAY ✨",
    page_icon="🔮",
    layout="centered"
)

# ============================================
# CSS - PHONG CÁCH PIXEL + TÍM ĐEN
# ============================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Share+Tech+Mono&display=swap');
    
    /* Nền tím đen */
    .stApp {
        background: linear-gradient(135deg, #0a0a1a 0%, #1a0a2e 50%, #0a0a1a 100%);
        min-height: 100vh;
    }
    
    * {
        font-family: 'Press Start 2P', 'Share Tech Mono', monospace !important;
    }
    
    /* Hiệu ứng chữ PALMISTRY - GIẢM SÁNG, CHẬM LẠI */
    @keyframes gentleGlow {
        0% {
            text-shadow: 0 0 2px #8b5cf6, 0 0 4px #8b5cf6;
        }
        50% {
            text-shadow: 0 0 6px #a78bfa, 0 0 10px #a855f7;
        }
        100% {
            text-shadow: 0 0 2px #8b5cf6, 0 0 4px #8b5cf6;
        }
    }
    
    @keyframes gentlePulse {
        0% { opacity: 0.95; letter-spacing: 2px; }
        50% { opacity: 1; letter-spacing: 4px; }
        100% { opacity: 0.95; letter-spacing: 2px; }
    }
    
    /* Chữ PALMISTRY - RÕ NÉT, SÁNG NHẸ, CHẬM */
    .palmistry-title {
        font-family: 'Press Start 2P', monospace;
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #b794f4;
        animation: gentleGlow 3s ease-in-out infinite, gentlePulse 4s ease-in-out infinite;
        letter-spacing: 4px;
        margin: 30px 0;
        padding: 20px;
    }
    
    .subtitle {
        font-family: 'Press Start 2P', monospace;
        font-size: 0.55rem;
        text-align: center;
        color: #8b5cf6;
        letter-spacing: 2px;
        margin-bottom: 30px;
    }
    
    /* Button */
    .stButton > button {
        background: linear-gradient(180deg, #2d1b4e 0%, #1a0f2e 100%);
        color: #d8b4fe !important;
        border: 2px solid #7e22ce;
        border-radius: 0px !important;
        font-family: 'Press Start 2P', monospace !important;
        font-size: 0.7rem !important;
        padding: 0.7rem 1.5rem !important;
        width: 100%;
    }
    
    .stButton > button:hover {
        background: linear-gradient(180deg, #4c1d95 0%, #2d1b4e 100%);
        border-color: #a855f7;
    }
    
    hr {
        border-color: #4c1d95 !important;
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
    <div class="subtitle">
        ═══════════════════════<br>
        ✦ PIXEL PALM READING ✦<br>
        ═══════════════════════
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================
# TẠM THỜI ĐỂ TRỐNG - CHỜ BƯỚC SAU
# ============================================
st.info("✨ Đã xong bước 1. Chờ yêu cầu bước 2...")
