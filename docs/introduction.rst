Introduction to Testing
=======================

This introduction is specifically aimed at developers new to testing or new to testing in python. Say we have a python
module called ``test_guide`` containing a file ``base.py`` with a class called ``Resource`` in it that has some methods
on it.

Code to test
------------

.. code-block:: python

    class Resource(object):
        """
        A base class for API resources
        """
        ...
        ...
        def build_param_string(self, params):
            """
            This is a simple helper method to build a parameter string. It joins
            all list elements that evaluate to ``True`` with an ampersand, '&'

            .. code-block:: python

                >>> parameters = Resource().build_param_string([
                ...    'filter[name]=dev', None, 'page=1'
                ...    ])
                ...
                >>> print parameters
                filter[name]=dev&page=1

            :type params: list
            :param params: The parameters to build a string with

            :rtype: str
            :return: The compiled parameter string
            """
            return '&'.join([p for p in params if p])

Setup
-----
We first need a ``tests`` directory in our module with a file called ``base_tests.py`` in it. Our example structure
looks like this:

.. code-block:: bash

    $  ls -alR tests_guide
    total 24
    drwxr-xr-x   6 ubuntu  ubuntu   204 Jul 22 10:39 .
    drwxr-xr-x  24 ubuntu  ubuntu   816 Jul 22 10:36 ..
    -rw-r--r--   1 ubuntu  ubuntu    47 Jul 22 10:05 __init__.py
    -rw-r--r--   1 ubuntu  ubuntu  1520 Jul 22 10:39 base.py
    drwxr-xr-x   4 ubuntu  ubuntu   136 Jul 22 10:45 tests
    -rw-r--r--   1 ubuntu  ubuntu    19 Jul 22 10:05 version.py

    ./tests:
    total 8
    drwxr-xr-x  4 ubuntu  ubuntu  136 Jul 22 10:45 .
    drwxr-xr-x  6 ubuntu  ubuntu  204 Jul 22 10:39 ..
    -rw-r--r--  1 ubuntu  ubuntu    0 Jul 22 10:05 __init__.py
    -rw-r--r--  1 ubuntu  ubuntu  125 Jul 22 10:05 base_tests.py

Writing an example test
-----------------------

Now we want to test the ``build_param_string()`` method on our ``Resource`` class. Since we only want the results that
evaluate to ``True`` in the method, we need to test it with a bunch of values that evaluate to ``False``.

.. code-block:: python

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

Did you see what happened? We first have a test class to group our tests of the ``Resource`` class. Then we have a
method ``test_build_param_string()`` that actually runs the tests. Tests in python are assertions, and the builtin
TestCase has a lot of helpful assertions. For this test, we simply assert that our method's output is equal to the
output we expect by calling ``assertEqual()``. We could just as easily used the built in ``assert`` keyword like so:

.. code-block:: python

    assert param_str == 'filter[name]=dev&page=1'

If our method's output had been different than what we expected, our test would have raised an
:class:`AssertionError <exceptions.AssertionError>` and the test would be marked as Failed.


Running the tests
-----------------
In all of the Ambition python templates a testing framework is built in and there is a
:doc:`Contributing <contributing>` section with instructions on how to run the tests. It may differ slightly depending
on if the project is a Django app or a pure Python project.

If the project is pure Python, you can run:

.. code-block:: bash

    $ python setup.py nosetests

If the project is a Django app or Django project:

.. code-block:: bash

    $ python setup.py test


Example output:

.. code-block:: bash

    $ python setup.py test
    running test
    running egg_info
    writing top-level names to ambition_py_tests_guide.egg-info/top_level.txt
    writing ambition_py_tests_guide.egg-info/PKG-INFO
    writing requirements to ambition_py_tests_guide.egg-info/requires.txt
    writing dependency_links to ambition_py_tests_guide.egg-info/dependency_links.txt
    reading manifest file 'ambition_py_tests_guide.egg-info/SOURCES.txt'
    reading manifest template 'MANIFEST.in'
    writing manifest file 'ambition_py_tests_guide.egg-info/SOURCES.txt'
    running build_ext
    nosetests tests_guide --verbosity=1
    Creating test database for alias 'default'...
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.001s

    OK
    Destroying test database for alias 'default'...