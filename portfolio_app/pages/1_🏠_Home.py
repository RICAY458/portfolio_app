import streamlit as st
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="My Portfolio", page_icon="✨", layout="wide")

# --- DYNAMIC PATH RESOLUTION ---
# This finds the 'assets' folder relative to this script's location
current_dir = os.path.dirname(__file__)  # Location of 1_🏠_Home.py
root_dir = os.path.dirname(current_dir)   # Up one level to project root
image_path = os.path.join(root_dir, "assets", "MYID2.png")

# --- STYLING ---
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
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
            margin-bottom: 20px;
            height: 150px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.title("✨ My Portfolio ✨")
st.subheader("Future Developer")

col1, col2 = st.columns([1, 2])

with col1:
    # Try to load the image using the dynamic path
    if os.path.exists(image_path):
        st.image(image_path)
    else:
        # Fallback debug message if image is still missing
        st.error(f"Image not found at: {image_path}")
        st.info(f"Check if 'MYID2.png' is inside the 'assets' folder on GitHub.")

with col2:
    st.markdown(f"""
    ### Hi, I'm Rica Mae Sinogbujan👋!
    I am a passionate student developer creating modern applications.

    I build efficient, offline-capable systems and modern user interfaces.

    🚀 Explore my portfolio using the sidebar!
    """)

st.divider()

# --- FEATURE CARDS ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="card">👤 <b>About Me</b><br><br>Explore to know more about me</div>', unsafe_allow_html=True)
    if st.button("Go to About", use_container_width=True):
        st.switch_page("pages/2_👤_About.py")

with col2:
    st.markdown('<div class="card">🛠️ <b>Skills</b><br><br>My technical stack</div>', unsafe_allow_html=True)
    # Update the path below to match your actual Skills page filename
    if st.button("View Skills", use_container_width=True):
        st.switch_page("pages/3_🛠️_Skills.py") 

with col3:
    st.markdown('<div class="card">💻 <b>Projects</b><br><br>Explore my work</div>', unsafe_allow_html=True)
    # Update the path below to match your actual Projects page filename
    if st.button("See Projects", use_container_width=True):
        st.switch_page("pages/4_💻_Projects.py")

with col4:
    st.markdown('<div class="card">📩 <b>Contact</b><br><br>Reach me easily</div>', unsafe_allow_html=True)
    # Update the path below to match your actual Contact page filename
    if st.button("Contact Me", use_container_width=True):
        st.switch_page("pages/5_📩_Contact.py")

with col4:
    st.markdown('<div class="card">📩 <b>Contact</b><br>Reach me easily</div>', unsafe_allow_html=True)
