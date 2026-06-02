import streamlit as st
import time

# ============================================
# KIỂM TRA TRẠNG THÁI TRANG
# ============================================
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# ============================================
# TRANG CHỦ - CÓ CHỮ PALMISTRY VÀ NÚT START
# ============================================
if st.session_state.page == 'home':
    
    st.set_page_config(
        page_title="PALMISTRY",
        page_icon="",
        layout="centered"
    )
    
    st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #0a0a1a 0%, #1a0a2e 50%, #0a0a1a 100%);
            min-height: 100vh;
        }
        
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
        
        /* Loading spinner */
        .loader {
            border: 4px solid #2d1b4e;
            border-top: 4px solid #c084fc;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 20px auto;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .stButton > button {
            background: transparent;
            color: #c084fc !important;
            border: 2px solid #c084fc;
            border-radius: 0px !important;
            font-family: 'SF Mono', 'Menlo', monospace !important;
            font-size: 1.2rem !important;
            padding: 0.8rem 2rem !important;
            width: auto;
            margin: 0 auto;
            display: block;
        }
        
        .stButton > button:hover {
            background: #c084fc20;
            border-color: #a855f7;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center;">
        <div class="palmistry-title">
            > PALMISTRY<span class="cursor">_</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Nút START
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("> START_", use_container_width=True):
            # Tạo placeholder cho hiệu ứng loading
            loading_placeholder = st.empty()
            
            with loading_placeholder.container():
                st.markdown('<div class="loader"></div>', unsafe_allow_html=True)
                st.markdown('<p style="text-align: center; color: #c084fc; font-family: monospace;">LOADING...</p>', unsafe_allow_html=True)
                
                # Chờ 3 giây
                time.sleep(3)
            
            # Xóa loading và chuyển trang
            loading_placeholder.empty()
            st.session_state.page = 'camera'
            st.rerun()

# ============================================
# TRANG CAMERA - CHỤP ẢNH BÀN TAY
# ============================================
elif st.session_state.page == 'camera':
    
    st.set_page_config(
        page_title="CHUP ANH BAN TAY",
        page_icon="",
        layout="centered"
    )
    
    st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #0a0a1a 0%, #1a0a2e 50%, #0a0a1a 100%);
            min-height: 100vh;
        }
        
        .page-title {
            font-family: 'SF Mono', 'Menlo', monospace;
            font-size: 1.5rem;
            text-align: center;
            color: #c084fc;
            margin-top: 40px;
            margin-bottom: 40px;
        }
        
        .stButton > button {
            background: transparent;
            color: #c084fc !important;
            border: 2px solid #c084fc;
            border-radius: 0px !important;
            font-family: 'SF Mono', 'Menlo', monospace !important;
            font-size: 1rem !important;
            padding: 0.6rem 1.5rem !important;
        }
        
        .stButton > button:hover {
            background: #c084fc20;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="page-title">
        > CHUP ANH BAN TAY DE DU DOAN
    </div>
    """, unsafe_allow_html=True)
    
    # Nút chụp ảnh từ camera
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        camera_image = st.camera_input("", label_visibility="collapsed")
        
        if camera_image is not None:
            st.image(camera_image, caption="ANH BAN TAY CUA BAN", use_container_width=True)
            
            if st.button("> DU DOAN", use_container_width=True):
                with st.spinner("DANG PHAN TICH..."):
                    time.sleep(2)
                st.success("KET QUA SE HIEN THI O DAY!")
