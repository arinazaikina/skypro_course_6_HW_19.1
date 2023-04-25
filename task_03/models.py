class Message:
    """
    Класс, описывающий модель сообщения
    """

    @classmethod
    def get_hello_message(cls) -> str:
        """
        Возвращает приветственное сообщение
        """
        return 'Hello, World wide web!'

    @classmethod
    def get_success_message(cls) -> str:
        """
        Возвращает сообщение об успешной отправке данных на сервер
        """
        return 'Data successfully sent to the server'
