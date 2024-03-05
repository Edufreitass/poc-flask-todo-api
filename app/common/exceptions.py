class ApplicationError(Exception):
    """Classe base para erros na aplicação."""
    pass


class UserNotFoundError(ApplicationError):
    """Exceção levantada quando um usuário não é encontrado."""

    def __init__(self, user_id):
        self.message = f'User with ID {user_id} not found.'
        super().__init__(self.message)


class InvalidDataError(ApplicationError):
    """Exceção levantada quando dados inválidos são fornecidos a uma função
    ou método."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
