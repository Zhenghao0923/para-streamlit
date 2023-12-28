import streamlit as st

st.set_page_config(
    page_title="mult"
)
st.title("用户中心")
st.sidebar.success("select your page")

#to get input from user
if "input" not in st.session_state:
    st.session_state["input"] =""

input = st.text_input("Input your info here",st.session_state["input"])
submit = st.button("Submit-提交")
if submit:
    st.session_state["input"] = input
    st.write("Your have entered: ",input)
    
