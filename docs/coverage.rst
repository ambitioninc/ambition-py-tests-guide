Coverage
========
From the `Coverage`_ documentation:

    Coverage.py is a tool for measuring code coverage of Python programs. It monitors your program, noting which parts
    of the code have been executed, then analyzes the source to identify code that could have been executed but was not.

At Ambition, we attempt to get 100% test coverage on all our python projects. This does not eliminate bugs, but
significantly reduces the amount of small easily caught bugs in a project.

Installation
------------
.. code-block:: bash

    $ pip install coverage

Running coverage from the terminal
----------------------------------
For Django projects, coverage can be run from the terminal by simply calling:

.. code-block:: bash

    $ coverage run setup.py test
    $ coverage report --fail-under=100

For pure Python projects you can simply call:

.. code-block:: bash

    $ python setup.py nosetests

.coveragerc configuration
-------------------------
To configure coverage, there is a ``.coveragerc`` file that can configure ``run``, ``report``, and more commands.

.. code-block:: guess

    [run]
    branch = True
    omit =
        tests_guide/migrations/*
        tests_guide/version.py
    source = tests_guide
    [report]
    exclude_lines =
        # Have to re-enable the standard pragma
        pragma: no cover
        # Don't complain if tests don't hit defensive assertion code:
        raise NotImplementedError
    show_missing = 1

Nose plugin configuration
-------------------------
For pure python projects, the file ``setup.cfg`` has the relevant coverage configuration. An example might look like
this:

.. code-block:: guess

    [nosetests]
    with-coverage = 1
    cover-branches = 1
    cover-min-percentage = 100
    cover-package = tests_guide

HTML Report
-----------
To produce an HTML report of your code coverage, run:

.. code-block:: bash

    $ coverage html && open htmlcov/index.html