import unittest

from mock import Mock, patch

from tests_guide.base import Resource
from tests_guide.consumer import Consumer


class ConsumerTests(unittest.TestCase):
    def test_process_resource(self):

        mock_resource = Mock(name='MyResource')

        mock_resource.make_a_network_heavy_call.return_value = 'Ambition'

        consumer = Consumer()

        # Call the method
        response = consumer.process_resource(mock_resource)

        self.assertEqual(response, '\'Ambition\' is the data')

    @patch.object(Resource, 'make_a_network_heavy_call')
    def test_process_resource_with_patch(self, mock_net_call):
        """
        Test that process resource returns the correct output
        """
        mock_net_call.return_value = 'Ambition'

        consumer = Consumer()
        consumer.API_KEY = 'abc'

        # Call the method
        response = consumer.process_resource(Resource())

        self.assertEqual(response, '\'Ambition\' is the data')

        mock_net_call.assert_called_once_with('abc')
