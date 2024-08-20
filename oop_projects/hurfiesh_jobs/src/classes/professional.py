import json
import os
import logging
from oop_projects.hurfiesh_jobs.src.utilities.config_provider import ConfigProvider


class Professional:
    """
    This class manages professional data.
    Args:
        name (str): The name of the professional.
        phone (str): The phone number of the professional.
        profession (str): The profession of the professional.
    """
    def __init__(self, name, phone, profession):
        self._name = name
        self._profession = profession
        self._phone = phone
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, '..\..\horfiesh.json')
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
        """
        This method returns the professional data as a dictionary.
        :return: professional data.
        """
        return {
            "name": self._name,
            "phone": self._phone,
            "profession": self._profession
        }

    def add_professional(self):
        """
        This method adds the professional data to the config file.
        """
        try:
            with open(self._config_file_path, 'r') as file:
                data = json.load(file)
            data['professionals'].append(self.to_dict())
            with open(self._config_file_path, 'w') as file:
                json.dump(data, file)
        except FileNotFoundError:
            logging.error(f"File {self._config_file_path} not found.")
        except json.JSONDecodeError:
            logging.error(f"Error in reading file {self._config_file_path}.")

    @staticmethod
    def show_professionals():
        """
        This method shows all the professionals in the config file.
        """
        try:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            config_file_path = os.path.join(base_dir, '..\..\horfiesh.json')
            with open(config_file_path, 'r') as file:
                data = json.load(file)
                if data is None:
                    print("No professionals found.")
                    return
                if data['professionals'] is None:
                    print("No professionals found.")
                    return
                if len(data['professionals']) > 0:
                    for professional in data['professionals']:
                        if professional:
                            print(f'Professional name: {professional["name"]}')
                else:
                    print("No professionals found.")
        except FileNotFoundError:
            logging.error(f"File {config_file_path} not found.")
        except json.JSONDecodeError:
            logging.error(f"Error in reading file {config_file_path}.")

    def remove_professional(self, name):
        """
        This method removes a professional from the config file by his name.
        :param name:
        """
        try:
            # Step 1: Open and load the current data from the JSON file.
            with open(self._config_file_path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            logging.error(f"File {self._config_file_path} not found.")
            # If the file doesn't exist, initialize it with an empty structure.
            data = {'jobs': [],
                    'professionals': []}

        except json.JSONDecodeError:
            logging.error(f"Error in reading file {self._config_file_path}.")
            # If there's an error in reading the file, also initialize it.
            data = {'jobs': [],
                    'professionals': []}

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

    def add_a_professional(self):
        """
        This method adds a professional data to the config file.
        """
        try:
            # Step 1: Open and load the current data from the JSON file.
            with open(self._config_file_path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            logging.error(f"File {self._config_file_path} not found.")
            # If the file doesn't exist, initialize it with an empty structure.
            data = {'jobs': [],
                    'professionals': []}

        except json.JSONDecodeError:
            logging.error(f"Error in reading file {self._config_file_path}.")
            # If there's an error in reading the file, also initialize it.
            data = {'jobs': [],
                    'professionals': []}

        # Step 2: Append the new professional to the 'professionals' list.
        data['professionals'].append(self.to_dict())

        # Step 3: Write the updated data back to the JSON file.
        with open(self._config_file_path, 'w') as file:
            json.dump(data, file, indent=1)
            logging.info(f"Professional: {self._name} was added successfully.")
