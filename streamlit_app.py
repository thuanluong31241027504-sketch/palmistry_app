import streamlit as st
import random
from PIL import Image, ImageDraw
import numpy as np
import time

# ============================================
# CẤU HÌNH TRANG
# ============================================
st.set_page_config(
    page_title="PALMISTRY - PIXEL ORACLE",
    page_icon="",
    layout="centered"
)

# ============================================
# CSS - PHONG CÁCH PIXEL
# ============================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Share+Tech+Mono&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #0a0a1a 0%, #1a0a2e 50%, #0a0a1a 100%);
        min-height: 100vh;
    }
    
    * {
        font-family: 'Press Start 2P', 'Share Tech Mono', monospace !important;
    }
    
    /* Hiệu ứng nhẹ nhàng cho chữ PALMISTRY */
    @keyframes softPixelGlow {
        0% {
            text-shadow: 0 0 1px #a78bfa, 0 0 2px #8b5cf6;
        }
        50% {
            text-shadow: 0 0 3px #c4b5fd, 0 0 5px #a855f7;
        }
        100% {
            text-shadow: 0 0 1px #a78bfa, 0 0 2px #8b5cf6;
        }
    }
    
    .palmistry-title {
        font-family: 'Press Start 2P', monospace;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        color: #c4b5fd;
        animation: softPixelGlow 3s ease-in-out infinite;
        letter-spacing: 3px;
        margin: 20px 0;
        padding: 15px;
        image-rendering: pixelated;
        image-rendering: crisp-edges;
    }
    
    .subtitle {
        font-family: 'Share Tech Mono', monospace;
        font-size: 0.5rem;
        text-align: center;
        color: #8b5cf6;
        letter-spacing: 1px;
        margin-bottom: 25px;
    }
    
    .stButton > button {
        background: linear-gradient(180deg, #2d1b4e 0%, #1a0f2e 100%);
        color: #c4b5fd !important;
        border: 2px solid #7e22ce;
        border-radius: 0px !important;
        font-family: 'Press Start 2P', monospace !important;
        font-size: 0.6rem !important;
        padding: 0.6rem 1.2rem !important;
        width: 100%;
        image-rendering: pixelated;
    }
    
    .stButton > button:hover {
        background: linear-gradient(180deg, #4c1d95 0%, #2d1b4e 100%);
        border-color: #a78bfa;
    }
    
    .stTextInput > div > div > input {
        background-color: #0f0719 !important;
        border: 2px solid #7e22ce !important;
        border-radius: 0px !important;
        color: #c4b5fd !important;
        font-family: 'Share Tech Mono', monospace !important;
        font-size: 0.7rem !important;
    }
    
    hr {
        border-color: #4c1d95 !important;
    }
    
    .result-box {
        background: #0f0719;
        border: 2px solid #7e22ce;
        padding: 1.2rem;
        margin-top: 1rem;
    }
    
    .result-text {
        font-family: 'Press Start 2P', monospace;
        color: #c4b5fd;
        font-size: 0.55rem;
        line-height: 1.4;
        margin: 0;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# HÀM TẠO QUẢ CẦU PIXEL
# ============================================
def tao_qua_cau_pixel(kich_thuoc=200):
    """Tạo quả cầu bói phong cách pixel"""
    pixel_size = 8
    img = Image.new('RGB', (kich_thuoc, kich_thuoc), (10, 10, 26))
    draw = ImageDraw.Draw(img)
    
    center = kich_thuoc // 2
    radius = kich_thuoc // 2 - pixel_size
    
    mau_tim_nhat = (180, 150, 255)
    mau_tim_duong = (120, 80, 200)
    mau_tim_dam = (70, 40, 120)
    mau_trang = (200, 180, 255)
    
    for x in range(0, kich_thuoc, pixel_size):
        for y in range(0, kich_thuoc, pixel_size):
            dx = (x + pixel_size//2) - center
            dy = (y + pixel_size//2) - center
            distance = (dx*dx + dy*dy) ** 0.5
            
            if distance <= radius:
                intensity = 1 - (distance / radius)
                
                if distance < radius * 0.3:
                    color = mau_tim_nhat
                elif distance < radius * 0.6:
                    color = mau_tim_duong
                else:
                    color = mau_tim_dam
                
                if abs(dx) < radius * 0.2 and dy < -radius * 0.2:
                    color = mau_trang
                
                draw.rectangle(
                    [x, y, x + pixel_size - 1, y + pixel_size - 1],
                    fill=color
                )
                
                draw.rectangle(
                    [x, y, x + pixel_size - 1, y + pixel_size - 1],
                    outline=(30, 20, 50),
                    width=1
                )
    
    return img

# ============================================
# HÀM TIÊN ĐOÁN
# ============================================
def tien_doan():
    cac_cau = [
        "DUONG TINH CAM CUA BAN SE SANG TOI",
        "CONG VIEC SAP CO TIEN TRIEN TOT",
        "HAY CHAM CHI HON TRONG THANG NAY",
        "MOI QUAN HE MOI DANG DEN GAN",
        "SU NGHIEP CUA BAN SE THANG TIEN",
        "HAY LANG NGHE TRUC GIAC CUA BAN",
        "CO NGUOI DANG NGHI VE BAN",
        "NGAY MAI SE LA MOT NGAY MAY MAN"
    ]
    return random.choice(cac_cau)

# ============================================
# HIỂN THỊ CHỮ PALMISTRY
# ============================================
st.markdown("""
<div style="text-align: center;">
    <div class="palmistry-title">
        PALMISTRY
    </div>
    <div class="subtitle">
        ========================<br>
        PIXEL PALM READING ORACLE<br>
        ========================
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ============================================
# GIAO DIỆN 2 CỘT
# ============================================
col_left, col_right = st.columns([1, 1])

with col_left:
    st.markdown("### QUA CAU PIXEL")
    
    qua_cau = tao_qua_cau_pixel(250)
    st.image(qua_cau, use_container_width=True)
    
    nut_bam = st.button("NHAN DE TIEN DOAN", use_container_width=True)
    
    if nut_bam:
        with st.spinner("DANG TIEN DOAN..."):
            time.sleep(0.8)
            st.session_state['du_doan'] = tien_doan()

with col_right:
    st.markdown("### NHAP CAU HOI")
    
    cau_hoi = st.text_input(
        "",
        placeholder="Nhap cau hoi cua ban...",
        key="cau_hoi_input",
        label_visibility="collapsed"
    )
    
    st.markdown("### KET QUA")
    
    if 'du_doan' in st.session_state:
        st.markdown(f"""
        <div class="result-box">
            <p class="result-text">
            {st.session_state['du_doan']}
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="result-box">
            <p class="result-text">
            [?] CHUA CO TIEN DOAN NAO [?]
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    if cau_hoi:
        st.markdown(f"""
        <div style="margin-top: 1rem;">
            <p style="color: #8b5cf6; font-size: 0.45rem;">
            > CAU HOI:
            </p>
            <p style="
                background: #0f0719;
                border-left: 2px solid #8b5cf6;
                padding: 0.5rem;
                font-size: 0.55rem;
                color: #c4b5fd;
            ">
            {cau_hoi}
            </p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div style="text-align: center;">
    <p style="font-size: 0.35rem; color: #4c1d95;">
    ========================================<br>
    PALMISTRY PIXEL SYSTEM - ACTIVE<br>
    ========================================
    </p>
</div>
""", unsafe_allow_html=True)
