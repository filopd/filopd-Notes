
class InvalidPasswordException(Exception):
    pass
    #This is InvalidPasswordException when length of password is less than 8.

try:
    i = (input(("Enter the Password: ")))
    if (len(i) <8):
        raise InvalidPasswordException
except InvalidPasswordException:
    print("Length of your password (", i, ") is ", len(i), ". Kindly re-enter more than 8.")
finally:
    print("End of Program.")

