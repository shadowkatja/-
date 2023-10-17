from selene import have
from selene import command
from selene.support.shared import browser

import tests_demo.recourses


def test_submit_student_registration_form():
    # open url
    browser.open('/automation-practice-form')
    browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.75)"')
    # Fill name
    browser.element('#firstName').type('Charles')
    browser.element('#lastName').type('Leclerc')
    # Fill email
    browser.element('#userEmail').type('CL16@test.com')
    # Fill gender
    browser.element('[for="gender-radio-1"]').click()
    # fill phone number
    browser.element('#userNumber').type('7900900909')
    # fill birthdate
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys('October')
    browser.element('.react-datepicker__year-select').click().send_keys('1997')
    browser.element(f'.react-datepicker__day--0{16}').click()
    # fill subjects
    browser.element('#subjectsInput').click().type('arts').press_enter()
    # fill hobbies
    browser.all('.custom-control').element_by(have.exact_text("Sports")).click()
    # scrolling to submit button
    browser.element('#submit').perform(command.js.scroll_into_view)
    # add picture
    browser.element('#uploadPicture').send_keys(tests_demo.recourses.path('image.png'))
    # add address
    browser.element('#currentAddress').type('Monaco, Avenue de la Costa')
    # add state and city
    browser.element('[id="state"]').click()
    browser.all('[id^="react-select"][id*=option]').element_by(have.exact_text('Haryana')).click()
    browser.element('[id="city"]').click()
    browser.all('[id^="react-select"][id*=option]').element_by(have.exact_text('Panipat')).click()
    # press submit
    browser.element('#submit').click()

    # checking
    browser.element('.table').all('tr td:nth-child(2)').should(have.texts
        (
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
    ))
