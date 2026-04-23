import streamlit as st

st.set_page_config(
    page_title="My Portfolio",
    page_icon="✨",
    layout="wide"
)

# Custom CSS for modern UI
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background: #F5F2FF;
        }

        [data-testid="stSidebar"] {
            background: #EBE6FF;

        }
        
        body {
            background-color: #0e1117;
            color: white;
        }

        h1, h2, h3 {
            color: #00c6ff;
        }

        .stButton>button {
            background-color: #00c6ff;
            color: black;
            border-radius: 10px;
            padding: 10px 20px;
        }

        .stTextInput>div>div>input {
            border-radius: 10px;
        }

        .card {
            padding: 20px;
            border-radius: 15px;
            background-color: #1c1f26;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.4);
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="My Portfolio", page_icon="🎓")

st.title("Welcome to My Professional Portfolio")
st.write("Navigate through the sidebar to learn more about my work and skills.")

st.success("Select a page above to get started about me!")