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
        self._professional_object = Professional.generate_random_professional()
        self._job_2 = Job(self._job_title_2)
        self._job_2.add_job(self._professional_object)

        self.assertIn(self._job_2.title, Job.return_jobs_titles())
        self.assertIn(self._professional_object.name, Professional.return_professionals_name())
        self._remove2 = True

    def tearDown(self):
        """
        This method runs after each test and removes added jobs and professionals if they exist.
        """
        if self._remove1:
            self._job_1.remove_job(self._job_title_1)
        if self._remove2:
            self._job_2.remove_job(self._job_title_2)
            self._professional_object.remove_professional(self._professional_object.name)
