from Common.supporting import (
    login_status_check,
    logout_render,
    request_to_automate_button)
)
import streamlit as st

# This is to jump the user back to login if their are not authenticated
login_status_check()
logout_render()
request_to_automate_button()

def main():
    st.title("Health Check")
    tab1, tab2, tab3 = st.tabs(["Overview", "HomeX", "HomeE"])

    with tab1:
        st.header("System Health Check Overview")
        st.text("This tab provides an overview of the health status of all connected platforms. It displays the results of health checks for HomeX, HomeE, and HOSEL SSO in a consolidated manner. Users can quickly assess the overall system health and identify any issues that may require attention.")

    with tab2:
        st.header("HomeX Health Check")
        st.text("This tab focuses on the health check of the HomeX platform. It performs various checks to ensure that HomeX is functioning correctly, including connectivity tests, API response checks, and performance metrics. Users can view detailed results and logs related to HomeX's health status.")
    with tab3:
        st.header("HomeE Health Check")
        st.text("This tab is dedicated to the health check of the HomeE platform. It conducts comprehensive checks to verify that HomeE is operating smoothly, such as database connectivity, service availability, and error rate monitoring. Users can access detailed insights and reports on HomeE's health status.")
        
