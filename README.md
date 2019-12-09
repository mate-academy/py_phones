# py_change

In this assignment you must write a phone book. This should be a console-based application. The user can create a new contact by name and phone number, find the contact by name, update the contact by name and delete it by name. Data must be saved in a pickle file. Divide your application into two modules, one for working with data and one for the user interface. Please note that the data module must not contain print () / input () functions.

To deploy project on your local machine create new virtual environment and execute this command:

`pip install -r requirements.txt`

To run all style checkers and tests use commands:

`pytest`

`flake8 main.py contacts.py`

`pylint main.py contacts.py`

`mypy --ignore-missing-imports .`