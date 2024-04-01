from inquirer import Text, prompt, List,Checkbox
from re import match
cash = [Text('FullName', message="Please enter full name",validate=lambda _, x: match(r'^(?:(?:\+|00)([1-9]\d{0,2})|0)(?:\s?|-?)([1-9]\d{0,3})(?:\s?|-?)(\d{4,})$', x))]
while True:
    prompt(cash)
