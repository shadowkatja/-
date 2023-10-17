from tests_demo.pages.registration_page import RegistrationPage


def test_submit_student_registration_form_by_mid_steps():
    registration_page = RegistrationPage()

    registration_page.open_form()
    registration_page.fill_first_name('Charles')
    registration_page.fill_last_name('Leclerc')
    registration_page.fill_email('CL16@test.com')
    registration_page.fill_gender()
    registration_page.fill_number('7900900909')
    registration_page.fill_date_of_birth(year='1997', month='October', day='16')
    registration_page.fill_subjects('Arts')
    registration_page.fill_hobbies('Sports')
    registration_page.scroll_form()
    registration_page.add_image('image.png')
    registration_page.fill_address('Monaco, Avenue de la Costa')
    registration_page.fill_state('Haryana')
    registration_page.fill_city('Panipat')
    registration_page.submit_form()

    # checking
    registration_page.should_have_registrated_user_with(
        'Charles Leclerc',
        'CL16@test.com',
        'Male',
        '7900900909',
        '16 October,1997',
        'Arts',
        'Sports',
        'image.png',
        'Monaco, Avenue de la Costa',
        'Haryana Panipat'
    )
