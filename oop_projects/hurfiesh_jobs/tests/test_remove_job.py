import unittest
from hurfiesh_jobs.src.classes.jobs import Job
from hurfiesh_jobs.src.utilities.utilities import Utilities


class TestRemoveJob(unittest.TestCase):
    """
    This class tests removing a job.
    """

    def test_remove_job(self):
        """
        This method tests removing a job.
        """
        self._job_title = Utilities.generate_random_string_only_letters(7)
        self._job = Job(self._job_title)
        self._job.add_job(None)
        self._job.remove_job(self._job_title)
        self.assertNotIn(self._job.title, Job.return_jobs_titles())


if __name__ == '__main__':
    unittest.main()
