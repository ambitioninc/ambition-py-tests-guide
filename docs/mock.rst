Mock
====

From the `Mock`_ documentation:

    mock is a library for testing in Python. It allows you to replace parts of your system under test with mock objects
    and make assertions about how they have been used.

.. _Mock: http://www.voidspace.org.uk/python/mock/

You'll need to read the Mock documentation to really understand its internals, but the following guide is meant to just
introduce how it can be used.

Mock Class
----------
The :class:`Mock <mock:mock.Mock>` class is very useful for isolating your test to just the function or method you are
writing a test for, instead of setting up all kinds of state in your test class.

.. code-block:: python

    class Consumer(object):
        """
        A class for consuming resources
        """
        API_KEY = 'abcdefghijklmnopqustuvwxyz'
        def process_resource(self, resource):
            """
            This method processes Resource objects and returns a printable string
            """
            response = resource.make_a_network_heavy_call(self.API_KEY)
            return '\'{0}\' is the data'.format(response)

Notice that the ``process_resource()`` method calls a method ``make_a_network_heavy_call()`` on the resource that is
passed in. Typically we don't want to be contacting other services from inside our tests. Let's mock that call out:

.. code-block:: python

    import unittest

    from mock import Mock

    from tests_guide.consumer import Consumer


    class ConsumerTests(unittest.TestCase):
        def test_process_resource(self):
            """
            Test that process resource returns the correct output
            """
            mock_resource = Mock(name='MyResource')
            mock_resource.make_a_network_heavy_call.return_value = 'Ambition'

            consumer = Consumer()
            consumer.API_KEY = 'abc'

            # Call the method
            response = consumer.process_resource(mock_resource)

            self.assertEqual(response, '\'Ambition\' is the data')

            mock_resource.make_a_network_heavy_call.assert_called_once_with('abc')

In this Unit test, we really only want to verify that the relevant unit of our code is measured, and that is verifying
that we properly format the response in a string. We also verify that our network heavy call used the correct API key.

patch
-----
:func:`patch <mock:mock.patch>` is a powerful decorator and context manager that makes isolating your tests really easy.
Patch `patches` a method on an object and returns an instance of Mock instead of the original function's call.

Let's extend our previous example usage of mock and show how patch can be used to simplify our test.

.. code-block:: python

    import unittest

    from mock import patch

    from tests_guide.consumer import Consumer
    from tests_guide.base import Resource


    class ConsumerTests(unittest.TestCase):
        @patch.object(Resource, 'make_a_network_heavy_call')
        def test_process_resource(self, mock_net_call):
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

So we replaced the ``make_a_network_heavy_call`` method on the Resource class and returned our Mock object instead.
