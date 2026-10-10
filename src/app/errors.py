class InvalidAmount(Exception):
    """Raise this exception class when the amount is invalid. For example negative or zero value for deposit/withdraw"""

    pass


class AccountNotFound(Exception):
    """Raise this exception class when the account could not be found."""

    pass
