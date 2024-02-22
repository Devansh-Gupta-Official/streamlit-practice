import streamlit as st

st.title("Registration Form")


#ROW 1
first,last = st.columns(2)      #provide the number of columns ; return containers first and last

first.text_input("First Name")
last.text_input("Last Name")


#ROW 2
email,mob = st.columns([3,1])       #[3,1] divides column in ratio 3:1
email.text_input("Enter email ID")
mob.text_input("Enter Mobile Number")

#ROW 3
user,pw,pw2 = st.columns(3)
user.text_input("Enter username")
pw.text_input("Enter password", type='password')
pw2.text_input("Re-Enter password", type='password')

#ROW 4
ch,bl,sub = st.columns(3)
ch.checkbox("I Agree")
sub.button("Submit")