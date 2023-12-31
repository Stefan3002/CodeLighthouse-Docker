import unittest

from vol.userFile import user_function
from vol.authorFile import true_function
from vol.randomFile import random_function


random_tests = random_function()
class TestRandomInputs(unittest.TestCase):
    def testing(self):
        for test in random_tests:
            print('Testing with: ', test)
            self.assertEqual(user_function(test), true_function(test))
