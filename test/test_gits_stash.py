# import subprocess
# from subprocess import PIPE
# import unittest
# from unittest.mock import patch, Mock
# from gits_stash import gits_stash  # Import the module you want to test


# class TestGitsStash(unittest.TestCase):

#     @patch("builtins.input", side_effect=["Y", "Custom Stash Label"])
#     @patch("subprocess.Popen")
#     def test_gits_stash_with_label(self, mock_popen, mock_input):
#         mocked_pipe = Mock()
#         attrs = {
#             'communicate.return_value': ('Stash saved.'.encode('UTF-8'), 'error'),
#             'returncode': 0
#         }
#         mocked_pipe.configure_mock(**attrs)
#         mock_popen.return_value = mocked_pipe

#         args = None  # You can pass the args if needed
#         result = gits_stash.gits_stash(args)
#         self.assertTrue(result, "gits_stash function should return True")

#     @patch("builtins.input", side_effect=["N"])
#     @patch("subprocess.Popen")
#     def test_gits_stash_without_label(self, mock_popen, mock_input):
#         mocked_pipe = Mock()
#         attrs = {
#             'communicate.return_value': ('Stash saved.'.encode('UTF-8'), 'error'),
#             'returncode': 0
#         }
#         mocked_pipe.configure_mock(**attrs)
#         mock_popen.return_value = mocked_pipe

#         args = None  # You can pass the args if needed
#         result = gits_stash.gits_stash(args)
#         self.assertTrue(result, "gits_stash function should return True")


# if __name__ == '__main__':
#     unittest.main()
