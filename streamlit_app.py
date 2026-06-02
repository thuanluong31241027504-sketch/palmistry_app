import streamlit as st
import random
import time

# ============================================
# CẤU HÌNH TRANG (PHẢI ĐẦU TIÊN)
# ============================================
st.set_page_config(
    page_title="✨ PALMISTRY - TIÊN ĐOÁN PIXEL ✨",
    page_icon="🔮",
    layout="centered"
)

# ============================================
# CSS TÙY CHỈNH - PHONG CÁCH PIXEL + TÍM ĐEN
# ============================================
st.markdown("""
<style>
    /* Font chữ kiểu code/pixel */
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Share+Tech+Mono&display=swap');
    
    /* Nền tím đen gradient */
    .stApp {
        background: linear-gradient(135deg, #0a0a1a 0%, #1a0a2e 50%, #0a0a1a 100%);
    }
    
    /* Tất cả text */
    * {
        font-family: 'Press Start 2P', 'Share Tech Mono', monospace !important;
    }
    
    /* Container cho chữ PALMISTRY động */
    @keyframes textGlow {
        0% {
            text-shadow: 0 0 5px #8b5cf6, 0 0 10px #8b5cf6, 0 0 20px #7e22ce;
        }
        50% {
            text-shadow: 0 0 15px #a78bfa, 0 0 30px #a855f7, 0 0 45px #7e22ce;
        }
        100% {
            text-shadow: 0 0 5px #8b5cf6, 0 0 10px #8b5cf6, 0 0 20px #7e22ce;
        }
    }
    
    @keyframes textPulse {
        0% { opacity: 0.7; letter-spacing: 8px; }
        50% { opacity: 1; letter-spacing: 12px; }
        100% { opacity: 0.7; letter-spacing: 8px; }
    }
    
    @keyframes borderPulse {
        0% { border-color: #6d28d9; box-shadow: 0 0 10px rgba(139, 92, 246, 0.3); }
        50% { border-color: #a855f7; box-shadow: 0 0 30px rgba(168, 85, 247, 0.6); }
        100% { border-color: #6d28d9; box-shadow: 0 0 10px rgba(139, 92, 246, 0.3); }
    }
    
    @keyframes flicker {
        0% { opacity: 0.8; }
        5% { opacity: 1; }
        10% { opacity: 0.9; }
        15% { opacity: 1; }
        20% { opacity: 0.95; }
        100% { opacity: 1; }
    }
    
    /* Hiệu ứng ma trận rớt chữ */
    @keyframes matrixRain {
        0% { background-position: 0% 0%; }
        100% { background-position: 0% 100%; }
    }
    
    /* Text chính PALMISTRY */
    .palmistry-text {
        font-family: 'Press Start 2P', monospace;
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(135deg, #c4b5fd, #a78bfa, #7e22ce, #a855f7);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        animation: textGlow 2s ease-in-out infinite, textPulse 3s ease-in-out infinite;
        letter-spacing: 8px;
        margin: 0;
        padding: 20px;
    }
    
    /* Hiệu chữ nhỏ phụ */
    .subtitle {
        font-family: 'Share Tech Mono', monospace;
        font-size: 0.6rem;
        text-align: center;
        color: #a78bfa;
        animation: flicker 3s infinite;
        letter-spacing: 2px;
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
        animation: borderPulse 2s infinite;
    }
    
    .stButton > button:hover {
        background: linear-gradient(180deg, #4c1d95 0%, #2d1b4e 100%);
        border-color: #a855f7;
        box-shadow: 0 0 25px #8b5cf6;
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
    
    .stTextInput > div > div > input:focus {
        border-color: #a855f7 !important;
        box-shadow: 0 0 10px #8b5cf6 !important;
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
    
    /* Container kết quả */
    .result-box {
        background: linear-gradient(135deg, #1a0f2e 0%, #0f0719 100%);
        border: 2px solid #8b5cf6;
        padding: 1.5rem;
        margin-top: 1rem;
        animation: borderPulse 2s infinite;
    }
    
    .result-text {
        font-family: 'Press Start 2P', monospace;
        color: #d8b4fe;
        font-size: 0.65rem;
        line-height: 1.5;
        margin: 0;
        text-shadow: 0 0 5px #8b5cf6;
    }
    
    /* Loading animation */
    @keyframes dotPulse {
        0%, 100% { opacity: 0.2; }
        50% { opacity: 1; }
    }
    
    .loading-dots {
        font-family: 'Press Start 2P', monospace;
        font-size: 1rem;
        color: #a78bfa;
    }
    
    /* Star decoration */
    .star {
        color: #a855f7;
        animation: textGlow 1.5s infinite;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# HIỂN THỊ CHỮ PALMISTRY ĐỘNG
# ============================================

# Tạo hiệu ứng chữ PALMISTRY sáng rực
st.markdown("""
<div style="text-align: center; padding: 2rem 0;">
    <div class="palmistry-text">
        ██████╗░██████╗░██╗░░░░░███╗░░░███╗██╗░██████╗████████╗██████╗░██╗░░░██╗<br>
        ██╔══██╗██╔══██╗██║░░░░░████╗░████║██║██╔════╝╚══██╔══╝██╔══██╗╚██╗░██╔╝<br>
        ██████╔╝██████╔╝██║░░░░░██╔████╔██║██║╚█████╗░░░░██║░░░██████╔╝░╚████╔╝░<br>
        ██╔═══╝░██╔══██╗██║░░░░░██║╚██╔╝██║██║░╚═══██╗░░░██║░░░██╔══██╗░░╚██╔╝░░<br>
        ██║░░░░░██║░░██║███████╗██║░╚═╝░██║██║██████╔╝░░░██║░░░██║░░██║░░░██║░░░<br>
        ╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░<br>
    </div>
    <div class="subtitle">
        ═══════════════════════════════════════<br>
        ✦ PIXEL RETRO ORACLE - TIEN DOAN BANG CHU ✦<br>
        ═══════════════════════════════════════
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================
# HÀM TIÊN ĐOÁN NGẪU NHIÊN
# ============================================
def tien_doan():
    cac_cau_tien_doan = [
        "✨ TUONG LAI CUA BAN SE NHU NHUNG DONG CHU SANG✨",
        "🎮 MOT CO HOI MOI DANG DEN RAT GAN. HAY NAM BAT! 🎮",
        "💜 DIEU BAN DANG TIM KIEM O NGAY TRUOC MAT 💜",
        "🔮 VU TRU DANG MIM CUOI VOI BAN HOM NAY 🔮",
        "⭐ HAY TIN VAO TRUC GIAC CUA CHINH MINH ⭐",
        "⚡ MOT CUOC PHIEU LUU VI DAI SAP BAT DAU ⚡",
        "🌸 NHUNG DIEU KY DIEU DANG DEN VOI BAN 🌸",
        "🎯 THEO DUOI DAM ME, THANH CONG SE TIM DEN 🎯",
        "💫 TRAI TIM BAN DANG DAN DEN CONG DUONG DUNG 💫",
        "🌟 HOM NAY LA NGAY TOT DE BAT DAU DIEU MOI 🌟"
    ]
    return random.choice(cac_cau_tien_doan)

# ============================================
# HIỂU ỨNG LOADING (TĂNG TRẢI NGHIỆM)
# ============================================
def loading_animation():
    placeholder = st.empty()
    for i in range(3):
        dots = "." * (i + 1)
        placeholder.markdown(f"""
        <div style="text-align: center; margin: 2rem 0;">
            <p class="loading-dots">DANG TIEN DOAN{dots}</p>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(0.3)
    placeholder.empty()

# ============================================
# GIAO DIỆN CHÍNH
# ============================================

# Tạo 2 cột cho bố cục
col_left, col_right = st.columns([1, 1.5])

with col_left:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <p style="font-size: 2rem;">🔮</p>
        <p style="font-family: 'Press Start 2P', monospace; font-size: 0.7rem; color: #a78bfa;">
        &gt;_ QUA CAU TIEN TRI &lt;
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Nút để tiên đoán với hiệu ứng
    nut_bam = st.button("✨ NHAN DE TIEN DOAN ✨", use_container_width=True)
    
    if nut_bam:
        loading_animation()
        ket_qua = tien_doan()
        st.session_state['du_doan'] = ket_qua

with col_right:
    st.markdown("""
    <div style="margin-bottom: 1rem;">
        <p style="font-family: 'Press Start 2P', monospace; font-size: 0.7rem; color: #c4b5fd;">
        >_ NHAP CAU HOI:
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Text input
    cau_hoi = st.text_input(
        "",
        placeholder="[ NHAP CAU HOI CUA BAN VAO DAY ]",
        key="cau_hoi_input",
        label_visibility="collapsed"
    )
    
    st.markdown("""
    <div style="margin: 1.5rem 0 0.5rem 0;">
        <p style="font-family: 'Press Start 2P', monospace; font-size: 0.7rem; color: #c4b5fd;">
        >_ KET QUA TIEN DOAN:
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Hiển thị kết quả dự đoán
    if 'du_doan' in st.session_state:
        st.markdown(f"""
        <div class="result-box">
            <p class="result-text">
            {st.session_state['du_doan']}
            </p>
            <p style="
                font-family: 'Share Tech Mono', monospace;
                color: #a78bfa;
                font-size: 0.55rem;
                margin-top: 1rem;
                text-align: right;
                border-top: 1px solid #4c1d95;
                padding-top: 0.5rem;
            ">
            &gt;_ PALMISTRY PIXEL ORACLE v2.0 _&lt;
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="
            background: #0f0719;
            border: 2px solid #4c1d95;
            padding: 1.5rem;
            text-align: center;
        ">
            <p style="color: #6b21a5; font-family: 'Press Start 2P', monospace; font-size: 0.55rem;">
            [???] CHUA CO TIEN DOAN NAO [???]<br>
            &gt;_ HAY NHAN NUT BEN TRAI _&lt;
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Hiển thị câu hỏi đã nhập
    if cau_hoi:
        st.markdown(f"""
        <div style="margin-top: 1.5rem;">
            <p style="color: #8b5cf6; font-size: 0.55rem; font-family: 'Share Tech Mono', monospace;">
            &gt; CAU HOI CUA BAN:
            </p>
            <p style="
                background: #0f0719;
                border-left: 3px solid #8b5cf6;
                padding: 0.5rem;
                font-family: 'Share Tech Mono', monospace;
                font-size: 0.65rem;
                color: #d8b4fe;
            ">
            "{cau_hoi}"
            </p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; margin-top: 2rem;">
    <p style="
        font-family: 'Press Start 2P', monospace; 
        font-size: 0.4rem; 
        color: #6b21a5;
        letter-spacing: 2px;
    ">
    ═══════════════════════════════════════════════<br>
    [ PALMISTRY PIXEL SYSTEM - ONLINE ]<br>
    &gt;_ HAY LUON TIN VAO NHUNG DIEU KY DIEU _&lt;<br>
    ═══════════════════════════════════════════════
    </p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style="text-align: center;">
        <p style="font-size: 2rem;">🎮</p>
        <p style="font-family: 'Press Start 2P', monospace; font-size: 0.6rem; color: #a78bfa;">
        PALMISTRY<br>INFO
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    **⚡ HUONG DAN SU DUNG:**
    
    1. Nhap cau hoi cua ban
    2. Nhan nut ben trai
    3. Nhan ngay tien tri
    
    ---
    
    **💜 THONG DIEP:**
    Tien doan mang tinh giai tri,
    nhung hay luon giu niem tin
    vao nhung dieu tot dep!
    
    ---
    
    **🔮 CHUC NANG:**
    - Tien doan ngau nhien
    - Hieu ung chuyen dong
    - Giao dien pixel retro
    
    ---
    """)
    
    # Thêm vài ngôi sao trang trí
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <span class="star">✦</span> <span class="star">✧</span> <span class="star">✦</span> <span class="star">✧</span> <span class="star">✦</span>
        <p style="font-size: 0.45rem; color: #4c1d95; margin-top: 0.5rem;">
        PIXEL MODE v2.0<br>
        STATUS: ACTIVE
        </p>
    </div>
    """, unsafe_allow_html=True)
