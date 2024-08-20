import json
import os
import logging
from oop_projects.hurfiesh_jobs.logger_setup import LoggingSetup
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
            logging.error('Professional name cannot be empty')
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
            logging.error('Professional phone cannot be empty')
            raise ValueError('Professional phone cannot be empty')
        elif self._phone is not int:
            logging.error('Professional phone must be a number')
            raise ValueError('Professional phone must be a number')
        elif not 9 < self._phone < 11:
            logging.error('Professional phone must be 9-11 digits')
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
            logging.error('Professional profession cannot be empty')
            raise ValueError('Professional profession cannot be empty')
        else:
            self._profession = value

    def to_dict(self):
        return {
            "name": self._name,
            "phone": self._phone,
            "profession": self._profession
        }

    def remove_professional(self, name):
        try:
            with open(self._config_file_path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            logging.error(f"File {self._config_file_path} not found.")
            # If the file doesn't exist, initialize it with an empty structure.
            data = {'jobs': [],
                    'professionals': []}
            return
        except json.JSONDecodeError:
            logging.error(f"Error in reading file {self._config_file_path}.")
            # If there's an error in reading the file, also initialize it.
            data = {'jobs': [],
                    'professionals': []}
            return
        professional_found = False
        for professional in data['professionals']:
            if professional['name'] == name:
                data['professionals'].remove(professional)
                professional_found = True
                logging.info(f"Professional: {name} was removed successfully.")
                break
        if professional_found:
            with open(self._config_file_path, 'w') as file:
                json.dump(data, file, indent=1)
        else:
            logging.error(f"Professional: {name} not found.")

    def add_professional(self):
        # Step 1: Open and load the current data from the JSON file.
        try:
            with open(self._config_file_path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            logging.error(f"File {self._config_file_path} not found.")
            # If the file doesn't exist, initialize it with an empty structure.
            data = {'jobs': [],
                    'professionals': []}
            return
        except json.JSONDecodeError:
            logging.error(f"Error in reading file {self._config_file_path}.")
            # If there's an error in reading the file, also initialize it.
            data = {'jobs': [],
                    'professionals': []}
            return
        # Step 2: Append the new professional to the 'professionals' list.
        data['professionals'].append(self.to_dict())

        # Step 3: Write the updated data back to the JSON file.
        with open(self._config_file_path, 'w') as file:
            json.dump(data, file, indent=1)
            logging.info(f"Professional: {self._name} was added successfully.")
