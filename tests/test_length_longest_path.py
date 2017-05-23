from unittest import TestCase


class TestLength_longest_path(TestCase):
    def test_length_longest_path(self):
        try:
            from build import length_longest_path
        except ImportError:
            self.assertFalse("no function found")

        self.assertRaises(TypeError, length_longest_path, None)
        self.assertEqual(length_longest_path(''), 0)
        file_system = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
        expected = 32
        self.assertEqual(length_longest_path(file_system), expected)
