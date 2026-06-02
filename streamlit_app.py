import streamlit as st
import random
from PIL import Image, ImageDraw
import numpy as np

# ============================================
# CẤU HÌNH TRANG (PHẢI ĐẦU TIÊN)
# ============================================
st.set_page_config(
    page_title="✨ Quả Cầu Tiên Đoán Pixel ✨",
    page_icon="🔮",
    layout="centered"
)

# ============================================
# CSS TÙY CHỈNH - PHONG CÁCH PIXEL + TÍM ĐEN
# ============================================
st.markdown("""
<style>
    /* Font chữ kiểu code */
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Share+Tech+Mono&display=swap');
    
    /* Nền tím đen gradient */
    .stApp {
        background: linear-gradient(135deg, #0a0a1a 0%, #1a0a2e 50%, #0a0a1a 100%);
    }
    
    /* Tất cả text */
    * {
        font-family: 'Press Start 2P', 'Share Tech Mono', monospace !important;
        color: #c4b5fd !important;
    }
    
    /* Tiêu đề chính */
    h1 {
        text-align: center;
        text-shadow: 0 0 10px #8b5cf6, 0 0 20px #6d28d9;
        color: #a78bfa !important;
        font-size: 1.5rem !important;
        margin-bottom: 2rem !important;
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    /* Hiệu ứng glow cho text */
    @keyframes glow {
        from { text-shadow: 0 0 5px #8b5cf6; }
        to { text-shadow: 0 0 20px #a855f7, 0 0 30px #7e22ce; }
    }
    
    /* Button pixel */
    .stButton > button {
        background: linear-gradient(180deg, #2d1b4e 0%, #1a0f2e 100%);
        color: #d8b4fe !important;
        border: 2px solid #7e22ce;
        border-radius: 0px !important;
        font-family: 'Press Start 2P', monospace !important;
        font-size: 0.7rem !important;
        padding: 0.7rem 1.5rem !important;
        transition: all 0.2s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        background: linear-gradient(180deg, #4c1d95 0%, #2d1b4e 100%);
        border-color: #a855f7;
        box-shadow: 0 0 15px #8b5cf6;
        transform: scale(1.02);
    }
    
    /* Text input pixel */
    .stTextInput > div > div > input {
        background-color: #0f0719 !important;
        border: 2px solid #7e22ce !important;
        border-radius: 0px !important;
        color: #e9d5ff !important;
        font-family: 'Share Tech Mono', monospace !important;
        font-size: 0.9rem !important;
    }
    
    /* Text area */
    .stTextArea > div > div > textarea {
        background-color: #0f0719 !important;
        border: 2px solid #7e22ce !important;
        border-radius: 0px !important;
        color: #e9d5ff !important;
        font-family: 'Share Tech Mono', monospace !important;
    }
    
    /* Select box */
    .stSelectbox > div > div {
        background-color: #0f0719 !important;
        border: 2px solid #7e22ce !important;
        border-radius: 0px !important;
    }
    
    /* Info/Warning/Success boxes */
    .stAlert {
        background-color: #1a0f2e !important;
        border-left: 4px solid #8b5cf6 !important;
        border-radius: 0px !important;
    }
    
    /* Divider */
    hr {
        border-color: #4c1d95 !important;
        border-width: 2px !important;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0a1a 0%, #120a1f 100%);
        border-right: 2px solid #4c1d95;
    }
    
    /* Cursor nhấp nháy kiểu terminal */
    @keyframes blink {
        0%, 100% { opacity: 1; }
        50% { opacity: 0; }
    }
    
    .terminal-cursor::after {
        content: '_';
        animation: blink 1s step-end infinite;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# HÀM TẠO HÌNH QUẢ CẦU PIXEL
# ============================================
def tao_qua_cau_pixel(kich_thuoc=200, mau_chinh=(168, 85, 247), mau_vien=(216, 180, 254), do_phat_sang=0):
    """Tạo hình ảnh quả cầu phong cách pixel retro"""
    # Tạo ảnh với kích thước pixel
    img = Image.new('RGBA', (kich_thuoc, kich_thuoc), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Kích thước pixel (mỗi pixel là 8x8 hoặc 4x4 cho hiệu ứng blocky)
    pixel_size = max(4, kich_thuoc // 25)
    center = kich_thuoc // 2
    radius = kich_thuoc // 2 - pixel_size
    
    # Vẽ các pixel tạo thành hình cầu
    for x in range(0, kich_thuoc, pixel_size):
        for y in range(0, kich_thuoc, pixel_size):
            # Tính khoảng cách từ tâm
            dx = (x + pixel_size//2) - center
            dy = (y + pixel_size//2) - center
            distance = (dx**2 + dy**2) ** 0.5
            
            # Vẽ pixel nếu nằm trong bán kính
            if distance <= radius:
                # Tạo hiệu ứng gradient và ánh sáng
                intensity = 1 - (distance / radius)
                
                # Tính màu dựa trên vị trí (hiệu ứng 3D pixel)
                if abs(dx) < radius * 0.3 and dy < -radius * 0.2:
                    # Vùng sáng
                    r = min(255, mau_chinh[0] + int(80 * intensity))
                    g = min(255, mau_chinh[1] + int(60 * intensity))
                    b = min(255, mau_chinh[2] + int(100 * intensity))
                elif dx > radius * 0.3 and dy > radius * 0.2:
                    # Vùng tối
                    r = max(50, mau_chinh[0] - 40)
                    g = max(50, mau_chinh[1] - 30)
                    b = max(100, mau_chinh[2] - 50)
                else:
                    # Màu chính
                    r = mau_chinh[0]
                    g = mau_chinh[1]
                    b = mau_chinh[2]
                
                # Thêm hiệu ứng phát sáng
                if do_phat_sang > 0:
                    r = min(255, r + do_phat_sang)
                    g = min(255, g + do_phat_sang * 0.8)
                    b = min(255, b + do_phat_sang * 1.2)
                
                # Vẽ pixel vuông
                draw.rectangle(
                    [x, y, x + pixel_size - 1, y + pixel_size - 1],
                    fill=(r, g, b, 255)
                )
                
                # Vẽ viền pixel (tạo hiệu ứng block)
                if pixel_size > 4:
                    draw.rectangle(
                        [x, y, x + pixel_size - 1, y + pixel_size - 1],
                        outline=(mau_vien[0], mau_vien[1], mau_vien[2], 100),
                        width=1
                    )
    
    # Thêm hiệu ứng "ma thuật" xung quanh (các pixel lấp lánh)
    for _ in range(50):
        x = random.randint(0, kich_thuoc - pixel_size)
        y = random.randint(0, kich_thuoc - pixel_size)
        draw.rectangle(
            [x, y, x + pixel_size//2, y + pixel_size//2],
            fill=(255, 200, 255, random.randint(50, 150))
        )
    
    return img

# ============================================
# HÀM TIÊN ĐOÁN NGẪU NHIÊN
# ============================================
def tien_doan():
    cac_cau_tien_doan = [
        "✨ TUONG LAI CUA BAN SE RUC RO NHU PIXEL NAY ✨",
        "🎮 MOT CO HOI MOI DANG DEN GAN... HAY NAM BAT! 🎮",
        "💜 DIEU BAN DANG TIM KIEM O NGAY TRUOC MAT 💜",
        "🔮 VU TRU DANG MIM CUOI VOI BAN HOM NAY 🔮",
        "⭐ HAY TIN VAO TRUC GIAC CUA CHINH MINH ⭐",
        "⚡ MOT CUOC PHIEU LUU MOI SAP BAT DAU ⚡",
        "🌸 NHUNG DIEU TOT DEP DANG DEN RAT GAN 🌸",
        "🎯 HAY THEO DUOI DAM ME, THANH CONG SE THEO SAU 🎯"
    ]
    return random.choice(cac_cau_tien_doan)

# ============================================
# GIAO DIỆN CHÍNH - PHONG CÁCH PIXEL
# ============================================

# Hiệu ứng typing cho tiêu đề
st.markdown("""
<div style="text-align: center;">
    <h1>
        ███████╗██╗██╗░░░░░██╗██╗░░░██╗███████╗<br>
        ██╔════╝██║╚██╗░██╔╝██║╚██╗░██╔╝██╔════╝<br>
        █████╗░░██║░╚████╔╝░██║░╚████╔╝░█████╗░░<br>
        ██╔══╝░░██║░░╚██╔╝░░██║░░╚██╔╝░░██╔══╝░░<br>
        ██║░░░░░██║░░░██║░░░██║░░░██║░░░███████╗<br>
        ╚═╝░░░░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░░╚══════╝<br>
    </h1>
    <p style="color: #a78bfa; font-size: 0.7rem;">⚡ QUA CAU TIEN DOAN PIXEL RETRO ⚡</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Tạo 2 cột cho bố cục
col1, col2 = st.columns([1, 1.5])

with col1:
    st.markdown("### 🔮 QUA CAU MA THUAT")
    
    # Tạo và hiển thị quả cầu pixel
    qua_cau = tao_qua_cau_pixel(kich_thuoc=250, mau_chinh=(147, 51, 234), do_phat_sang=30)
    st.image(qua_cau, use_container_width=True)
    
    # Nút để tiên đoán
    if st.button("✨ NHAN DE TIEN DOAN ✨", use_container_width=True):
        ket_qua = tien_doan()
        st.session_state['du_doan'] = ket_qua

with col2:
    st.markdown("### 💜 NHAP CAU HOI CUA BAN")
    
    # Text input với style pixel
    cau_hoi = st.text_input(
        ">_ ",
        placeholder="Nhap cau hoi cua ban vao day...",
        key="cau_hoi_input"
    )
    
    st.markdown("### ⚡ KET QUA TIEN DOAN")
    
    # Hiển thị kết quả dự đoán
    if 'du_doan' in st.session_state:
        st.markdown(
            f"""
            <div style="
                background: linear-gradient(135deg, #1a0f2e 0%, #0f0719 100%);
                border: 2px solid #8b5cf6;
                padding: 1.5rem;
                margin-top: 1rem;
                box-shadow: 0 0 20px rgba(139, 92, 246, 0.3);
            ">
                <p style="
                    font-family: 'Press Start 2P', monospace;
                    color: #d8b4fe;
                    font-size: 0.65rem;
                    line-height: 1.5;
                    margin: 0;
                    text-shadow: 0 0 5px #8b5cf6;
                ">
                {st.session_state['du_doan']}
                </p>
                <p style="
                    font-family: 'Share Tech Mono', monospace;
                    color: #a78bfa;
                    font-size: 0.55rem;
                    margin-top: 1rem;
                    text-align: right;
                ">
                &gt;_ QUA CAU TIEN DOAN &lt;
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <div style="
                background: #0f0719;
                border: 2px solid #4c1d95;
                padding: 1.5rem;
                text-align: center;
            ">
                <p style="color: #6b21a5; font-family: 'Press Start 2P', monospace; font-size: 0.6rem;">
                [?] HAY NHAN NUT BEN TRAI<br>
                DE NHAN TIEN DOAN [?]
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Hiển thị câu hỏi đã nhập (nếu có)
    if cau_hoi:
        st.markdown(
            f"""
            <div style="margin-top: 1.5rem;">
                <p style="color: #8b5cf6; font-size: 0.6rem;">&gt; Cau hoi cua ban:</p>
                <p style="
                    background: #0f0719;
                    border-left: 4px solid #8b5cf6;
                    padding: 0.5rem;
                    font-family: 'Share Tech Mono', monospace;
                    font-size: 0.7rem;
                ">
                "{cau_hoi}"
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

# Footer với hiệu ứng terminal
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; margin-top: 2rem;">
        <p style="
            font-family: 'Press Start 2P', monospace; 
            font-size: 0.45rem; 
            color: #6b21a5;
        ">
        ═══════════════════════════════════════<br>
        [ PIXEL RETRO ORACLE v1.0 ]<br>
        &gt;_ HAY TIN VAO NHUNG DIEU KY DIEU _&lt;<br>
        ═══════════════════════════════════════
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar với thông tin thêm
with st.sidebar:
    st.markdown("### 🎮 PIXEL INFO")
    st.markdown("---")
    st.markdown("""
    **⚡ HUONG DAN:**
    1. Nhap cau hoi cua ban
    2. Nhan nut "NHAN DE TIEN DOAN"
    3. Qua cau se mach bao cho ban!
    
    ---
    
    **💜 THONG DIEP:**
    Moi loi tien doan deu mang
    tinh giai tri, nhung hay
    luon giu niem tin vao
    nhung dieu tot dep!
    
    ---
    
    **🔧 CAI DAT PIXEL:**
    """)
    
    # Thanh điều chỉnh độ sáng của quả cầu
    do_sang = st.slider("DO SANG", 0, 100, 50)
    if st.button("TAI TAO QUA CAU"):
        st.rerun()
    
    st.markdown(
        """
        <div style="text-align: center; margin-top: 2rem;">
            <p style="font-size: 0.5rem; color: #4c1d95;">
            [ SYSTEM: ONLINE ]<br>
            &gt;_ PIXEL MODE ACTIVE _&lt;
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
