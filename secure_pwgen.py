# Louie Bloomberg
# The Secure Password Generator!

__version__ = "0.2.0"

# Importing Modules:
import random
import string
import secrets
import math


#######BEGIN FUNCTION DEFINITIONS###################
def load_words(file):
    """
    Function loads words into list, words
    Param: file, string - it contains the name of the text file with the words to be used for the password.
    Returns: words, a list containing the words.
    """
    with open(file, "r", encoding="utf8") as infile:
        words = infile.read().split()

    return words


def print_password_types():
    """
    This password prints out the possible types of passwords and what number to use when asked to enter a number
    Params: None
    Returns: None
    """
    print("Welcome to the Secure Password Generator")
    print("To begin, please select the type of password you would like using a num-pad/num-row on your keyboard.")
    print("1. Alphanumeric Password")
    print("2. Alphabetic Password: 2")
    print("3. Numeric Password: 3")
    print("4. Completely Random Password: 4")


def get_pw_type():
    """
    This function handles user selection of the password type.
    Params: NONE
    Return Value: an integer containing the number corresponding to the type of password.
    """
    select1 = -1
    sel = True
    while sel == True:
        select1 = int(input("Choose your password type: "))
        if (select1 == 1 or select1 == 2 or select1 == 3 or select1 == 4):
            sel = False
        else:
            print("Invalid input: please enter either 1, 2, 3, 4: ")
    return select1

def pw_start(select1, words, ascii_list):
    """
    This function provides the backbone for creating the user's password as it handles calling to the password generators
    Params: select1: an integer containing the number corresponding to the type of password.
            words: a list containing the words to be used for the password from words_alpha.txt
            ascii_list: a list containing the characters to be used for the password from the ASCII character set
    Returns: password: a string containing the generated password.
    """

    if select1 == 1:
        print("This password will contain words, numbers, and punctuation.")
        password = create_alphanumeric_password(words)
        return password
    elif select1 == 2:
        print("This password will contain at least four words.")
        num_words = get_pw_length(2)
        password = create_word_password(words, num_words)
        return password
    elif select1 == 3:
        print("This password will only contain numbers.")
        digits = get_pw_length(3)
        password = create_num_password(digits)
        return password
    elif select1 == 4:
        print("This password will consist of all ASCII Characters in a random order.")
        num_chars = get_pw_length(4)
        password = create_random_password(ascii_list, num_chars)
        return password


def get_pw_length(sel):
    """
    Asks user for character length based on their selection from earlier
    Parameter: sel, an integer corresponding to their choice from above.
    Returns: length, an integer instructing the program how many characters are required.
    """
    if sel == 2:  # word only
        length = int(input("How many words should the password be? (Must be 4+ - default = 4) "))
        if length >= 4:
            return length
        else:
            return 4
    elif sel == 3:  # numeric
        length = int(input("How many digits should the passcode be? (Must be 8+ digits - default = 8) "))
        if length >= 8:
            return length
        else:
            return 8
    elif sel == 4:  # random
        length = int(input("How many characters should the password be? (Must be 12+ characters - default = 16) "))
        if length >= 12:
            return length
        else:
            return 16


def create_alphanumeric_password(words):  # 1 (Default Password) - This is the standard alphanumeric password
    """
    This function creates an alphanumeric password by choosing two words from the words list, 4 random numbers, and a punctuation mark.
    Parameter: words, a list containing the English dictionary
    Returns: password, a string containing the alphanumeric password in the following format: Word1+word2+4-digit-number+punctuation-mark.
    """
    two_words = ""  # stores the two random words
    for i in range(2):  # add two random words
        two_words += secrets.choice(words)
    # Now numbers
    passcode = create_num_password(4)  # calls the create_number_password function to create 4 digit passcode
    punc_list = string.punctuation
    punc_mark = secrets.choice(punc_list)  # Chooses ASCII punctuation

    password = two_words + str(passcode) + punc_mark  # adds everything together
    password = password.capitalize()  # capitalizes the first letter
    return password  # returns alphanumeric password


def create_word_password(words, num_words):  # 2
    """
    Function creates an alphabetic password by choosing four words from the words list and combines them
    Parameter: words, a list containing the words
               num_words, an integer which must be greater than 4
    Returns: password, a string containing the password
    """
    password = ""
    for i in range(num_words):
        password += secrets.choice(words)

    return password


def create_num_password(digits):  # 3
    """
    Creates a numeric password of a length entered by user. Default = 8 (sent from pw_length function, must be greater than 8 digits
    Params: digits, an integer.
    Returns: passcode, an integer containing the passcode

    EXCEPTION: This function is used in the alphanumeric, and it produces a 4 digit number
    """
    seed = secrets.randbits(256)
    random.seed(seed)
    num = random.random()
    tens_place = math.pow(10, digits)
    passcode = num * tens_place
    passcode = math.trunc(passcode)
    return passcode


def create_random_password(ascii_list, num_chars):  # 4
    """
    Uses the 94 possible ascii charater set (uppercase, lowercase, digits, and punctuation) to make a random password
    Parameter: ascii_list, a string containing all possible ascii characters (excluding whitespace).
               num_chars, an integer must be greater than 12 characters with a default of 16 characters
    Returns: password, a string containing the password
    """

    password = ""
    for i in range(num_chars):
        password += secrets.choice(ascii_list)

    return password


####################MAIN######################

# Load File:
words = load_words(
    "words_alpha.txt") # You can replace words_alpha.txt with any other document that contains the words you would like to use

# Create ASCII list
ascii_list = string.ascii_letters + string.digits + string.punctuation

print_password_types() #prints the password types available
pw_type = get_pw_type() #gets the password type the user would like generated
password = pw_start(pw_type, words, ascii_list) #starts the password generation
print(password) #prints the generated password


