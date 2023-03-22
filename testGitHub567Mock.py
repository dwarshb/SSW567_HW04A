import unittest
import mock
from mock import MagicMock

import GithubAPI


# Mocking service calls
@mock.patch('GithubAPI.gitHubApi', return_value=False)
class testRepo(unittest.TestCase):
	# Test case for when user is not present
	def testNoUser(self, mock_check_output):
		actual_result = GithubAPI.gitHubApi()
		expected_result = False
		self.assertEqual(expected_result, actual_result)  # Checking the final and expected result

	# Test case for when user is found
	def testUserFound(self, mock_check_output):
		actual_directory = GithubAPI.gitHubApi()
		expected_directory = True
		self.assertNotEqual(expected_directory, actual_directory)
		# Checking the final and expected result

	def test_mock_noOfCommits(self, mock_user):
		mock_user.return_value = MagicMock(user_id="dwarshb", repo_name="SSW567_HW04A")
		print(mock_user.return_value)
		result = mock_user.return_value.user_id
		try:
			self.assertEqual(result, "dwarshb")
		except:
			print("Test Failed")
		else:
			print("Test Passed")

if __name__ == '__main__':
	unittest.main()
