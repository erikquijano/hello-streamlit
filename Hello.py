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

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Automobile case study 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        ABC Cardeals Pvt Ltd maintains caller’s data who are looking to buy new or used cars. Prospects can call or write an email and a support is given in terms of choosing the desired cars. 
    """
    )


if __name__ == "__main__":
    run()

import streamlit as st

# Create session state variables for managing login status and user session
if 'login_status' not in st.session_state:
    st.session_state['login_status'] = False

def login(username, password):
    # Simple check for username and password
    if username == "admin" and password == "testuser20":
        st.session_state['login_status'] = True
    else:
        st.session_state['login_status'] = False
        st.error("Incorrect Username or Password")

def logout():
    st.session_state['login_status'] = False

# Layout for login
def main():
    st.title("Streamlit Application")

    # Check if the user is logged in
    if st.session_state['login_status']:
        st.success("Logged in as admin")
        st.button("Logout", on_click=logout)
        # Your application code goes here
        st.write("Welcome to the secure part of the app!")

    else:
        # Login form
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            login_button = st.form_submit_button("Login", on_click=login, args=(username, password))
            if login_button:
                if st.session_state['login_status']:
                    st.success("Login Successful!")
                else:
                    st.error("Login Failed. Try Again!")

if __name__ == "__main__":
    main()
