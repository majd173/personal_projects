import os
import unittest
from oop_projects.hurfiesh_jobs.src.utilities.utilities import Utilities
from oop_projects.hurfiesh_jobs.src.classes.professional import Professional
from oop_projects.hurfiesh_jobs.src.classes.jobs import Job
from oop_projects.hurfiesh_jobs.src.utilities.config_provider import ConfigProvider


class TestAddJob(unittest.TestCase):
    """
    This class tests adding a job.
    """

    def setUp(self):
        """
        This method runs before each test.
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, '..\horfiesh.json')
        self._config = ConfigProvider().load_from_file(self._config_file_path)
        self._remove1 = False
        self._remove2 = False

    def test_add_only_job(self):
        """
        This method tests adding only a job without a professional.
        """
        self._job_title_1 = Utilities.generate_random_string_only_letters(7)
        self._job_1 = Job(self._job_title_1)
        self._job_1.add_job(None)

        self.assertIn(self._job_1.title, Job.return_jobs_titles())
        self._remove1 = True

    def test_add_job_with_professional(self):
        """
        This method tests adding a job with a professional.
        """
        self._job_title_2 = Utilities.generate_random_string_only_letters(7)
        self._generated_professional = Professional.generate_random_professional()
        self._job_2 = Job(self._job_title_2)
        self._job_2.add_job(self._generated_professional)

        self.assertIn(self._job_2.title, Job.return_jobs_titles())
        self.assertIn(self._generated_professional.name, Professional.return_professionals_name())
        self._remove2 = True

    def tearDown(self):
        """
        This method runs after each test and removes added jobs and professionals if they exist.
        """
        if self._remove1:
            self._job_1.remove_job(self._job_title_1)
        if self._remove2:
            self._job_2.remove_job(self._job_title_2)
            self._generated_professional.remove_professional(self._generated_professional.name)
