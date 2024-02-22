import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt    #for non interactive plots
import altair as alt      #can be used for plotting interactive graphs
import plotly.graph_objs as go     #used for interactive graphs

data = pd.read_csv('../practice-scripts/Salary_Data.csv')

st.title("Salary Predictor")

nav = st.sidebar.radio("Navigation",["Home","Prediction","Contribute to Dataset"])

if nav=="Home":
    st.image("imgg.jpg",width=800,caption="Money Money")
    if st.checkbox("Show Table"):
        st.table(data)

    graph = st.selectbox("What type of graph do you want?",["Non-Interactive","Interactive"])
    val=st.slider("Select Years of Experience",0,20)
    data = data.loc[data["YearsExperience"]>= val]
    if graph=="Non-Interactive":
        plt.figure(figsize=(10,5))
        plt.scatter(data["YearsExperience"],data["Salary"])
        plt.title("Scatter")
        plt.ylim(0)
        plt.xlabel("Years of Experience")
        plt.ylabel("Salary")
        plt.tight_layout()
        st.set_option('deprecation.showPyplotGlobalUse', False)     #ignoring warnings
        st.pyplot()
    if graph=="Interactive":
        # #plotting using altair
        # chart=alt.Chart(data).mark_circle().encode(
        #     x='YearsExperience',y='Salary', tooltip=['YearsExperience','Salary']    #tooltip adds interactivity
        # )
        # st.altair_chart(chart, use_container_width=True)    #makes this plot as big as all other plots
        layout=go.Layout(
            xaxis=dict(range=[0,16]),
            yaxis=dict(range=[0,210000])
        )
        fig=go.Figure(data=go.Scatter(x=data['YearsExperience'],y=data['Salary'],mode="markers"), layout=layout)
        st.plotly_chart(fig)


if nav=="Prediction":
    st.write("pred")

if nav=="Contribute to Dataset":
    st.write("contri")

