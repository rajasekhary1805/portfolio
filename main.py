import streamlit as sl

sl.set_page_config(layout="wide")

col1, col2 = sl.columns(2)

with col1:
    sl.image("images/photo.png")

with col2:
    sl.title("Rajasekhar Y")
    content = """
    Hi, I am Rajasekhar, a passionate Python Developer with a keen interest in creating efficient 
    and scalable software solutions. 
    With a background in computer science and extensive hands-on experience, 
    I thrive in dynamic and challenging environments 
    where I can apply my skills to solve complex problems.
    """
    sl.info(content)