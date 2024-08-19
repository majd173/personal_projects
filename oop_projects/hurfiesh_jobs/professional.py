import json
import os
from oop_projects.hurfiesh_jobs.config_provider import ConfigProvider


class Professional:
    def __init__(self, name, phone, profession):
        self._name = name
        self._profession = profession
        self._phone = phone
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, 'horfiesh.json')
        self._config = ConfigProvider()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        if self._name == '':
            raise ValueError('Professional name cannot be empty')
        else:
            self._name = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
        if self._phone == '':
            raise ValueError('Professional phone cannot be empty')
        elif self._phone is not int:
            raise ValueError('Professional phone must be a number')
        elif not 9 < self._phone < 11:
            raise ValueError('Professional phone must be 9-11 digits')
        else:
            self._phone = value

    @property
    def profession(self):
        return self._profession

    @profession.setter
    def profession(self, value):
        self._profession = value
        if self._profession == '':
            raise ValueError('Professional profession cannot be empty')
        else:
            self._profession = value

    def to_dict(self):
        return {
            "name": self._name,
            "phone": self._phone,
            "profession": self._profession
        }

    def add_professional(self):
        with open(self._config_file_path, 'r') as file:
            data = json.load(file)
            data['professionals'].append(self.to_dict())

        with open(self._config_file_path, 'w') as file:
            json.dump(data, file, indent=1)
