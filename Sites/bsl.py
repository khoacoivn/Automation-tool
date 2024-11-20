import logging
from Common.page_object import page_object as Page

#Element Path
class bsl(Page):
    """This is a wrapper for BSL Page, based on the customed Page Object, which is also a wrapper of Selenium driver

    Args:
        Page (_type_): This is a wrapper for Selenium driver
        
    Returns:
        _type_: A customed BSL object    
    """
    
    #Base URL
    bsl_url = "https://bsl.pdcvn1.vn.prod/bsl"
    
    # Login/Logout
    ldap_user_input = '//*[@id="username"]'
    ldap_pw_input = '//*[@id="password"]'
    login_button = '//*[@id="kc-login"]'
    logout_button = '//*[contains(text(),"Logout")]' #Need update
    
    # Landing Xpath
    find_bank_branch_button = '//div[contains(text(), "Find bank branch")]'
    find_bank_button = '//*[@data-better-uid="menu:uc00-110:code"][contains(text(), "Find bank")]'
    
    # Find bank Xpath
    bank_name_input = '//*[@data-uid="name"]'
    bank_code_input = '//*[@data-uid="code"]'
    search_button = '//*[@name="buttonPanel:search"]'
    
    #Function
    def get_bsl_url(self) -> None:
        """
        This method navigates to the UMC URL.
        """
        self.get(self.bsl_url)
        
    def login_with_data(self, ldap_user: str, ldap_pw: str) -> bool:
        """
        This method logs in with the provided LDAP user and password.

        Args:
            ldap_user (str): The LDAP username.
            ldap_pw (str): The LDAP password.

        Returns:
            bool: True if login is successful, False otherwise.
        """
        if (ldap_user is not None) & (ldap_pw is not None):
            self.search_by_xpath(self.ldap_user_input, delay=0.5).send_keys(ldap_user)
            self.search_by_xpath(self.ldap_pw_input, delay=0.5).send_keys(ldap_pw)
            return self.search_by_xpath(self.login_button, delay=0.5).click()
        else:
            logging.critical("Missing Username or Password.")
            return False
        
    def logout(self) -> None:
        """
        This method logs out of the current session.
        """
        #self.search_by_xpath(self.logout_button).click()
        pass
    
    def click_find_bank(self) -> None:
        """
        This method click find bank button on Homepage
        """
        self.search_by_xpath(self.find_bank_button)
        
    def click_find_bankbranch(self) -> None:
        """
        This method click find bank branch button on Homepage
        """
        self.search_by_xpath(self.find_bank_branch_button)