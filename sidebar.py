import streamlit as st
import pandas as pd 
from matplotlib import pyplot as plt 
import time

plt.style.use("ggplot")

data = {
    "num":[x for x in range(1,11)],
    "square":[x**2 for x in range(1,11)],
    "twice":[x*2 for x in range(1,11)],
    "thrice":[x*3 for x in range(1,11)]
}

df = pd.DataFrame(data = data)


#sidebar
# st.sidebar.selectbox("Select a number",[1,2,3,4,5])    #selectbox widget in sidebar
# col = st.sidebar.selectbox("Select a column",df.columns)    

# plt.plot(df['num'],df[col])
# st.set_option('deprecation.showPyplotGlobalUse', False)    #to remove error in web page
# st.pyplot()


# col1 = st.sidebar.multiselect("Select a column",df.columns)
# plt.plot(df['num'],df[col1])
# st.set_option('deprecation.showPyplotGlobalUse', False)    #to remove error in web page
# st.pyplot()


#navigation bar
rad = st.sidebar.radio("Navigation",["Home","About Us"])
if rad=="Home":
    col1 = st.sidebar.multiselect("Select a column",df.columns)
    plt.plot(df['num'],df[col1])
    st.set_option('deprecation.showPyplotGlobalUse', False)    #to remove error in web page
    st.pyplot()

if rad=="About Us":
    st.write("yOU ARE AT ABOUT US PAGE")


#Progress and status
#ANIMATIONS

#STATUS
st.error("Error")
st.success("Success")
st.info("Information")
st.exception(RuntimeError("this is an error"))
st.warning("warning")

#PROGRESS BAR
progress = st.progress(0)      #initialize with 0
for i in range(100):
    time.sleep(0.2)
    progress.progress(i+1)

st.balloons()       #balloon animation