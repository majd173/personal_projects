import json
import os
import logging
from oop_projects.hurfiesh_jobs.src.utilities.utilities import Utilities
from oop_projects.hurfiesh_jobs.src.utilities.logger_setup import LoggingSetup
from oop_projects.hurfiesh_jobs.src.utilities.config_provider import ConfigProvider


class Professional:
    """
    This class manages professional data.
    Args:
        name (str): The name of the professional.
        phone (str): The phone number of the professional.
        services (list): The list of services offered by the professional.
    """

    def __init__(self, name, phone, services):
        self._name = name
        self._phone = phone
        self._services = services
        if self._services:
            self._services = [service.strip() for service in self._services.split(',')]
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, '..\..\horfiesh.json')
        self._config = ConfigProvider().load_from_file(self._config_file_path)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == '':
            logging.error('Professional name cannot be empty')
            raise ValueError('Professional name cannot be empty')
        else:
            self._name = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if value == '':
            logging.error('Professional phone cannot be empty')
            raise ValueError('Professional phone cannot be empty')
        elif value is not int:
            logging.error('Professional phone must be a number')
            raise ValueError('Professional phone must be a number')
        elif not 9 < value < 11:
            logging.error('Professional phone must be 9-11 digits')
            raise ValueError('Professional phone must be 9-11 digits')
        else:
            self._phone = value

    @property
    def services(self):
        return self._services

    @services.setter
    def services(self, value):
        if self._services == '':
            logging.error('Professional services cannot be empty')
            raise ValueError('Professional services cannot be empty')
        else:
            self._services = value

    def to_dict(self):
        """
        This method returns the professional data as a dictionary.
        :return: professional data.
        """
        return {
            "name": self._name,
            "phone": self._phone,
            "services": self._services
        }

    def add_professional(self):
        """
        This method adds the professional data to the config file.
        """
        try:
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

        data['professionals'].append(self.to_dict())
        with open(self._config_file_path, 'w') as file:
            json.dump(data, file, indent=4)
            logging.info(f"Professional: {self._name} was added successfully.")

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
        except FileNotFoundError:
            logging.error(f"File {config_file_path} not found.")
        except json.JSONDecodeError:
            logging.error(f"Error in reading file {config_file_path}.")

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
                        return f'Professional name: {professional["name"]}'
                else:
                    print("No professionals found.")

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
                json.dump(data, file, indent=4)
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

        for professional in data['professionals']:
            if professional['name'] == self._name:
                logging.error(f"Professional: {self._name} already exists.")
                print(f"Professional: {self._name} already exists.")
                return

        # Step 2: Append the new professional to the 'professionals' list.
        data['professionals'].append(self.to_dict())

        # Step 3: Write the updated data back to the JSON file.
        with open(self._config_file_path, 'w') as file:
            json.dump(data, file, indent=4)
            logging.info(f"Professional: {self._name} was added successfully.")
            return f"Professional: {self._name} was added successfully."

    @staticmethod
    def return_professionals_name():
        """
        This method returns all the names of the professionals in the config file.
        :return: names of the professionals: list
        """
        try:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            config_file_path = os.path.join(base_dir, '..\..\horfiesh.json')
            config = ConfigProvider().load_from_file(config_file_path)
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
                            print(f'Professional: {professional["name"]}')
                            return f'Professional: {professional["name"]}'
                else:
                    print("No professionals found.")
        except FileNotFoundError:
            logging.error(f"File {config} not found.")
        except json.JSONDecodeError:
            logging.error(f"Error in reading file {config}.")


    @staticmethod
    def generate_random_professional():
        """
        This method generates a random professional.
        :return: generated_professional: Professional
        """
        professional_name = Utilities.generate_random_string_only_letters(7)
        professional_phone = Utilities.generate_random_number_by_length(10)
        professional_services = Utilities.generate_random_string_only_letters(12)
        generated_professional = (Professional
                                  (professional_name, professional_phone, professional_services))
        return generated_professional

    @staticmethod
    def find_professional(name):
        try:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            config_file_path = os.path.join(base_dir, '..\..\horfiesh.json')
            config = ConfigProvider().load_from_file(config_file_path)
            with open(config_file_path, 'r') as file:
                data = json.load(file)

        except FileNotFoundError:
            logging.error(f"File {config} not found.")
            # If the file doesn't exist, initialize it with an empty structure.
            data = {'jobs': [],
                    'professionals': []}

        except json.JSONDecodeError:
            logging.error(f"Error in reading file {config}.")
            # If there's an error in reading the file, also initialize it.
            data = {'jobs': [],
                    'professionals': []}

        for professional in data['professionals']:
            if professional.get('name') == name:
                print(f"Professional: {professional['name']}")
                return (f"Professional Name: {professional['name']}\n"
                        f"Professional Phone: {professional['phone']}\n"
                        f"Professional Services: {professional['services']}")
            logging.error(f"Professional: {name} not found.")
            return None  # Return None or an appropriate message if not found


