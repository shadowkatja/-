from selene import have, command
from selene.support.shared import browser

from tests_demo import recourses


class RegistrationPage:

    def open_form(self):
        browser.open('/automation-practice-form')
        browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.75)"')
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def fill_gender(self):
        browser.element('[for="gender-radio-1"]').click()
        return self

    def fill_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element('.react-datepicker__year-select').click().send_keys(year)
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def fill_subjects(self, value):
        browser.element('#subjectsInput').click().type(value).press_enter()
        return self

    def fill_hobbies(self, value):
        #browser.with_(timeout=browser.config.timeout * 2).element('[for="hobbies-checkbox-1"]').click()
        browser.all('.custom-control').element_by(have.exact_text(value)).click()
        return self

    def scroll_form(self):
        browser.element('#submit').perform(command.js.scroll_into_view)
        return self

    def add_image(self, picture_name):
        browser.element('#uploadPicture').send_keys(recourses.path(picture_name))
        return self

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def fill_state(self,value):
        browser.element('[id="state"]').click()
        browser.all('[id^="react-select"][id*=option]').element_by(have.exact_text(value)).click()
        return self

    def fill_city(self,value):
        browser.element('[id="city"]').click()
        browser.all('[id^="react-select"][id*=option]').element_by(have.exact_text(value)).click()
        return self

    def submit_form(self):
        browser.element('#submit').perform(command.js.click)

    def should_have_registrated_user_with(self, full_name, email, gender, number, date_of_birth,
                                          subjects, hobbies, picture, current_address, state_and_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                number,
                date_of_birth,
                subjects,
                hobbies,
                picture,
                current_address,
                state_and_city
            )
        )