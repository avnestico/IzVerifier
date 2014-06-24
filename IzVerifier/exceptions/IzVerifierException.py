__author__ = 'fcanas'

class IzVerifierException(Exception):
    """
    General exception thrown by IzVerifier.
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)



class IzArgumentsException(IzVerifierException):
    """
    Thrown when IzVerifier is called with invalid arguments.
    """

class MissingSpecsException(IzVerifierException):
    """
    Thrown when a required xml spec file can't be found.
    """

