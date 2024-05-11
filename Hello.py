import streamlit as st
from auth import check_login, login, logout
from automobile_case_study import automobile_case_study  # Import the module

def main_page():
    st.title("Main Page")
    st.write("This is the main page of the application.")

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
        "Automobile Case Study": automobile_case_study  # Replace "Secure Page" with this
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
