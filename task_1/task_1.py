import random
from datetime import datetime, date, time, timezone, timedelta
import string


# a = datetime(2023, 5, 19, 21, 49,
#              tzinfo=timezone(timedelta(hours=3)))
# print(a)
#
# event_type_list = ['private', 'meeting', 'corporate', 'other']
# print(random.choice(event_type_list))
#
#
def event_place(length):
    place_list = ['zoom', 'telegram']
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", rand_string or random.choice(place_list))


event_place(random.randint(0, 20))

member_name = ['']

# def event_name(length):
#     letters_and_digits = string.ascii_letters + string.digits
#     rand_string = ''.join(random.sample(letters_and_digits, length))
#     print("Alphanum Random string of length", length, "is:", rand_string)
#
#
# event_name(random.randint(0, 20))


class Ivent:
    def __init__(self, event_date, event_type, event_name, member, place):
        self.event_date = event_date
        self.event_type = event_type
        self.event_name = event_name
        self.member = member
        self.place = place
