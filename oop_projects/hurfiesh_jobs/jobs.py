import json
import os
import logging
from oop_projects.hurfiesh_jobs.logger_setup import LoggingSetup
from oop_projects.hurfiesh_jobs.config_provider import ConfigProvider
from oop_projects.hurfiesh_jobs.professional import Professional


class Job:

    def __init__(self, title):
        self._title = title
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, 'horfiesh.json')
        self._config = ConfigProvider()

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
        if self._title == '':
            logging.error('Job title cannot be empty')
            raise ValueError('Job title cannot be empty')
        else:
            self._title = value

    def to_dict(self, professional: Professional):
        return {
            "title": self._title,
            "professional": professional
        }

    def remove_job(self, title):
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
        for job in data['jobs']:
            if job['title'] == title:
                data['jobs'].remove(job)
                logging.info(f"Job: {title} was removed successfully.")
                break
            else:
                logging.error(f"Job: {title} not found.")

    def add_job(self, professional: Professional):
        # Step 1: Open and load the current data from the JSON file.
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
        if professional is not None:
            professional_name = professional['name']
        else:
            professional_name = None

        # Step 2: Append the new job to the 'jobs' list.
        data['jobs'].append(self.to_dict(professional))

        # Step 3: Write the updated data back to the JSON file.
        with open(self._config_file_path, 'w') as file:
            json.dump(data, file, indent=1)
            logging.info(f"Job: {self._title} was added successfully includes professional: {professional_name}.")
