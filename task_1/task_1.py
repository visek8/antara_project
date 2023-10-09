import json
import random
from datetime import datetime, timezone, timedelta
import string


class Event:

    @staticmethod
    def event_name():
        letters_and_digits = string.ascii_letters + string.digits
        name = ''.join(random.sample(letters_and_digits, 20))
        event_name = ['event_name']
        return event_name.append(name)

    @staticmethod
    def place():
        place_list = ['zoom', 'telegram']
        letters = string.ascii_lowercase
        place = ''.join(random.choice(letters) for i in range(10))
        lst_place = ['place']
        return lst_place.append(place or random.choice(place_list))

    @staticmethod
    def event_type():
        event_type_list = ['private', 'meeting', 'corporate', 'other']
        event_type = random.choice(event_type_list)
        lst_type = ['type']
        return lst_type.append(event_type)

    @staticmethod
    def event_date():
        year = random.randint(2000, 2023)
        month = random.randint(1, 12)
        day = random.randint(1, 31)
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        time_del = random.randint(-12, 14)

        event_date = datetime(year, month, day, hour, minute,
                              tzinfo=timezone(timedelta(hours=time_del)))
        lst_date = ['date']
        return lst_date.append(event_date)

    def member(self):
        member = ['Scott Pierce', 'James Gonzales', 'Ian Price', 'Tim Holmes', 'Joseph Coleman']
        lst_members = ['members']
        return lst_members.append(member)

    def make_dict(self):
        pass


event_1 = Event()


class Encoder(json.JSONEncoder):
    pass
