import streamlit as st


st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background: #F5F2FF;
        }

        [data-testid="stSidebar"] {
            background: #EBE6FF;
        }
            
        .cert-badge {
            background-color: #ffffff;
            padding: 2px 10px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: bold;
            display: inline-block;
            margin-top: 5px;
        }
        .skill-card {
            text-align: center;
            margin-bottom: 30px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🛠️ My Skills")
st.subheader(" Programming Languages")
skills = {
    "Python": 50,
    "Java/xml/ Sqlite": 40,
    "Streamlit": 40,
    "HTML/CSS/JAVASCRIPT": 70
}

for skill, level in skills.items():
    st.markdown(f"**{skill}**")
    st.progress(level)

st.divider()

# --- Skills & Certificates Section ---
st.subheader(" Certificates")

# 1. Define your data (You can replace the URLs with your local image paths)
skills_data = [
    {"name": "Python Programming in Cisco Networking Academy", "img": "assets/Python.png"},
    {"name": "Python Programming in Simple Learn", "img": "assets/python1.png"},
    {"name": "java", "img": "assets/java.png"},
    {"name": "UI/UX Design", "img": "assets/ui_ux.jpeg"},
    {"name": "Cybersecurity", "img": "assets/cyber.jpg"},
    {"name": "Android", "img": "assets/android.png"},
]

# 3. Create the 3-column grid
# We process the list in chunks of 3
for i in range(0, len(skills_data), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(skills_data):
            skill = skills_data[i + j]
            with cols[j]:
                # Wrap inside your existing 'card' class for consistency
                st.markdown(f'<div class="card skill-card">', unsafe_allow_html=True)
                
                # Skill Image
                st.image(skill["img"], use_container_width=True)