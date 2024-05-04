import streamlit as st
import time as t

# to create image
st.image("lena_copy.png")

#title-used to add title of the app
st.title('Welcome to the new world of Ashish')

#Header
st.header("Machine Learning")


# sub header
st.subheader("Linear Regression")

# To give information
st.info("Information details of a user")

# Warning message
st.warning("Come on time or else you will be marked absent")

# write function
st.write("Employee names")
st.write(range(50))

# Error
st.error("wrong password")

# Success message
st.success("You got A grades")

# Markdown
st.markdown("# Intelligent")
st.markdown("## small")

st.markdown(":moon:")


# text-Write fixed-width and preformatted text.

st.text("Intellipat learners")


# To write a caption
st.caption("caption is here")

# to display a mathematical equation

st.latex(r''' a+b x^2+c''')


# widgets
# checkbox
st.checkbox('Login')

# button
st.button('click')

# radio widget
st.radio("Pick your gender",["Male","Female","Others"])

# select box
st.selectbox("Pick your course",["ML","cloud","Cyber secrity"])

# multiselect
st.multiselect("Choose the dept",["Content","Sales","Marketing"])

# selectslider

st.select_slider("Rating",["Bad","Good","Excellent","Outstanding"])

# slider
st.slider("Enter your number",0,100)

# number_input
st.number_input("Pick a number",0,100)
# text input
st.text_input("Enter your email address")

# date input
st.date_input("Date of Birth")

# time input
st.time_input("Hey,What's the timing")

# text area -Display a multi-line text input widget.

st.text_area("Welcome to the New world of Ashish. Hello friends")

# file uploader

st.file_uploader("upload your file/folder")

st.color_picker("color")

st.progress(90)

# spinner-Temporarily displays a message while executing a block of code.
with st.spinner("In Progress..."):
  t.sleep(2)

# ballon
st.balloons()

# sidebar-display items in sidebar
st.sidebar.title("Welcome to The MY WORLD")
st.sidebar.text_input("Mail Address")
st.sidebar.text_input("Password")
st.sidebar.button("Submit")

# Data visualization
import pandas as pd
import numpy as np
st.title("Bar Chart")
data=pd.DataFrame(np.random.randn(50,2),columns=["x","y"])
st.bar_chart(data)
st.title("Line Chart")
st.line_chart(data)
st.title("Area Chart")
st.area_chart(data)