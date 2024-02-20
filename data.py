import streamlit as st
import pandas as pd
import numpy as np

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

