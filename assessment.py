# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5%

def calculate_tax(price, state, tax = 0.05):
    """Takes two required inputs, item cost as a float and state abbreviation as a string, and one
    optional input, state tax (defaults to '5%' if not provided). Returns total cost."""

    if state == 'CA':
        return price + (price * 0.07)
    else:
        return price + (price * tax)


#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry".

def is_berry(fruit):
    """Takes name of a fruit as a string and returns boolean if fruit is/is not a type of berry."""

    if fruit[-4:] == "erry":
        return True
    else:
        return False

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

def shipping_cost(fruit): 
    """Takes the name of a fruit as string and returns shipping cost as an integer."""

    if is_berry(fruit) == True:
        return 0
    else:
        return 5


# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#

def is_hometown(town):
    """Takes the name of a town as string and returns boolean if is/is not East Greenwich."""

    if town == "East Greenwich":
        return True
    else:
        return False

#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.

def full_name(first_name, last_name):
    """Takes two strings, a first and last name, and returns full name as one string."""

    return first_name + ' ' + last_name

#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you
#        from?" depending on what `is_hometown()` evaluates to.

def hometown_greeting(town, first_name, last_name):
    """Takes three strings-town, first, and last name, and returns a greeting if town
    evaluates True to is_hometown, else returns question."""

    name = full_name(first_name, last_name)
    if is_hometown(town) == True:
        return "Hi, %s, we're from the same place!" % name
    else:
        return "Hi, %s, where are you from?" % name

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()``
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

def increment(x = 1):
    """Takes integer input, defaults to 1 if none provided, and returns output
    from inner function, add."""

    def add(y = 1):
        """Takes integer input, defaults to 1 if none provided, and returns integer
        sum of inner and outer fuction parameters."""
        return x + y
    return add()


# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call
#    addfive with y = 5. Call again with y = 20.

add_five = increment(5)
print add_five

def increment(x = 1):

    def add(y = 1):
        return x + y
    return add(5)

add_five = increment(5)
print add_five


def increment(x = 1):

    def add(y = 1):
        return x + y
    return add(20)

add_five = increment(5)
print add_five


# -------------------------- ALTERNATIVE SOLUTION ----------------------------
# Not really sure I'm understanding the directions above, they're pretty unclear,
# and the above way of changing the y value each time is pretty terrible, rather than
# just including it in the outer functions parameteres. So here's the way I would do it.

def increment(y, x = 1):
    """Takes two integers, a number and the preferred increment (defaults to 1 if
        not provided) and returns the incremented result."""

    def add(y):
        return x + y
    return add(y)


# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

def append_to_list(number, lst):
    """Takes integer and list of integers, returns list with integer appended."""

    lst.append(number)
    return lst

#####################################################################
