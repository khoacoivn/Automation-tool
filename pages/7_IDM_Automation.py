import time
import streamlit as st
import pandas as pd


from Activity.idm_actions import (
    login_to_site,
    search_user_by_login_name,
    access_user_profile,
    get_user_info,
    search_user_in_modify

)


def main():

    st.title("IDM Automation")
    st.divider()
    st.subheader("Extract data from IDM in user")
    right_col, left_col = st.columns([5, 5])
    data_extract_options = ["User Hr Code", "User Email", "User Title", "User Job Position",
                            "User Department", "User Division", "User Manager", "User Status"]
    idm_login_name_input_area = right_col.text_area("Input IDM login here")
    idm_login_name_input_list = idm_login_name_input_area.split(
        "\n")  # This return a list
    left_col.text("Choose what info you wanna extract")

# Get current selections
    selected_options = [
        opt for opt in data_extract_options if st.checkbox(opt)]

    user_data = {option: [] for option in selected_options}

    test_button = st.button("Test button")

    # if selected_options:

    #     data = {col: range(1, 4) for col in selected_options}

    #     df = pd.DataFrame(data)
    # else:
    #     st.write("Please select at least one option.")

    if test_button:
        idm_page = login_to_site()
        time.sleep(15)
        idm_page.click_user_tab()
        time.sleep(1)
        idm_page.click_manage_user()
        for login_name in idm_login_name_input_list:
            search_user_by_login_name(
                idm_page=idm_page, user_login_name=login_name)
            access_user_profile(idm_page=idm_page)
            # # value = get_user_info(idm_page=idm_page, element_id="USER_ID")

            if "User Hr Code" in selected_options:
                try:
                    user_hr_code = get_user_info(
                        idm_page=idm_page, element_id="USER_ID")
                    user_data["User Hr Code"].append(user_hr_code)
                except Exception:
                    user_data["User Hr Code"].append(None)

            if "User Email" in selected_options:
                try:
                    user_email = get_user_info(
                        idm_page=idm_page, element_id="EMAIL")
                    user_data["User Email"].append(user_email)
                except Exception:
                    user_data["User Email"].append(None)

            if "User Title" in selected_options:
                try:
                    user_title = get_user_info(
                        idm_page=idm_page, element_id="title")
                    user_data["User Title"].append(user_title)
                except Exception:
                    user_data["User Title"].append(None)

            if "User Job Position" in selected_options:
                try:
                    user_job_position = get_user_info(
                        idm_page=idm_page, element_id="idmJobPosition")
                    user_data["User Job Position"].append(user_job_position)
                except Exception:
                    user_data["User Job Position"].append(None)

            if "User Department" in selected_options:
                try:
                    user_department = get_user_info(
                        idm_page=idm_page, element_id="organizationName")
                    user_data["User Department"].append(user_department)
                except Exception:
                    user_data["User Department"].append(None)

            if "User Division" in selected_options:
                try:
                    user_division = get_user_info(
                        idm_page=idm_page, element_id="idmCustomAttribute17")
                    user_data["User Division"].append(user_division)
                except Exception:
                    user_data["User Division"].append(None)

            if "User Manager" in selected_options:
                try:
                    user_manager = get_user_info(
                        idm_page=idm_page, element_id="idmManagerName")
                    user_data["User Manager"].append(user_manager)
                except Exception:
                    user_data["User Manager"].append(None)

            if "User Status" in selected_options:
                try:
                    user_status = get_user_info(
                        idm_page=idm_page, element_id="idmUserStatus")
                    user_data["User Status"].append(user_status)
                except Exception:
                    user_data["User Status"].append(None)
            idm_page.get_idm_url()
            idm_page.click_login_button()

    df = pd.DataFrame(user_data)
    st.dataframe(df)

    st.divider()
    st.subheader("Extract data from IDM modify user")
    right_col, left_col = st.columns([5, 5])
    data_extract_from_modify_options = ["User Manager Account"]
    idm_login_name_input_area = right_col.text_area("Input Hr code here")
    idm_login_name_input_list = idm_login_name_input_area.split(
        "\n")  # This return a list
    left_col.text("Choose what info you wanna extract")
    # Get current selections
    selected_options_for_modify = [
        opt for opt in data_extract_from_modify_options if st.checkbox(opt)]

    user_data = {option: [] for option in selected_options_for_modify}

    get_modify_info_button = st.button("Get infor")

    if get_modify_info_button:
        idm_page = login_to_site()
        time.sleep(15)
        idm_page.click_user_tab()
        time.sleep(1)
        idm_page.click_manage_user()
        time.sleep(1)
        idm_page.click_view_user_modify()
        for login_name in idm_login_name_input_list:
            search_user_in_modify(
                idm_page=idm_page, user_login_name=login_name)
            access_user_profile(idm_page=idm_page)

            if "User Manager Account" in selected_options_for_modify:
                try:
                    user_manager_account = get_user_info(
                        idm_page=idm_page, element_id="idmCustomAttribute26")
                    user_data["User Manager Account"].append(
                        user_manager_account)
                except Exception:
                    user_data["User Manager Account"].append(None)
            idm_page.get_idm_url()
            idm_page.click_login_button()

    df = pd.DataFrame(user_data)
    st.dataframe(df)


if __name__ == "__main__":
    main()
