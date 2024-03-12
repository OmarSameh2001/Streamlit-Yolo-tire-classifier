import base64
import streamlit as st


def style():
    # Background and styling
    background = 'v:background.jpg'
    with open(background, "rb") as f:
        img_data = f.read()
    b64_encoded = base64.b64encode(img_data).decode()
    styling = f"""
    <style>
    .stApp {{
        background-image: url(data:image/png;base64,{b64_encoded});
        background-size: cover;
    }}
    footer {{visibility: hidden;}}
    .stAlert {{
        .st-bd {{
            background-color: rgb(26 31 59);
         }}
        .st-bc {{
            color: rgb(246 246 246);
         }}
    }}
    </style>
"""
    st.markdown(styling, unsafe_allow_html=True)
