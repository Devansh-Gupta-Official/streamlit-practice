import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

data = pd.DataFrame(
    np.random.randn(100,3),
    columns=['a','b','c']
)


#plotting graphs
st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)

#plotting using matplotlib
plt.scatter(data['a'],data['b'])
plt.title("scatter")
st.pyplot()     #instead of plt.show


#plotting using altair
chart=alt.Chart(data).mark_circle().encode(
    x='a',y='b', tooltip=['a','b']    #tooltip adds interactivity
)
st.altair_chart(chart, use_container_width=True)    #makes this plot as big as all other plots

#flow diagrams in streamlit app
st.graphviz_chart("""
digraph{
    streamlit->practice
    practice->mlapps
    mlapps->hackathons
    hackathons->streamlit
}
""")


#plotting maps in streamlit
st.map()
#we can use dataframes, but dataframes need to have lat or lon named columns
city = pd.DataFrame({
    'awesome cities' : ['Chicago', 'Minneapolis', 'Louisville', 'Topeka'],
    'lat' : [41.868171, 44.979840,  38.257972, 39.030575],
    'lon' : [-87.667458, -93.272474, -85.765187,  -95.702548]
})
st.map(city)



#adding media to streamlit app
st.image("im1.jpg")   #height and width can also be passed

#adding audio to streamlit
st.audio("au1.wav")

#adding video to streamlit
st.video("vi1.mp4")
st.video("https://youtu.be/zARJgccbIEk?si=kVaON3J83aAfeP0M")