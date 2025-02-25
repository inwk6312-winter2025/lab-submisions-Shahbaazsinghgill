class CustomError(Exception):
    """A custom exception with a message."""
    
    def __init__(self, message="Something went wrong!"):
        self.message = message
        super().__init__(self.message)

# Raise exception with a custom message
raise CustomError("Invalid Input!")








