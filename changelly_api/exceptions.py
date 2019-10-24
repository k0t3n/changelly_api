class ChangellyAPIError(Exception):
    pass


class JSONResponseParseError(ChangellyAPIError):
    pass


class UnexpectedResponseStatusCode(ChangellyAPIError):
    pass


class AuthorizationError(ChangellyAPIError):
    pass
