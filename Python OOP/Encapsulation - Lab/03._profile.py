class Profile:

    def __init__(self, username='', password=''):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.username

    @username.setter
    def username(self, value):
        if 5 <= len(value) <= 15:
            self.__username = value
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, value):
        if len(value) < 8:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        else:
            upper_letter = False
            digit_letter = False
            for letter in value:
                if letter == letter.upper():
                    upper_letter = True
                if letter.isdigit():
                    digit_letter = True
            if upper_letter and digit_letter:
                self.__password = value
            else:
                raise ValueError(
                    "The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f"You have a profile with username: \"{self.__username}\" and password: {len(self.__password) * '*'}"
