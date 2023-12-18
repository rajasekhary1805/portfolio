import streamlit as sl
import pandas

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

content2 = """
Below you can find some of the apps i have built in Python. Feel free to contact me!
"""
sl.write(content2)

col3, col4 = sl.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        sl.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        sl.header(row["title"])