# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit.logger import get_logger

# Initialize session state for login status if not already set
if 'login_status' not in st.session_state:
    st.session_state['login_status'] = False

def login(username, password):
    if username == "admin" and password == "testuser20":
        st.session_state['login_status'] = True
    else:
        st.session_state['login_status'] = False
        st.error("Incorrect Username or Password")

def logout():
    st.session_state['login_status'] = False

def main():
    st.title("Streamlit Application")

    if st.session_state['login_status']:
        st.success("Logged in as admin")

        # Here you could place the sidebar content that should only be visible when logged in
        with st.sidebar:
            st.write("Sidebar content for logged-in users")
            if st.button("Logout", key="logout_button"):
                logout()

        # Main page content for logged-in users
        st.write("Welcome to the secure part of the app!")

    else:
        # Only show login form if not logged in
        with st.form("login_form", clear_on_submit=True):
            username = st.text_input("Username", key="username")
            password = st.text_input("Password", type="password", key="password")
            login_button = st.form_submit_button("Login")
            if login_button:
                login(username, password)
                if st.session_state['login_status']:
                    st.success("Login Successful!")
                else:
                    st.error("Login Failed. Try Again!")

if __name__ == "__main__":
    main()
