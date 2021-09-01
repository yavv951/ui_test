from faker import Faker

fake = Faker()


class AuthData:
    def __init__(self, login=None, password=None):
        self.login = login
        self.password = password

    @staticmethod
    def random():
        login = fake.email()
        password = fake.password()
        return AuthData(login, password)


"""moodle_net_profile=None,
        city=None,
        timezone=None,
        country_code=None,
        about=None,
        url=None,
        image_url=None,"""


class PersonalData:
    def __init__(self, firstname=None, lastname=None, user_email=None):
        self.firstname = firstname
        self.lastname = lastname
        self.user_email = user_email
        # self.moodle_net_profile = moodle_net_profile
        # self.city = city
        # self.timezone = timezone
        # self.country_code = country_code
        # self.about = about
        # self.url = url
        # self.image_url = image_url

    @staticmethod
    def random():
        firstname = fake.first_name()
        lastname = fake.last_name()
        user_email = fake.email()
        # moodle_net_profile = fake.url()
        # city = fake.city_name()
        # timezone = random.choice(PersonalDataConstants.TIMEZONE_VALUES)
        # country_code = fake.country_code()
        # about = fake.text(max_nb_chars=200)
        # url = fake.url()
        # image_url = fake.image_url()
        return PersonalData(
            firstname,
            lastname,
            user_email
            # moodle_net_profile,
            # city,
            # timezone,
            # country_code,
            # about,
            # url,
            # image_url,
        )
