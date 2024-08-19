import json
import os
from oop_projects.hurfiesh_jobs.config_provider import ConfigProvider


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
            raise ValueError('Job title cannot be empty')
        else:
            self._title = value

    def to_dict(self):
        return {
            "title": self._title
        }

    def add_job(self):
        with open(self._config_file_path, 'r') as file:
            data = json.load(file)
            data['jobs'].append(self.to_dict())

        with open(self._config_file_path, 'w') as file:
            json.dump(data, file, indent=1)
