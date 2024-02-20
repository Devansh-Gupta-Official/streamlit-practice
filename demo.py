import streamlit as st

st.title("Practicing Streamlit")     #title

st.header("Header")      #header
st.subheader("Sub Header")      #subheader

st.text("This is my first time learning and using Streamlit")      #text

st.markdown("""# h1 tag
### h3 tag
:moon: <br>
:sunglasses:
**bold**
_italics_
""",True)      #True implies to the markdown that<br> is not a text but a html command

st.latex(r'''a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)''')                  #using latex


#write command  IMPORTANT*****
st.write("devansh","streamlit","practice")
st.write("# devansh")
st.write(st)
st.write(sum)


d ={
    "name":"Harsh",
    "language":"Python",
    "topic":"Streamlit"
} 
st.write(d)   #passing a dictionary