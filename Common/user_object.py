
class User:
    """This is a class represent user information on SD Automation Hub
    """

    def __init__(self, username: str, display_name: str, roles: list, hr_code: str, job_title: str, account_type: int = 1, last_logon: str = "") -> None:
        """Initialize a user session object
        """
        self.username = username
        self.display_name = display_name
        self.roles = roles
        self.hr_code = hr_code
        self.job_title = job_title
        self.account_type = account_type
        self.last_logon = last_logon

    def get_user_information(self, search_query: str) -> User:

        user_information
