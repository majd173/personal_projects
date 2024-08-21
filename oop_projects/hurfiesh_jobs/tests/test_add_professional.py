import unittest
from oop_projects.hurfiesh_jobs.src.classes.professional import Professional


class TestAddProfessional(unittest.TestCase):
    """
    This class tests adding a professional.
    """

    def setUp(self):
        """
        This method runs before each test.
        """
        self._remove = False

    def test_add_professional(self):
        """
        This method tests adding a professional.
        """
        self._professional_object = Professional.generate_random_professional()
        self._professional_object.add_professional()
        self._professional_object.remove_professional(self._professional_object.name)
        all_professionals = self._professional_object.return_professionals_name()

        self.assertNotIn(self._professional_object.name, all_professionals)

    def tearDown(self):
        """
        This method runs after each test and removes added professional if it exists.
        :return:
        """
        if self._remove:
            self._professional_object.remove_professional(self._professional_object.name)


if __name__ == '__main__':
    unittest.main()
