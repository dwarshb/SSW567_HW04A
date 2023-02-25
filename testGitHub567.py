import unittest
import mock

import GitHub567
from GitHub567 import gitHubApi


# Mocking service calls
@mock.patch('GitHub567.gitHubApi', return_value=False)
class testRepo(unittest.TestCase):
    # Test case for when user is not present
    def testNoUser(self, mock_check_output):
        actual_result = GitHub567.gitHubApi()
        expected_result = False
        self.assertEqual(expected_result, actual_result)  # Checking the final and expected result

    # Test case for when user is found
    def testUserFound(self, mock_check_output):
        actual_directory = GitHub567.gitHubApi()
        expected_directory = True
        self.assertNotEqual(expected_directory, actual_directory)  # Checking the final and expected result


if __name__ == '__main__':
    unittest.main()
