"""
    NOTE: Install mypy before starting this chapter.
    (In your terminal, write "pip install mypy")
    Also go to the "Extensions" tab in your VSCode sidebar and install the mypy extension.
"""

"""-------------------------------------------------------------------------------------------"""

"""
    When we're talking about typing here, we're talking about types of variables.
    For example, given x = 1, x would be a number (or more specifically, an integer).
    Thinking about code in terms of types helps with writing solid code.
    For that reason, I recommend writing Python with types.
    The benefit of this is greater understanding of your code and better autocomplete.
"""

### EXAMPLE

## Writing something without a type
x = 1

## With a type
x: int = 1

"""
    In this simple example, writing the type might seem pointless.

    However, imagine this:
        You're getting data from a database. The data is a list of records.
        A record is a dictionary (a collection of key: value pairs).
        The field names of the record (ie 'Name', 'Phone Number' etc) are the record's KEYS.
        The actual names and phone numbers (ie 'John', '0402853916') are the record's VALUES.

    These sorts of situations make types very handy, because VSCode's autocomplete will know
    that the values of your records are strings, and will give you string methods accordingly.
"""

### EXAMPLE
## Imagine we're receiving these two records
example_records = [
    {
        "Name": "Jesse",
        "Phone Number": "0400203941",
        "Occupation": "Resident Nerd",
    },
    {"Name": "Angus", "Phone Number": "0421932791", "Occupation": "Honourary Nerd"},
]

## We could receive these one record at a time and add them to a new list.
## Create the list, specifying the appropriate types.
## Note: list[dict[str, str]] is a list of dictionaries, with strings for keys and strings for values.
new_list: list[dict[str, str]] = []

## Add each record to the new list
for record in example_records:
    new_list.append(record)

"""
    Creating a habit of doing this means you'll understand what your code is doing better.
    You will also notice the shape of your data more intimately, and get all that autocomplete niceness.
    However, Python doesn't use the types to improve performance, and Python doens't have proper types.
    Many other languages do have real types, so it's a good thing to think about early.
"""

### EXAMPLE
## Python not having real types
x: int = 1
x = "hello"

"""
    This is fine in Python, but often wouldn't work elsewhere and probably isn't allowed by mypy.

    You can also use types for function parameters and output values.
    This is very helpful for documenting what the function actually does.
"""


### EXAMPLE
## Annotate the parameter types like you would with a variable.
## Annotate the return type after a ->
def divide_two_integers(integer_1: int, integer_2: int) -> float:
    return integer_1 / integer_2


"""
    Imagine a codebase where you have 20 different files.
    You might use this function across 12 of those files.
    Doing this means you can just hover over the function wherever you use it, and you'll know how to use it.
"""

"""
    You can also use types with classes.
"""


### EXAMPLE
class Supporter:
    def __init__(self, name: str, age: int, accepts_emails: bool) -> "Supporter":
        self.name: str = name
        self.age: int = age
        self.accepts_emails: bool = accepts_emails
