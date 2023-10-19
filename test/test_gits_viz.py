import unittest
from unittest.mock import patch
from io import StringIO
from gits_viz import gits_viz_func


class TestGitsVizFunc(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_gits_viz_func_with_visualization(self, mock_stdout):
        class Args:
            g = True
            f = "output.png"
            s = True

        args = Args()
        result = gits_viz_func(args)

        self.assertTrue(result)
        self.assertIn("ExpectedOutputString", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_gits_viz_func_without_visualization(self, mock_stdout):
        class Args:
            g = False
            f = None
            s = False

        args = Args()

        result = gits_viz_func(args)

        self.assertTrue(result)
        self.assertIn("ExpectedOutputString", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_gits_viz_func_with_exception(self, mock_stdout):
        class Args:
            g = True
            f = "output.png"
            s = True

        args = Args()

        with patch('your_module.subprocess.Popen') as mock_popen:
            mock_popen.side_effect = Exception("Mocked Exception")

            result = gits_viz_func(args)

        self.assertFalse(result)
        self.assertIn("ERROR: gits viz command caught an exception", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
