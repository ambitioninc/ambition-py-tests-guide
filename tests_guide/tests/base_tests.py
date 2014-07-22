from datetime import time
import unittest

from tests_guide.base import Resource


class ResourceTests(unittest.TestCase):

    def test_build_param_string(self):
        """
        Tests .build_param_string() returns the correct string
        """
        resource = Resource()

        test_params = [
            False,
            'filter[name]=dev',
            None,
            'page=1',
            0,
            '',
            [],
            {},
            time(0)
        ]

        param_str = resource.build_param_string(test_params)

        self.assertEqual(param_str, 'filter[name]=dev&page=1')

    def test_make_a_network_heavy_call(self):
        self.assertIsNone(Resource().make_a_network_heavy_call())
