import streamlit as st

st.title("widgets")

#adding a button
if st.button("learn"):                 
    st.write("streamlit")   

#adding text input
name = st.text_input("Name")
st.write(name)

#number input
st.number_input("number", min_value=18.0, max_value=60.0, value=30.0, step=2.0)    #input all floats*******

#text area
address=st.text_area("Enter address")
st.write(address)

#datetime input
date = st.date_input("enter date")
st.write(date)
time = st.time_input("enter time")
st.write(date)

#checkbox
if st.checkbox("YOU accept learning",value=False):
    st.write("Hi")

#radio button
v1 = st.radio("colors",["r","g","b"],index=0)     #name,list of options, default selected option

#selecr box
v2 = st.selectbox("colors",["r","g","b"],index=0)     
st.write(v1,v2)

#select multiple options
v3 = st.multiselect("colors",["r","g","b"])
st.write(v3)

#adding a slider
st.slider("age", min_value=18, max_value=60, value=30, step=2)

#add files
img23 = st.file_uploader("upload a file")
if img23 is not None:
    file_contents = img23.read()
    st.image(file_contents)