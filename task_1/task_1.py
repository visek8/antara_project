import json
import random
from datetime import datetime, timezone, timedelta
import string


class Event:
    def init(self, event_name, place, event_type, event_date, member):
        self.event_name = event_name
        self.place = place
        self.event_type = event_type
        self.event_date = event_date
        self.member = member

    def create_name(self):
        self.event_name = ''.join(random.sample(string.ascii_letters + string.digits, 20))

    def create_place(self):
        place_list = ['zoom', 'telegram']
        self.place = ''.join(random.choice(string.ascii_lowercase) for i in range(10)) or random.choice(place_list)

    def create_type(self):
        event_type_list = ['private', 'meeting', 'corporate', 'other']
        self.event_type = random.choice(event_type_list)

    def create_date(self):
        year = random.randint(2000, 2023)
        month = random.randint(1, 12)
        day = random.randint(1, 31)
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        time_del = random.randint(-12, 14)

        self.event_date = datetime(year, month, day, hour, minute,
                                   tzinfo=timezone(timedelta(hours=time_del)))

    def create_member(self):
        self.member = ['Scott Pierce', 'James Gonzales', 'Ian Price', 'Tim Holmes', 'Joseph Coleman']

    def make_dict(self):
        self.create_name()
        self.create_place()
        self.create_type()
        self.create_date()
        self.create_member()
        event_list = []
        event_name = ['name', str(self.event_name)]
        event_list.append(event_name)
        event_place = ['place', str(self.place)]
        event_list.append(event_place)
        event_type = ['type', str(self.event_type)]
        event_list.append(event_type)
        event_date = ['date', str(self.event_date)]
        event_list.append(event_date)
        event_member = ['members', str(self.member)]
        event_list.append(event_member)
        self.event_dict = dict(event_list)
        return self.event_dict


event_1 = Event()
event_1.make_dict()
event_2 = Event()
event_2.make_dict()
event_3 = Event()
event_3.make_dict()
event_4 = Event()
event_4.make_dict()
event_5 = Event()
event_5.make_dict()
event_6 = Event()
event_6.make_dict()


# class Encoder(json.JSONEncoder):
#     def default(self, o):
#         return o

class File:
    def __init__(self, obj_1, obj_2, obj_3, obj_4, obj_5, obj_6):
        self.obj_1 = obj_1
        self.obj_2 = obj_2
        self.obj_3 = obj_3
        self.obj_4 = obj_4
        self.obj_6 = obj_5
        self.obj_5 = obj_6

    def make_json(self):
        with open('event.json', 'w') as file:
            json.dump(self.obj_1, file, indent=4)
            json.dump(self.obj_2, file, indent=4)
            json.dump(self.obj_3, file, indent=4)
            json.dump(self.obj_4, file, indent=4)
            json.dump(self.obj_5, file, indent=4)
            json.dump(self.obj_6, file, indent=4)

    # def update_json(self):
    #     with open('event.json', 'w') as f:
    #         json.dump(self.obj, f, indent=4)


# json_str = json.dumps(event_1.make_dict(), cls=Encoder, indent=4)
# print(json_str)
#
# py_obj = json.loads(json_str)
# print(type(py_obj))

js_file = File(event_1.make_dict(), event_2.make_dict(), event_3.make_dict(), event_4.make_dict(), event_5.make_dict(),
               event_6.make_dict())
js_file.make_json()


class To_Py:

    def py_dict(self):
        with open('event.json', 'r') as f:
            s = f.read()
            person_dict = json.loads(s)
            print(type(person_dict))


glossary = To_Py()
glossary.py_dict()
