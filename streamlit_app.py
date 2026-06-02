import streamlit as st
import time

# ============================================
# KIỂM TRA TRẠNG THÁI TRANG
# ============================================
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# ============================================
# CSS CHUNG CHO CẢ 2 TRANG
# ============================================
st.markdown("""
<style>
    /* Nền tím gradient */
    .stApp {
        background: linear-gradient(135deg, #0a0a1a 0%, #1a0a2e 50%, #0a0a1a 100%);
        min-height: 100vh;
    }
    
    /* Font terminal */
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600;700&display=swap');
    
    * {
        font-family: 'Fira Code', 'SF Mono', 'Menlo', 'Courier New', monospace;
    }
    
    /* Hiệu ứng border đẹp */
    .glass-box {
        background: rgba(20, 10, 40, 0.6);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(192, 132, 252, 0.3);
        border-radius: 12px;
        padding: 2rem;
        margin: 1rem 0;
    }
    
    /* Nút bấm đẹp */
    .stButton > button {
        background: linear-gradient(135deg, #2d1b4e 0%, #1a0f2e 100%);
        color: #c084fc !important;
        border: 1px solid #c084fc;
        border-radius: 8px !important;
        font-family: 'Fira Code', monospace !important;
        font-size: 1rem !important;
        font-weight: 500 !important;
        padding: 0.75rem 2rem !important;
        transition: all 0.3s ease !important;
        width: 100%;
        cursor: pointer;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #4c1d95 0%, #2d1b4e 100%);
        border-color: #a855f7;
        box-shadow: 0 0 20px rgba(192, 132, 252, 0.3);
        transform: translateY(-2px);
    }
    
    /* Loading spinner đẹp */
    .loader {
        border: 3px solid #2d1b4e;
        border-top: 3px solid #c084fc;
        border-right: 3px solid #a855f7;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        animation: spin 1s linear infinite;
        margin: 20px auto;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* Cursor nhấp nháy */
    @keyframes blink {
        0%, 100% { opacity: 1; }
        50% { opacity: 0; }
    }
    
    .cursor {
        animation: blink 1s step-end infinite;
        display: inline-block;
        width: 8px;
        margin-left: 5px;
        background-color: #c084fc;
    }
    
    /* Hiệu ứng glow cho text */
    .glow-text {
        text-shadow: 0 0 10px rgba(192, 132, 252, 0.5);
    }
    
    /* Divider đẹp */
    .custom-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #c084fc, #a855f7, #c084fc, transparent);
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# TRANG CHỦ
# ============================================
if st.session_state.page == 'home':
    
    st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; min-height: 60vh;">
        <div style="text-align: center;">
            <div style="font-family: 'Fira Code', monospace; font-size: 3.5rem; color: #c084fc; font-weight: 700; letter-spacing: 4px; margin-bottom: 1rem;">
                > PALMISTRY<span class="cursor">_</span>
            </div>
            <div style="font-family: 'Fira Code', monospace; font-size: 0.8rem; color: #8b5cf6; letter-spacing: 2px; margin-bottom: 3rem;">
                ═══════════════════════════<br>
                PIXEL PALM READING TERMINAL<br>
                ═══════════════════════════
            </div>
    """, unsafe_allow_html=True)
    
    # Nút START
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("> START_", use_container_width=True):
            loading_placeholder = st.empty()
            
            with loading_placeholder.container():
                st.markdown('<div class="loader"></div>', unsafe_allow_html=True)
                st.markdown('<p style="text-align: center; color: #c084fc; font-family: monospace; margin-top: 1rem;">[ SYSTEM INITIALIZING... ]</p>', unsafe_allow_html=True)
                time.sleep(3)
            
            loading_placeholder.empty()
            st.session_state.page = 'camera'
            st.rerun()
    
    st.markdown("""
        </div>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# TRANG CAMERA
# ============================================
elif st.session_state.page == 'camera':
    
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <div style="font-family: 'Fira Code', monospace; font-size: 1.8rem; color: #c084fc; font-weight: 600; margin-bottom: 0.5rem;">
            > CAPTURE HAND
        </div>
        <div style="font-family: 'Fira Code', monospace; font-size: 0.7rem; color: #8b5cf6;">
            ─────────────────────────────────<br>
            CHUP ANH BAN TAY DE DU DOAN<br>
            ─────────────────────────────────
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Bố cục 2 cột
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.markdown("""
        <div class="glass-box">
            <div style="text-align: center; margin-bottom: 1rem;">
                <span style="font-size: 3rem;">📸</span>
                <p style="color: #c084fc; font-size: 0.8rem; margin-top: 0.5rem;">> CAMERA FEED</p>
            </div>
        """, unsafe_allow_html=True)
        
        camera_image = st.camera_input("", label_visibility="collapsed")
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col_right:
        st.markdown("""
        <div class="glass-box">
            <div style="text-align: center; margin-bottom: 1rem;">
                <span style="font-size: 3rem;">🔮</span>
                <p style="color: #c084fc; font-size: 0.8rem; margin-top: 0.5rem;">> PREDICTION</p>
            </div>
        """, unsafe_allow_html=True)
        
        if camera_image is not None:
            st.image(camera_image, caption="> HAND IMAGE", use_container_width=True)
            
            if st.button("> ANALYZE", use_container_width=True):
                with st.spinner("[ PROCESSING... ]"):
                    time.sleep(2)
                st.success("✅ DU DOAN HOAN TAT!")
                st.info("""
                > KET QUA SO BO:
                - DUONG TINH CAM: RO NET
                - DUONG CONG DANH: DANG PHAT TRIEN
                - DUONG SINH MENH: MANH ME
                """)
        else:
            st.markdown("""
            <div style="text-align: center; padding: 3rem 0;">
                <p style="color: #6b21a5; font-size: 0.8rem;">
                [?] CHUA CO ANH NAO<br>
                > HAY CHUP ANH BAN TAY BEN TRAI
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Nút quay lại
    st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("< BACK", use_container_width=True):
            st.session_state.page = 'home'
            st.rerun()
