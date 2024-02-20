import streamlit as st
import pandas as pd
import numpy as np
import time

#types of data we can have
a=[1,2,3,4,5,6,7,8]
n = np.array(a)
nd = n.reshape((2,4))
dic={
    "name":"devansh",
    "age":21,
    "city":"mumbai"
}

data = pd.read_csv('Salary_Data.csv')


#displaying data
#METHOD 1
st.dataframe(a)         #(a,width,height)
st.dataframe(n)         
st.dataframe(nd)         
st.dataframe(dic)         
st.dataframe(data)         
st.dataframe(data,width=500,height=500)        

#METHOD 2
st.table(data)
st.table(dic)

#METHOD 3
st.json(dic)

#METHOD 4
st.write(data)
st.write(a)
st.write(dic)


#as soon as we save the above script, the whole code runs from top to bottom. imagine we have a very heavy computing requirement or heavy dataset, everytime we save, it will take a lot of time to run. 

#CACHING IN STREAMLIT
#whenever we use a caching decorator, it tells streamlit that whenever this function is being called, it needs to check some of these things- 1. input parameter, 2. value of any internal variable, 3. body of function and 4. body of any function used inside the cache decorator.

@st.cache_data
def ret_time(a):
    time.sleep(5)
    return time.time()

if st.checkbox("1"):
    st.write(ret_time(1))

if st.checkbox("2"):
    st.write(ret_time(2))