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
        
        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0; }
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
        
        .cursor {
            display: inline-block;
            width: 12px;
            margin-left: 5px;
            opacity: 1;
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
        
        .instruction {
            font-family: 'SF Mono', monospace;
            font-size: 0.7rem;
            color: #8b5cf6;
            margin-top: 2rem;
            line-height: 1.8;
            display: inline-block;
            text-align: left;
        }
        
        .instruction-container {
            display: flex;
            justify-content: center;
            margin-top: 2rem;
        }
        
        .blinking-underscore {
            animation: blink 1s step-end infinite;
            display: inline-block;
            width: 8px;
            margin-left: 2px;
        }
        
        .static-underscore {
            display: inline-block;
            width: 8px;
            margin-left: 2px;
            opacity: 1;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Chữ PALMISTRY không nháy
    st.markdown("""
    <div style="text-align: center;">
        <div class="palmistry-title">
            > palmistry_
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Nút START
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("START", use_container_width=True):
            loading_placeholder = st.empty()
            
            with loading_placeholder.container():
                st.markdown('<div class="loader"></div>', unsafe_allow_html=True)
                st.markdown('<p style="text-align: center; color: #c084fc; font-family: monospace;">loading...</p>', unsafe_allow_html=True)
                
                time.sleep(3)
            
            loading_placeholder.empty()
            st.session_state.page = 'camera'
            st.rerun()
    
    # 3 dòng text: dòng 1,2 tắt nháy - dòng 3 nháy
    st.markdown("""
    <div class="instruction-container">
        <div class="instruction">
            > chụp ảnh lòng bàn tay dưới ánh sáng đủ, tay để trong khung hình<span class="static-underscore">_</span><br>
            > nhấn nút app sẽ tự động nhận diện các đường chỉ tay<span class="static-underscore">_</span><br>
            > đọc kết quả giải mã đường sinh mệnh, trí tuệ, tình cảm và vận mệnh<span class="blinking-underscore">_</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# TRANG CAMERA - CHỤP ẢNH BÀN TAY
# ============================================
elif st.session_state.page == 'camera':
    
    st.set_page_config(
        page_title="palmistry",
        page_icon="",
        layout="centered"
    )
    
    st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #0a0a1a 0%, #1a0a2e 50%, #0a0a1a 100%);
            min-height: 100vh;
        }
        
        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0; }
        }
        
        .page-title {
            font-family: 'SF Mono', 'Menlo', monospace;
            font-size: 1.2rem;
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
        
        .instruction {
            font-family: 'SF Mono', monospace;
            font-size: 0.65rem;
            color: #8b5cf6;
            margin-top: 2rem;
            line-height: 1.8;
            display: inline-block;
            text-align: left;
        }
        
        .instruction-container {
            display: flex;
            justify-content: center;
            margin-top: 2rem;
        }
        
        .blinking-underscore {
            animation: blink 1s step-end infinite;
            display: inline-block;
            width: 8px;
            margin-left: 2px;
        }
        
        .static-underscore {
            display: inline-block;
            width: 8px;
            margin-left: 2px;
            opacity: 1;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="page-title">
        > chụp ảnh bàn tay của bạn
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        camera_image = st.camera_input("", label_visibility="collapsed")
        
        if camera_image is not None:
            st.image(camera_image, caption="bàn tay của bạn", use_container_width=True)
            
            if st.button("phân tích", use_container_width=True):
                with st.spinner("đang phân tích..."):
                    time.sleep(2)
                st.success("kết quả sẽ hiển thị ở đây!")
    
    # 3 dòng text: dòng 1,2 tắt nháy - dòng 3 nháy
    st.markdown("""
    <div class="instruction-container">
        <div class="instruction">
            > chụp ảnh lòng bàn tay dưới ánh sáng đủ, tay để trong khung hình<span class="static-underscore">_</span><br>
            > nhấn "phân tích" - app tự động nhận diện các đường chỉ tay chính<span class="static-underscore">_</span><br>
            > đọc kết quả giải mã đường sinh mệnh, trí tuệ, tình cảm và vận mệnh<span class="blinking-underscore">_</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
