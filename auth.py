import streamlit as st

def check_login():
    return st.session_state.get('login_status', False)

def login(username, password):
    if username == "admin" and password == "testuser20":
        st.session_state['login_status'] = True
        return True
    return False

def logout():
    st.session_state['login_status'] = False
