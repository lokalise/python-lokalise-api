.. index:: Contributing (developers)

Contributing
============

1. Fork the repository.
2. Create a topic branch.
3. Install the necessary dependencies with ``pipenv install``. If you don't have pipenv, `find installation instructions here <https://pipenv.pypa.io/en/latest/install/#installing-pipenv>`_.
4. Implement your feature or bug fix.
5. Don't forget to add tests and make sure they pass.
6. Make sure your code complies with the style guide by running ``pipenv run pylint lokalise/``. ``pipenv run autopep8 -i -r lokalise/ -a`` can automatically fix many issues for you.
7. If necessary, add documentation for your feature or bug fix.
8. Commit and push your changes.
9. Submit a pull request.

.. index:: Tests (developers)

Running tests
-------------

1. Copypaste ``.env.example`` file as ``.env``.
2. Put your API token inside. The ``.env`` file is excluded from version control so your token is safe. All in all, we use pre-recorded VCR cassettes, so the actual API requests won't be sent.
3. Run ``pipenv run pytest``. Observe test results and coverage. All your tests will be linted automatically.
