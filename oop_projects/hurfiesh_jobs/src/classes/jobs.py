import json
import os
import logging
from oop_projects.hurfiesh_jobs.src.utilities.logger_setup import LoggingSetup
from oop_projects.hurfiesh_jobs.src.utilities.config_provider import ConfigProvider
from oop_projects.hurfiesh_jobs.src.classes.professional import Professional


class Job:

    def __init__(self, title):
        self._title = title
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, '..\..\horfiesh.json')
        self._config = ConfigProvider().load_from_file(self._config_file_path)

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
        if professional is None:
            return {
                "title": self._title,
                "professionals": None
            }
        return {
            "title": self._title,
            "professionals": [professional.to_dict()]
        }

    @staticmethod
    def show_jobs():
        try:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            config_file_path = os.path.join(base_dir, '..\..\horfiesh.json')
            config = ConfigProvider().load_from_file(config_file_path)

            with open(config_file_path, 'r') as file:
                data = json.load(file)
                if data is None:
                    print("No jobs found.")
                    return
                if data['jobs'] is None:
                    print("No jobs found.")
                    return
                if len(data['jobs']) > 0:
                    for job in data['jobs']:
                        if job:
                            print(f'Job title: {job["title"]}')
                else:
                    print("No jobs found.")
        except FileNotFoundError:
            logging.error(f"File {config} not found.")
        except json.JSONDecodeError:
            logging.error(f"Error in reading file {config}.")

    def remove_job(self, title):
        try:
            # Step 1: Open and load the current data from the JSON file.
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
        job_found = False
        for job in data['jobs']:
            if job['title'] == title:
                data['jobs'].remove(job)
                job_found = True
                logging.info(f"Job: {title} was removed successfully.")
                break
        if job_found:
            with open(self._config_file_path, 'w') as file:
                json.dump(data, file)
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

        # Step 2: Append the new job to the 'jobs' list.
        if professional is None:
            data['jobs'].append(self.to_dict(None))
        else:
            data['jobs'].append(self.to_dict(professional))
            data['professionals'].append(professional.to_dict())

        # Step 3: Write the updated data back to the JSON file.
        with open(self._config_file_path, 'w') as file:
            json.dump(data, file, indent=1)
            if professional is None:
                logging.info(f"Job: {self._title} was added successfully.")
            else:
                logging.info(f"Job: {self._title} was added successfully includes professional: {professional.name}.")

    @staticmethod
    def return_jobs_titles():
        """
        This method returns all the jobs titles in the config file.
        :return: jobs_title: list
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_file_path = os.path.join(base_dir, '..\..\horfiesh.json')
        config = ConfigProvider().load_from_file(config_file_path)
        jobs_title = []
        for job in config['jobs']:
            jobs_title.append(job['title'])
        return jobs_title
