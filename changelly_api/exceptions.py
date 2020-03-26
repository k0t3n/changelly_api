class ChangellyAPIError(Exception):
    pass


class InvalidAmount(ChangellyAPIError):
    def __init__(self, threshold_value: float):
        self.threshold_value = threshold_value


class AmountGreaterThanMaximum(InvalidAmount):
    pass


class AmountLessThanMinimum(InvalidAmount):
    pass


class JSONResponseParseError(ChangellyAPIError):
    pass


class UnexpectedResponseStatusCode(ChangellyAPIError):
    pass


class AuthorizationError(ChangellyAPIError):
    pass
