import streamlit as st
import random
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import time
import math

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
        font-size: 2rem;
        font-weight: bold;
        text-align: center;
        color: #c4b5fd;
        animation: softPixelGlow 3s ease-in-out infinite;
        letter-spacing: 3px;
        margin: 15px 0;
        padding: 10px;
    }
    
    .subtitle {
        font-family: 'Share Tech Mono', monospace;
        font-size: 0.45rem;
        text-align: center;
        color: #8b5cf6;
        letter-spacing: 1px;
        margin-bottom: 20px;
    }
    
    .stButton > button {
        background: linear-gradient(180deg, #2d1b4e 0%, #1a0f2e 100%);
        color: #c4b5fd !important;
        border: 2px solid #7e22ce;
        border-radius: 0px !important;
        font-family: 'Press Start 2P', monospace !important;
        font-size: 0.55rem !important;
        padding: 0.5rem 1rem !important;
        width: 100%;
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
        font-size: 0.65rem !important;
    }
    
    hr {
        border-color: #4c1d95 !important;
    }
    
    .result-box {
        background: #0f0719;
        border: 2px solid #7e22ce;
        padding: 1rem;
        margin-top: 1rem;
    }
    
    .result-text {
        font-family: 'Press Start 2P', monospace;
        color: #c4b5fd;
        font-size: 0.5rem;
        line-height: 1.4;
        margin: 0;
    }
    
    .sphere-container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# HÀM TẠO QUẢ CẦU MA THUẬT CÓ CHỮ
# ============================================
def tao_qua_cau_pixel(kich_thuoc=150, goc_xoay=0):
    """Tạo quả cầu ma thuật pixel có chữ PALMISTRY bên trong"""
    pixel_size = 6
    img = Image.new('RGB', (kich_thuoc, kich_thuoc), (10, 10, 26))
    draw = ImageDraw.Draw(img)
    
    center = kich_thuoc // 2
    radius = kich_thuoc // 2 - pixel_size
    
    # Màu sắc ma thuật
    mau_tim = [(60, 40, 120), (100, 60, 160), (140, 90, 200), (180, 130, 230)]
    mau_sang = [(220, 180, 255), (200, 150, 240)]
    
    # Vẽ các pixel tạo thành quả cầu
    for x in range(0, kich_thuoc, pixel_size):
        for y in range(0, kich_thuoc, pixel_size):
            dx = (x + pixel_size//2) - center
            dy = (y + pixel_size//2) - center
            
            # Hiệu ứng xoay nhẹ
            cos_a = math.cos(goc_xoay)
            sin_a = math.sin(goc_xoay)
            dx_rot = dx * cos_a - dy * sin_a
            dy_rot = dx * sin_a + dy * cos_a
            
            distance = (dx_rot*dx_rot + dy_rot*dy_rot) ** 0.5
            
            if distance <= radius:
                intensity = 1 - (distance / radius)
                
                if distance < radius * 0.3:
                    color_index = 3
                elif distance < radius * 0.6:
                    color_index = 2
                elif distance < radius * 0.8:
                    color_index = 1
                else:
                    color_index = 0
                
                # Thêm hiệu ứng lấp lánh
                sparkle = math.sin(goc_xoay * 3 + dx * 0.1) * 15
                
                r = min(255, mau_tim[color_index][0] + int(sparkle))
                g = min(255, mau_tim[color_index][1] + int(sparkle * 0.7))
                b = min(255, mau_tim[color_index][2] + int(sparkle))
                
                # Vùng sáng di chuyển
                if abs(dx_rot) < radius * 0.2 and dy_rot < -radius * 0.3:
                    r, g, b = mau_sang[0]
                elif abs(dx_rot) < radius * 0.15 and dy_rot < -radius * 0.15:
                    r, g, b = mau_sang[1]
                
                draw.rectangle(
                    [x, y, x + pixel_size - 1, y + pixel_size - 1],
                    fill=(r, g, b)
                )
                
                draw.rectangle(
                    [x, y, x + pixel_size - 1, y + pixel_size - 1],
                    outline=(40, 30, 70),
                    width=1
                )
    
    # Vẽ chữ PALMISTRY lên trên quả cầu
    try:
        # Thử dùng font pixel, nếu không có thì dùng font mặc định
        font = ImageFont.truetype("PressStart2P-Regular.ttf", 12)
    except:
        font = ImageFont.load_default()
    
    # Chữ cần vẽ
    text_lines = ["PALM", "ISTRY"]
    text_y_start = center - 15
    
    for i, line in enumerate(text_lines):
        # Lấy kích thước chữ
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        text_x = center - text_width // 2
        text_y = text_y_start + i * 15
        
        # Vẽ chữ màu trắng sáng
        draw.text((text_x, text_y), line, font=font, fill=(255, 220, 255))
    
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
        ======================<br>
        MAGIC PALM READING SPHERE<br>
        ======================
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ============================================
# QUẢ CẦU MA THUẬT CÓ CHỮ Ở GIỮA
# ============================================

sphere_placeholder = st.empty()

# Hiệu ứng động - quả cầu xoay nhẹ
for angle in range(0, 180, 15):
    qua_cau = tao_qua_cau_pixel(kich_thuoc=160, goc_xoay=math.radians(angle))
    sphere_placeholder.image(qua_cau, use_container_width=False, width=160)
    time.sleep(0.03)

# Giữ quả cầu ở trạng thái cuối
qua_cau_final = tao_qua_cau_pixel(kich_thuoc=160, goc_xoay=0)
sphere_placeholder.image(qua_cau_final, use_container_width=False, width=160)

st.markdown("<br>", unsafe_allow_html=True)

# ============================================
# GIAO DIỆN CHÍNH
# ============================================
col_left, col_right = st.columns([1, 1])

with col_left:
    nut_bam = st.button("NHAN DE TIEN DOAN", use_container_width=True)
    
    if nut_bam:
        with st.spinner("DANG TIEN DOAN..."):
            time.sleep(0.8)
            st.session_state['du_doan'] = tien_doan()

with col_right:
    cau_hoi = st.text_input(
        "",
        placeholder="Nhap cau hoi cua ban...",
        key="cau_hoi_input",
        label_visibility="collapsed"
    )

# ============================================
# HIỂN THỊ KẾT QUẢ
# ============================================
if 'du_doan' in st.session_state:
    st.markdown(f"""
    <div class="result-box">
        <p class="result-text">
        {st.session_state['du_doan']}
        </p>
    </div>
    """, unsafe_allow_html=True)

if cau_hoi:
    st.markdown(f"""
    <div style="margin-top: 1rem;">
        <p style="color: #8b5cf6; font-size: 0.4rem;">
        > CAU HOI:
        </p>
        <p style="
            background: #0f0719;
            border-left: 2px solid #8b5cf6;
            padding: 0.5rem;
            font-size: 0.5rem;
            color: #c4b5fd;
        ">
        {cau_hoi}
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div style="text-align: center;">
    <p style="font-size: 0.3rem; color: #4c1d95;">
    ====================================<br>
    PALMISTRY PIXEL SYSTEM - ACTIVE<br>
    ====================================
    </p>
</div>
""", unsafe_allow_html=True)
