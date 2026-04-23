import streamlit as st
import os

# ---------- PAGE STYLE ----------
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background: #F5F2FF;
        }

        [data-testid="stSidebar"] {
            background: #EBE6FF;
        }
        
        .card {
            padding: 20px;
            border-radius: 15px;
            background-color: #ffffff;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.4);
            margin-bottom: 20px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- SAFE BASE PATH (works in pages/ or root) ----------
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
except:
    BASE_DIR = os.getcwd()

# If inside /pages, go one level up
if os.path.basename(BASE_DIR) == "pages":
    BASE_DIR = os.path.dirname(BASE_DIR)

# ---------- IMAGE PATH ----------
image_path = os.path.join(BASE_DIR, "assets", "MYID2.png")

# ---------- HEADER ----------
st.title("✨ My Portfolio ✨")
st.subheader("Future Developer")

col1, col2 = st.columns([1, 2])

with col1:
    try:
        # Load image using binary (prevents MediaFileStorageError)
        with open(image_path, "rb") as img_file:
            st.image(img_file.read(), use_container_width=True)
    except FileNotFoundError:
        st.error("❌ Image not found. Check if MYID2.png is inside assets/ folder in GitHub.")
    except Exception as e:
        st.error("❌ Error loading image")
        st.text(str(e))

with col2:
    st.markdown("""
    ### Hi, I'm Rica Mae Sinogbujan 👋!
    I am a passionate student developer creating modern applications.

    I build efficient, offline-capable systems and modern user interfaces.

    🚀 Explore my portfolio using the sidebar!
    """)

st.divider()

# ---------- FEATURE CARDS ----------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="card">👤 <b>About Me</b><br>Explore to know more about me</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">🛠️ <b>Skills</b><br>My technical stack</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card">💻 <b>Projects</b><br>Explore my work</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="card">📩 <b>Contact</b><br>Reach me easily</div>', unsafe_allow_html=True)
