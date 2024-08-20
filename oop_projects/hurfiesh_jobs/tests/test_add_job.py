import os
import unittest
from oop_projects.hurfiesh_jobs.src.utilities.utilities import Utilities
from oop_projects.hurfiesh_jobs.src.classes.professional import Professional
from oop_projects.hurfiesh_jobs.src.classes.jobs import Job
from oop_projects.hurfiesh_jobs.src.utilities.config_provider import ConfigProvider


class TestAddJob(unittest.TestCase):

    def setUp(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, '..\horfiesh.json')
        self._config = ConfigProvider().load_from_file(self._config_file_path)

    def test_add_only_job(self):
        job_title = Utilities.generate_random_string_only_letters(10)
        job = Job(job_title)
        job.add_job(None)
        self.assertIn(self._config['jobs'][0]['title'], job_title)