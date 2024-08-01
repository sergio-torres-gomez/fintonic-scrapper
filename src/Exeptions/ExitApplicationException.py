class ExitApplicationException(BaseException):
    def __init__(self, msg):
        super().__init__(msg)

    def __str__(self):
        return f'{self.args[0]}'