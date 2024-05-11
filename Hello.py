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

import streamlit as st
from auth import check_login, login, logout

def main_page():
    st.title("Main Page")
    st.write("This is the main page of the application.")

def secure_page():
    st.title("Secure Page")
    st.write("This page contains sensitive data.")

def login_page():
    with st.form("login_form", clear_on_submit=True):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        if submitted and login(username, password):
            st.success("Login Successful!")
        elif submitted:
            st.error("Login Failed. Try Again!")

def main():
    st.sidebar.title("Navigation")
    pages = {
        "Login": login_page,
        "Main Page": main_page,
        "Secure Page": secure_page
    }

    if check_login():
        pages["Logout"] = logout
        choice = st.sidebar.radio("Choose a page", list(pages.keys()))
        if choice == "Logout":
            logout()
            st.sidebar.success("You have been logged out.")
            st.experimental_rerun()
        else:
            pages[choice]()
    else:
        login_page()

if __name__ == "__main__":
    main()
