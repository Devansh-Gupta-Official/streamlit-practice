import streamlit as st
import time

#session states and callbacks IMPORTANT
if "photo" not in st.session_state:
    st.session_state["photo"] = "not done"

def change_photo_state():           #callback function
    st.session_state["photo"] = "done"

#columns
col1, col2, col3 = st.columns([1,2,1])
col1.markdown("# Welcome to my app!")
col1.markdown("## Let's try out some basic streamlit elements!")

#file uploader
file = col2.file_uploader("Upload a photo.", on_change=change_photo_state)

#camera input
photo = col2.camera_input("Say Cheese!!!", on_change=change_photo_state)

if st.session_state["photo"] == "done":

    #Progress Bar
    bar = col2.progress(0)    #initially 0
    for p in range(100):
        time.sleep(0.05)     #to ensure that the bar does not prgress too fast
        bar=bar.progress(p+1)

    #feedback
    col2.success("Photo Uploaded Successfully")

    #metrics
    col3.metric(label="Temperature", value="60 C", delta="3 C")

    #expanders
    with st.expander("Click here to Expand"):
        st.write("This is a Expander")
        if file is None:
            st.image(photo)
        else:
            st.image(file)


    
