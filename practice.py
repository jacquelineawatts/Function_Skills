"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:

    >>> hello_world()
    Hello World

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    >>> print_product(3, 5)
    15

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0

    >>> sign_and_parity(3)
    ['Odd', 'Positive']

    >>> sign_and_parity(-2)
    ['Even', 'Negative']

PART TWO:

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn

"""
################################################################################

# PART ONE

# 1. Write a function called 'hello_world' that does not take any arguments and
#    prints "Hello World".

def hello_world():
    """Function takes no input and prints hello world."""

    print 'Hello World'

# 2. Write a function called 'say_hi' that takes a name as a string and
#    prints "Hi" followed by the name.

def say_hi(name):
    """Function takes name as an input and prints hi to name."""

    print "Hi " + name

# 3. Write a function called 'print_product' that takes two integers and multiplies
#    them together. Print the result.

def print_product(a, b):
    """Function takes two integers as input and prints product of those integers."""

    print a * b

# 4. Write a function called 'repeat_string' that takes a string and an integer and
#    prints the string that many times

def repeat_string(string, x):
    """Function takes a string and integer as input and prints string that many times."""

    print string * x

# 5. Write a function called 'print_sign' that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If the integer is 0 print "Zero".

def print_sign(integer):
    """Function takes an integer and prints out if it's great than, less than, or equal to 0."""

    if integer > 0:
        print 'Higher than 0'
    elif integer == 0:
        print 'Zero'
    else:
        print 'Lower than 0'

# 6. Write a function called 'is_divisible_by_three' that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.

def is_divisible_by_three(integer):
    """Function takes an integer and returns True if divisible by 3. If not returns False."""

    if integer % 3 == 0:
        return True
    else:
        return False


# 7. Write a function called 'num_spaces' that takes a sentence as one string and
#    returns the number of spaces.

def num_spaces(sentence):
    """Function takes a string and returns the number of spaces in that string."""

    count = 0
    for char in sentence:
        if char == " ":
            count += 1

    return count


# 8. Write a function called 'total_meal_price' that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.

def total_meal_price(price, percentage = 0.15):
    """Function takes two integers, a price and the percent tip, and returns the total."""

    return price + (price * percentage)

# 9. Write a function called 'sign_and_parity' that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#    should be returned in a list.
#
#    Then, write code that shows the calling of this function
#    on a number and unpack what is returned into two
#    variables --- sign and parity (whether it's even or odd).
#    Print sign and parity.
def sign_and_parity(integer):
    """Function takes an integer, and returns whether it's positive/negative or even/odd."""

    # try:
    #     if integer > 0 and integer % 2 == 0:
    #         return ["Even", "Positive"]
    #     elif integer > 0 and integer % 2 == 1:
    #         return ["Odd", "Positive"]
    #     elif integer < 0 and integer % 2 == 0:
    #         return ["Even", "Negative"]
    #     elif integer < 0 and integer % 2 == 1:
    #         return ["Odd", "Negative"]
    #     elif integer == 0:
    #         return []

    # except TypeError:
    #     return "I'm sorry that's not an integer, please try again."



    sign_and_parity = []

    if integer == 0:
        return []
    else:
        try:
            if integer % 2 == 0:
                sign_and_parity.append('Even')
            else:
                sign_and_parity.append('Odd')

            if integer > 0:
                sign_and_parity.append('Positive')
            else:
                sign_and_parity.append('Negative')

            return sign_and_parity

        except TypeError:
            return "I'm sorry that's not an integer, please try again."


n = 6
sign, parity = sign_and_parity(n)
print "The number %d is %s and %s" % (n, sign, parity)


################################################################################
# PART TWO

# 1. Turn the block of code from the directions into a function.
#    Take a name and a job title as parameters, making it so the
#    job title defaults to "Engineer" if a job title is not passed in.
#    Return the person's title and name in one string.

def full_title(name, job_title = 'Engineer'):
    """Function takes two strings, a name and job title, and then returns the full name as a string."""


    return job_title + ' ' + name

# 2. Given a recipient name & job title and a sender name,
#    print the following letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #1 to construct the full title for the letter's
#    greeting.

def write_letter(recipient_name, job_title, sender_name):


    letter_text = "Dear %s %s, I think you are amazing! Sincerely, %s" % (job_title, recipient_name, sender_name)

    print letter_text


#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
