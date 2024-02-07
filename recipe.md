## 1. Describe the Problem

As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied, telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

As an admin
So that invalid entries are rejected
I want to generate an exception when the date of birth isn't the right type or format.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def age_verifier(dateofbirth):
    """takes in date of birth as string

    Parameters: (list all parameters and their types)
        dateofbirth: a string containing the birthday (e.g. "2023-12-31")

    Returns: (state the return value and its type)
        a message containing either access granted or access denied (e.g. access denied!)

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

def modify_list(lst):
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a birth date which is under 16
It returns the message Acces denied
"""
def age_verifier("2023-01-01") => ["Access denied!"]

"""
Given a birth date which is above 16
It returns the message Acces granted!
"""
def age_verifier("1985-01-01") => ["Access granted!"]

"""
Given the input only includes the year of birth
It returns a the error message Wrong date format!

"""
def age_verifier("1985") => ["Wrong date format!"]

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.age_verifier import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_age_verifier_user_is_old_enough(dateofbirth):
    actual = age_verifier("1985-12-25"):
    expected = "Access granted!"
    assert actual == expected

def test_age_verifier_user_is_old_enough(dateofbirth):
    actual = age_verifier("2015-12-25"):
    expected = "Access denied!"
    assert actual == expected
    
def test_age_verifier_user_is_old_enough(dateofbirth):
    with pytest.raises(Exception) as err:
        age_verifier(dateofbirth):
    actual = str(err.value)
    expected = "Wrong date format!"
    assert actual == expected
```

Ensure all test function names are unique, otherwise pytest will ignore them!
