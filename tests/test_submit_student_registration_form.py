from tests_demo.data import users_data
from tests_demo.pages.registration_page import RegistrationPage


def test_submit_student_registration_form_by_high_steps():
    registration_page = RegistrationPage()
    user = users_data.Charles_Leclerc

    registration_page.open_form()
    registration_page.submit_form(user)
    registration_page.should_have_registrated_user(user)