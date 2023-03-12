class Profile:

    def __init__(self, username, password):
        self.__username = set_username(username)
        self.__password = password(password)

    def get_username(self):
        return self.__username

    def set_username(self, value):
        if len(value) >= 5 and len(value) <= 15:
            self.__username = value
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    def password(self):
        return self.__password

    def password(self, value):
        upper_value = False
        if len(value) >= 8:
            for letter in value:
                if letter == letter.upper():
                    upper_value = True
        if upper_value:
            self.__password = value
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
profile_with_invalid_password = Profile('My_username', 'My-password')