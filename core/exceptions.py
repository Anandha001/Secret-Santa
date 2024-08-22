class DigitalXCError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class FileFormatError(DigitalXCError):

    def __init__(self, file_uri: str) -> None:
        message = f"Invalid file format for file '{file_uri}'. Only excel, csv files are supported."
        super().__init__(message)


class FileReadError(DigitalXCError):

    def __init__(self, file_uri: str) -> None:
        message = f"File '{file_uri}' could not be read."
        super().__init__(message)


class FileWriteError(DigitalXCError):

    def __init__(self, file_uri: str) -> None:
        message = f"File '{file_uri}' could not be read."
        super().__init__(message)
