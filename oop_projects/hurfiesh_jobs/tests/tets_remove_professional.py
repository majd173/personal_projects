import unittest
from oop_projects.hurfiesh_jobs.src.classes.professional import Professional


class TestRemoveProfessional(unittest.TestCase):
    """
    This class tests removing a professional.
    """

    def test_remove_professional(self):
        """
        This method tests removing a professional.
        """
        self._professional_object = Professional.generate_random_professional()
        self._professional_object.add_professional()
        self._professional_object.remove_professional(self._professional_object.name)
        self.assertNotIn(self._professional_object.name, Professional.return_professionals_name())


if __name__ == '__main__':
    unittest.main()
