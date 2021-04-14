import unittest

from projects.project1.submit.problem_2 import find_files


class TestRecursion(unittest.TestCase):

    def setUp(self):
        testdir = "/Users/jnorman/workspace/udacity/projects/project1/smalltest"

        self.result = find_files(".", testdir)

    def test_returns_list_type(self):
        self.assertIsInstance(self.result, list)

    def test_returns_list_of_files(self):
        self.assertListEqual(self.result, ['test.txt', 'test1.txt', 'test2.txt'])




if __name__ == "__main__":
    unittest.main()