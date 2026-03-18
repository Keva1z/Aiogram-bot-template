class UserCreateError(Exception):
    """Unexpected error while creating user"""

    def __init__(self, message: str = "Unexpected error while creating user") -> None:
        super().__init__(message)
