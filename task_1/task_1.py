import json
import random
from datetime import datetime, timezone, timedelta
import string
import argparse


class Event:
    """Создает атрибуты события."""
    def init(self, event_name, place, event_type, event_date, member):
        self.event_name = event_name
        self.place = place
        self.event_type = event_type
        self.event_date = event_date
        self.member = member

    def create_name(self):
        """Случайное название события."""
        self.event_name = ''.join(random.sample(string.ascii_letters + string.digits, 20))

    def create_place(self):
        """Случайное место проведения события, либо одно из предложенных."""
        place_list = ['zoom', 'telegram']
        self.place = ''.join(random.choice(string.ascii_lowercase) for i in range(10)) or random.choice(place_list)

    def create_type(self):
        """Выпадение типа события из предложенных."""
        event_type_list = ['private', 'meeting', 'corporate', 'other']
        self.event_type = random.choice(event_type_list)

    def create_date(self):
        """Рандомная дата события."""
        year = random.randint(2000, 2023)
        month = random.randint(1, 12)
        day = random.randint(1, 31)
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        time_del = random.randint(-12, 14)

        self.event_date = datetime(year, month, day, hour, minute,
                                   tzinfo=timezone(timedelta(hours=time_del)))

    def create_member(self):
        """Участники события."""
        self.member = ['Scott Pierce', 'James Gonzales', 'Ian Price', 'Tim Holmes', 'Joseph Coleman']

    def make_dict(self):
        """Создаем словарь, где ключ - атрибут события, значения - генерируемые данные."""
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


class File:
    """Создаем json-файл."""
    def __init__(self, obj_1, obj_2, obj_3, obj_4, obj_5, obj_6):
        self.obj_1 = obj_1
        self.obj_2 = obj_2
        self.obj_3 = obj_3
        self.obj_4 = obj_4
        self.obj_6 = obj_5
        self.obj_5 = obj_6

    def make_json(self):
        """Создаем json-файл."""
        with open('event.json', 'w') as file:
            self.json_list = []
            self.json_list.append(self.obj_1)
            self.json_list.append(self.obj_2)
            self.json_list.append(self.obj_3)
            self.json_list.append(self.obj_4)
            self.json_list.append(self.obj_5)
            self.json_list.append(self.obj_6)
            json.dump(self.json_list, file, indent=4)


js_file = File(event_1.make_dict(), event_2.make_dict(), event_3.make_dict(), event_4.make_dict(), event_5.make_dict(),
               event_6.make_dict())
js_file.make_json()


class Sorted:
    """Получаем на вход json-файл, на выходу получим файл с отсортированными по дате событиями."""

    def py_dict(self):
        """Конвертируем из json в python-объект."""
        with open('event.json', 'r') as f:
            s = f.read()
            self.person_dict = json.loads(s)

    def sort_dict(self):
        """Сортируем словари в списке по ключу(по дате)."""
        def get_data_for_sort(x):
            return x['date']

        self.sorted_dicts = sorted(self.person_dict, key=get_data_for_sort)

    def make_json_again(self):
        """Конвертируем список с упорядоченными по дате словарями в json-файл."""
        self.py_dict()
        self.sort_dict()
        with open('sorted.json', 'w') as file:
            json.dump(self.sorted_dicts, file, indent=4)

sorted_js = Sorted()
sorted_js.make_json_again()
