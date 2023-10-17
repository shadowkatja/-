import dataclasses
import datetime


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    number: str
    date_of_birth: datetime.date
    subject: str
    hobbies: str
    picture: str
    address: str
    state: str
    city: str


def __init__(self, first_name, last_name, email, gender, number, date_of_birth,
             subject, hobbies, picture, address, state, city):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.gender = gender
    self.number = number
    self.date_of_birth = datetime.date
    self.subject = subject
    self.hobbies = hobbies
    self.picture = picture
    self.address = address
    self.state = state
    self.city = city

