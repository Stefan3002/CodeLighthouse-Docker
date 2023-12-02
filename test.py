import unittest

random_tests = [(1, 2), (4, 7)]

def user_function(inputs):
    return inputs[0] * inputs[1]
def true_function(inputs):
    return inputs[0] * inputs[1]
class TestRandomInputs(unittest.TestCase):
    def testing(self):
        for test in random_tests:
            print('Testing with: ', test)
            self.assertEqual(user_function(test), true_function(test))
